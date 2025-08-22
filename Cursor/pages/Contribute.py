import streamlit as st
import os
import pandas as pd
from datetime import datetime
from io import BytesIO
import tempfile
import wave
import uuid

# ✅ Modular imports
import modules.Database as db

def show():
    # Page config
    st.markdown("## ➕ Contribute to JanaBhasha")
    st.markdown("Help preserve India's linguistic heritage by adding words, phrases, folk songs, and stories.")
    
    # Example section
    with st.expander("📌 Example Format", expanded=True):
        st.markdown("""
        **Word**: ಅಮ್ಮ  
        **Meaning**: *Mother*  
        **Language**: Kannada  
        **Example Sentence**: ಅಮ್ಮ ನನ್ನಿಗೆ ಇಷ್ಟವಾಗಿದೆ.
        """)
    
    st.divider()
    
    # Main contribution form
    st.markdown("### 📤 Submit Your Entry")
    
    # Form
    with st.form("contribute_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            word = st.text_input("🔤 Word/Title (in native script)", placeholder="e.g., చదువు")
            meaning = st.text_input("📘 Meaning", placeholder="e.g., Study")
            language = st.selectbox("🌐 Language", [
                "Telugu", "Hindi", "Kannada", "Tamil", "Malayalam",
                "Marathi", "Gujarati", "Punjabi", "Bengali", "Odia", 
                "Chinese", "Japanese", "English", "Others"
            ])
        
        with col2:
            type_option = st.selectbox("📂 Type", ["Word", "Phrase", "Folk Song", "Story"])
            contributor = st.text_input("👤 Your Name", placeholder="Anonymous")
            example = st.text_area("✍️ Example Sentence or Description", 
                                 placeholder="e.g., చదువు మన జీవితాన్ని వెలుగులోకి తీసుకెళ్తుంది", 
                                 height=100)
        
        # Audio upload section
        st.markdown("### 🎤 Audio (Optional)")
        
        audio_option = st.radio("Audio Input Method:", ["Upload File", "Record Audio", "No Audio"])
        
        audio_file = None
        if audio_option == "Upload File":
            audio_file = st.file_uploader("🔈 Upload Audio File", type=["mp3", "wav", "m4a", "ogg"])
        elif audio_option == "Record Audio":
            st.info("🎙️ Audio recording feature coming soon!")
        
        # AI Enhancement option
        ai_enhance = st.checkbox("🤖 Use AI to enhance meaning and context", value=False)
        
        submitted = st.form_submit_button("🚀 Submit Entry", type="primary")
        
        if submitted:
            if word and meaning and language and type_option:
                # Process the submission
                process_submission(word, meaning, language, type_option, example, 
                                 contributor, audio_file, ai_enhance)
            else:
                st.warning("⚠️ Please fill in all required fields (Word, Meaning, Language, Type)")

def process_submission(word, meaning, language, type_option, example, contributor, audio_file, ai_enhance):
    """Process the form submission"""
    
    with st.spinner("Processing your contribution..."):
        try:
            # Initialize variables
            audio_path = ""
            transcript = ""
            enhanced_meaning = meaning
            
            # Handle audio processing
            if audio_file:
                audio_path, transcript = process_audio(audio_file, word, type_option, language)
            
            # AI enhancement if requested (using Puter.js)
            if ai_enhance:
                try:
                    from modules.PuterTranslate import enhance_meaning, generate_example_sentences, analyze_cultural_significance
                    
                    # Enhance meaning
                    enhanced = enhance_meaning(word, meaning, language)
                    enhanced_meaning = enhanced.get('enhanced_meaning', meaning)
                    
                    st.success("🤖 AI enhancement applied!")
                    st.markdown(f"**Enhanced Meaning:** {enhanced_meaning}")
                    
                    if enhanced.get('related_words'):
                        st.markdown(f"**Related Words:** {', '.join(enhanced['related_words'])}")
                    
                    if enhanced.get('cultural_context'):
                        st.markdown(f"**Cultural Context:** {enhanced['cultural_context']}")
                    
                    # Generate additional example sentences
                    if not example:
                        example_sentences = generate_example_sentences(word, meaning, language)
                        if example_sentences:
                            st.markdown("**🤖 AI-Generated Examples:**")
                            for i, sentence in enumerate(example_sentences[:2], 1):
                                st.markdown(f"{i}. {sentence}")
                    
                    # Cultural analysis
                    cultural_analysis = analyze_cultural_significance(word, meaning, language)
                    if cultural_analysis.get('cultural_significance'):
                        with st.expander("🏛️ Cultural Analysis"):
                            st.markdown(f"**Cultural Significance:** {cultural_analysis['cultural_significance']}")
                            if cultural_analysis.get('historical_context'):
                                st.markdown(f"**Historical Context:** {cultural_analysis['historical_context']}")
                            if cultural_analysis.get('regional_variations'):
                                st.markdown(f"**Regional Variations:** {', '.join(cultural_analysis['regional_variations'])}")
                
                except Exception as e:
                    st.warning(f"AI enhancement failed: {e}")
                    enhanced_meaning = meaning
            
            # Create entry dictionary
            entry = {
                'word': word,
                'meaning': enhanced_meaning,
                'example': example or "",
                'language': language,
                'type': type_option,
                'audio_file': audio_path,
                'transcript': transcript,
                'contributor': contributor or "Anonymous"
            }
            
            # Save to database with automatic translation
            with st.spinner("🔄 Saving and translating your contribution..."):
                success = db.add_entry(entry)
                
                if success:
                    # Load the saved entry to get translations
                    saved_df = db.load_data()
                    saved_entry = saved_df[saved_df['word'] == word].iloc[-1]
                    
                    st.success("✅ Thank you for contributing! Your entry has been submitted and translated.")
                    
                    # Show translation results
                    st.markdown("### 🌐 Translation Results")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Original:**")
                        st.info(f"**Word:** {saved_entry['word']}")
                        st.info(f"**Meaning:** {saved_entry['meaning']}")
                        if saved_entry.get('example'):
                            st.info(f"**Example:** {saved_entry['example']}")
                    
                    with col2:
                        st.markdown("**Translated to English:**")
                        st.success(f"**Word:** {saved_entry.get('translated_word', 'N/A')}")
                        st.success(f"**Meaning:** {saved_entry.get('translated_meaning', 'N/A')}")
                        if saved_entry.get('translated_example'):
                            st.success(f"**Example:** {saved_entry['translated_example']}")
                    
                    # Show submission summary
                    show_submission_summary(entry, audio_path, transcript)
                    
                    # Clear form (optional)
                    st.rerun()
                else:
                    st.error("❌ Failed to save entry. Please try again.")
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

def process_audio(audio_file, word, type_option, language):
    """Process uploaded audio file"""
    
    try:
        # Generate unique filename
        file_extension = audio_file.name.split('.')[-1]
        filename = f"{word}_{type_option}_{uuid.uuid4().hex[:8]}.{file_extension}"
        
        # Save audio file
        audio_path = db.save_audio_file(audio_file.read(), filename)
        
        # Transcribe audio using Puter.js
        transcript = ""
        try:
            from modules.PuterTranslate import transcribe_audio
            transcript = transcribe_audio(audio_path, language)
            if transcript:
                st.success("🎤 Audio transcribed using Puter.js!")
        except Exception as e:
            st.warning(f"Puter.js transcription failed, using fallback: {e}")
            transcript = db.transcribe_audio(audio_path)
        
        return audio_path, transcript
        
    except Exception as e:
        st.warning(f"⚠️ Audio processing failed: {e}")
        return "", ""

def show_submission_summary(entry, audio_path, transcript):
    """Show summary of submitted entry"""
    
    st.markdown("### 📄 Submission Summary")
    
    # Create summary card
    summary_html = f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 20px; border-radius: 15px; margin: 20px 0;">
        <h3 style="margin-top: 0;">🎉 Entry Submitted Successfully!</h3>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
            <p><strong>📂 Type:</strong> {entry['type']}</p>
            <p><strong>🔤 Word/Title:</strong> {entry['word']}</p>
            <p><strong>📘 Meaning:</strong> {entry['meaning']}</p>
            <p><strong>🌐 Language:</strong> {entry['language']}</p>
            <p><strong>👤 Contributor:</strong> {entry['contributor']}</p>
            {f'<p><strong>✍️ Example:</strong> {entry["example"]}</p>' if entry['example'] else ''}
            {f'<p><strong>🔈 Audio:</strong> ✅ Uploaded</p>' if audio_path else ''}
            {f'<p><strong>📝 Transcript:</strong> {transcript}</p>' if transcript else ''}
        </div>
    </div>
    """
    
    st.markdown(summary_html, unsafe_allow_html=True)
    
    # Show audio player if available
    if audio_path and os.path.exists(audio_path):
        st.markdown("### 🎵 Audio Preview")
        st.audio(audio_path, format='audio/wav')
    
    # Show transcript if available
    if transcript:
        with st.expander("📝 View Transcript"):
            st.write(transcript)
    
    # Next steps
    st.markdown("### 🎯 What's Next?")
    st.markdown("""
    - Your entry will be reviewed by our community
    - Once verified, it will appear in the dictionary
    - You can track the status in the Analytics section
    - Consider contributing more words to help preserve linguistic diversity!
    """)
    
    # Quick actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📚 View Dictionary"):
            st.switch_page("pages/Dictionary.py")
    with col2:
        if st.button("📊 View Analytics"):
            st.switch_page("pages/Analytics.py")
    with col3:
        if st.button("➕ Add Another Entry"):
            st.rerun()
