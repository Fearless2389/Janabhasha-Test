import pandas as pd
import os
import json
from datetime import datetime
import whisper
import openai
from typing import Dict, List, Optional, Tuple

class JanaBhashaDB:
    def __init__(self):
        self.data_dir = "data"
        self.dict_file = os.path.join(self.data_dir, "Dictionary.csv")
        self.audio_dir = os.path.join(self.data_dir, "Audio_Transcripts")
        self.trigger_file = os.path.join(self.data_dir, "trigger.txt")
        
        # Create directories if they don't exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)
        
        # Initialize database
        self._init_database()
        
        # Initialize Whisper model
        self.whisper_model = None
        
    def _init_database(self):
        """Initialize the database with sample data if it doesn't exist"""
        if not os.path.exists(self.dict_file):
            sample_data = {
                'id': [1, 2, 3, 4, 5],
                'word': ['Namaste', 'Dhanyavaad', 'Kya haal hai', 'Acha', 'Shukriya'],
                'meaning': ['Hello/Greeting', 'Thank you', 'How are you?', 'Good', 'Thank you'],
                'translated_word': ['Hello', 'Thank you', 'How are you?', 'Good', 'Thank you'],
                'translated_meaning': ['Hello/Greeting', 'Thank you', 'How are you?', 'Good', 'Thank you'],
                'example': ['Namaste, kaise ho?', 'Dhanyavaad aapka', 'Kya haal hai dost?', 'Acha lag raha hai', 'Shukriya aapka'],
                'translated_example': ['Hello, how are you?', 'Thank you', 'How are you friend?', 'It feels good', 'Thank you'],
                'language': ['Hindi', 'Hindi', 'Hindi', 'Hindi', 'Hindi'],
                'type': ['Word', 'Word', 'Phrase', 'Word', 'Word'],
                'audio_file': ['', '', '', '', ''],
                'transcript': ['', '', '', '', ''],
                'contributor': ['System', 'System', 'System', 'System', 'System'],
                'timestamp': [datetime.now().isoformat()] * 5,
                'verified': [True] * 5
            }
            df = pd.DataFrame(sample_data)
            df.to_csv(self.dict_file, index=False)
    
    def load_data(self) -> pd.DataFrame:
        """Load data from CSV file"""
        try:
            df = pd.read_csv(self.dict_file)
            return df
        except FileNotFoundError:
            return pd.DataFrame()
    
    def save_data(self, df: pd.DataFrame):
        """Save data to CSV file"""
        df.to_csv(self.dict_file, index=False)
        self._update_trigger()
    
    def add_entry(self, entry: Dict) -> bool:
        """Add a new entry to the database with automatic translation"""
        try:
            df = self.load_data()
            
            # Generate new ID
            new_id = 1 if df.empty else df['id'].max() + 1
            
            # Add timestamp
            entry['id'] = new_id
            entry['timestamp'] = datetime.now().isoformat()
            entry['verified'] = False
            
            # Auto-translate content if OpenAI is available
            entry = self._auto_translate_entry(entry)
            
            # Add to dataframe
            new_row = pd.DataFrame([entry])
            df = pd.concat([df, new_row], ignore_index=True)
            
            # Save
            self.save_data(df)
            return True
        except Exception as e:
            print(f"Error adding entry: {e}")
            return False
    
    def _auto_translate_entry(self, entry: Dict) -> Dict:
        """Automatically translate entry content to English using Puter.js"""
        try:
            from modules.PuterTranslate import translate_text
            
            # Get language code
            source_lang = self._get_language_code(entry.get('language', 'auto'))
            
            # Translate word
            if entry.get('word') and not entry.get('translated_word'):
                entry['translated_word'] = translate_text(entry['word'], source_lang, 'en')
            
            # Translate meaning
            if entry.get('meaning') and not entry.get('translated_meaning'):
                entry['translated_meaning'] = translate_text(entry['meaning'], source_lang, 'en')
            
            # Translate example
            if entry.get('example') and not entry.get('translated_example'):
                entry['translated_example'] = translate_text(entry['example'], source_lang, 'en')
            
            # Translate transcript if available
            if entry.get('transcript') and not entry.get('translated_transcript'):
                entry['translated_transcript'] = translate_text(entry['transcript'], source_lang, 'en')
            
            return entry
            
        except Exception as e:
            print(f"Translation failed: {e}")
            # Set defaults if translation fails
            entry.setdefault('translated_word', entry.get('word', ''))
            entry.setdefault('translated_meaning', entry.get('meaning', ''))
            entry.setdefault('translated_example', entry.get('example', ''))
            entry.setdefault('translated_transcript', entry.get('transcript', ''))
            return entry
    
    def _get_language_code(self, language_name: str) -> str:
        """Convert language name to language code"""
        language_map = {
            "Hindi": "hi", "Telugu": "te", "Kannada": "kn", "Tamil": "ta",
            "Malayalam": "ml", "Marathi": "mr", "Gujarati": "gu", "Punjabi": "pa",
            "Bengali": "bn", "Odia": "or", "English": "en", "Chinese": "zh",
            "Japanese": "ja", "auto": "auto"
        }
        return language_map.get(language_name, language_name.lower())
    
    def search_entries(self, query: str = "", language: str = "", entry_type: str = "") -> pd.DataFrame:
        """Search entries with filters"""
        df = self.load_data()
        
        if query:
            mask = (
                df['word'].str.contains(query, case=False, na=False) |
                df['meaning'].str.contains(query, case=False, na=False) |
                df['example'].str.contains(query, case=False, na=False)
            )
            df = df[mask]
        
        if language:
            df = df[df['language'] == language]
        
        if entry_type:
            df = df[df['type'] == entry_type]
        
        return df
    
    def get_languages(self) -> List[str]:
        """Get list of available languages"""
        df = self.load_data()
        return sorted(df['language'].unique().tolist())
    
    def get_entry_types(self) -> List[str]:
        """Get list of available entry types"""
        return ['Word', 'Phrase', 'Folk Song', 'Story']
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """Transcribe audio using Whisper"""
        try:
            if self.whisper_model is None:
                self.whisper_model = whisper.load_model("tiny")
            
            result = self.whisper_model.transcribe(audio_file_path)
            return result["text"]
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""
    
    def enhance_with_openai(self, text: str, language: str) -> Dict:
        """Enhance text using Puter.js"""
        try:
            # Import the translation module
            from modules.PuterTranslate import enhance_meaning
            return enhance_meaning("", text, language)
                
        except Exception as e:
            print(f"Error enhancing with OpenAI: {e}")
            return {"enhanced_meaning": text, "related_words": [], "cultural_context": ""}
    
    def save_audio_file(self, audio_bytes: bytes, filename: str) -> str:
        """Save audio file and return path"""
        file_path = os.path.join(self.audio_dir, filename)
        with open(file_path, "wb") as f:
            f.write(audio_bytes)
        return file_path
    
    def _update_trigger(self):
        """Update trigger file for live refresh"""
        with open(self.trigger_file, "w") as f:
            f.write(datetime.now().isoformat())
    
    def get_basic_stats(self) -> Dict:
        """Get basic statistics"""
        df = self.load_data()
        
        if df.empty:
            return {
                'total_words': 0,
                'languages': 0,
                'audio_files': 0,
                'contributors': 0,
                'verified_entries': 0
            }
        
        return {
            'total_words': len(df),
            'languages': len(df['language'].unique()),
            'audio_files': len(df[df['audio_file'] != '']),
            'contributors': len(df['contributor'].unique()),
            'verified_entries': len(df[df['verified'] == True])
        }
    
    def get_analytics_data(self) -> Dict:
        """Get detailed analytics data"""
        df = self.load_data()
        
        if df.empty:
            return {}
        
        # Language distribution
        lang_dist = df['language'].value_counts().to_dict()
        
        # Type distribution
        type_dist = df['type'].value_counts().to_dict()
        
        # Recent activity (last 30 days)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        recent_df = df[df['timestamp'] >= (datetime.now() - pd.Timedelta(days=30))]
        recent_activity = len(recent_df)
        
        # Top contributors
        top_contributors = df['contributor'].value_counts().head(5).to_dict()
        
        return {
            'language_distribution': lang_dist,
            'type_distribution': type_dist,
            'recent_activity': recent_activity,
            'top_contributors': top_contributors
        }

# Global database instance
db = JanaBhashaDB()

# Convenience functions
def load_data():
    return db.load_data()

def save_data(df):
    return db.save_data(df)

def add_entry(entry):
    return db.add_entry(entry)

def search_entries(query="", language="", entry_type=""):
    return db.search_entries(query, language, entry_type)

def get_languages():
    return db.get_languages()

def get_entry_types():
    return db.get_entry_types()

def transcribe_audio(audio_file_path):
    return db.transcribe_audio(audio_file_path)

def enhance_with_openai(text, language):
    return db.enhance_with_openai(text, language)

def save_audio_file(audio_bytes, filename):
    return db.save_audio_file(audio_bytes, filename)

def get_basic_stats():
    return db.get_basic_stats()

def get_analytics_data():
    return db.get_analytics_data()
