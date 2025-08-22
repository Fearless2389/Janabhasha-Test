import streamlit as st
from modules.PuterTranslate import translate_text, enhance_meaning, generate_example_sentences

def show():
    st.markdown("## 🌐 JanaBhasha Translation Hub")
    st.markdown("Powered by OpenAI for high-quality, culturally-aware translations.")
    
    # Check Puter.js connection
    st.success("✅ Using Puter.js for free OpenAI access! Translation features are available.")
    
    # Main translation interface
    st.markdown("### 🔄 Text Translation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        source_text = st.text_area("📝 Enter text to translate", 
                                  placeholder="Enter text in any language...",
                                  height=150)
        
        source_lang = st.selectbox("🌍 From Language", [
            "Auto-detect", "Hindi", "Telugu", "Kannada", "Tamil", "Malayalam",
            "Marathi", "Gujarati", "Punjabi", "Bengali", "Odia", 
            "English", "Chinese", "Japanese", "Others"
        ])
    
    with col2:
        target_lang = st.selectbox("🎯 To Language", [
            "English", "Hindi", "Telugu", "Kannada", "Tamil", "Malayalam",
            "Marathi", "Gujarati", "Punjabi", "Bengali", "Odia", 
            "Chinese", "Japanese", "Others"
        ])
        
        if st.button("🔄 Translate", type="primary", use_container_width=True):
            if source_text.strip():
                with st.spinner("Translating..."):
                    try:
                        # Convert language names to codes for better translation
                        source_code = get_language_code(source_lang)
                        target_code = get_language_code(target_lang)
                        
                        translated_text = translate_text(source_text, source_code, target_code)
                        
                        st.markdown("### 📤 Translation Result")
                        st.markdown(f"**{source_lang} → {target_lang}:**")
                        st.success(translated_text)
                        
                        # Add to dictionary option
                        if st.button("➕ Add to JanaBhasha Dictionary"):
                            st.session_state.add_to_dict = {
                                'word': source_text,
                                'meaning': translated_text,
                                'source_lang': source_lang,
                                'target_lang': target_lang
                            }
                            st.rerun()
                            
                    except Exception as e:
                        st.error(f"Translation failed: {e}")
            else:
                st.warning("Please enter text to translate.")
    
    # Word enhancement section
    st.markdown("---")
    st.markdown("### 🤖 AI Word Enhancement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        word = st.text_input("🔤 Word", placeholder="Enter a word...")
        language = st.selectbox("🌍 Language", [
            "Hindi", "Telugu", "Kannada", "Tamil", "Malayalam",
            "Marathi", "Gujarati", "Punjabi", "Bengali", "Odia", 
            "English", "Chinese", "Japanese"
        ])
        meaning = st.text_input("📖 Current Meaning", placeholder="Enter current meaning...")
    
    with col2:
        if st.button("✨ Enhance Word", type="primary", use_container_width=True):
            if word and meaning:
                with st.spinner("Enhancing word..."):
                    try:
                        enhanced = enhance_meaning(word, meaning, language)
                        
                        st.markdown("### ✨ Enhanced Results")
                        
                        if enhanced.get('enhanced_meaning'):
                            st.markdown(f"**Enhanced Meaning:** {enhanced['enhanced_meaning']}")
                        
                        if enhanced.get('related_words'):
                            st.markdown(f"**Related Words:** {', '.join(enhanced['related_words'])}")
                        
                        if enhanced.get('cultural_context'):
                            st.markdown(f"**Cultural Context:** {enhanced['cultural_context']}")
                        
                        # Generate example sentences
                        examples = generate_example_sentences(word, meaning, language)
                        if examples:
                            st.markdown("**Example Sentences:**")
                            for i, example in enumerate(examples, 1):
                                st.markdown(f"{i}. {example}")
                                
                    except Exception as e:
                        st.error(f"Enhancement failed: {e}")
            else:
                st.warning("Please enter both word and meaning.")
    
    # Batch translation section
    st.markdown("---")
    st.markdown("### 📚 Batch Translation")
    
    uploaded_file = st.file_uploader("📁 Upload CSV file with words", type=['csv'])
    
    if uploaded_file:
        import pandas as pd
        
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ Loaded {len(df)} words from CSV")
            
            if st.button("🔄 Translate All", type="primary"):
                if 'word' in df.columns and 'language' in df.columns:
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    translated_words = []
                    
                    for idx, row in df.iterrows():
                        status_text.text(f"Translating {row['word']}...")
                        
                        try:
                            translated = translate_text(
                                row['word'], 
                                get_language_code(row['language']), 
                                "English"
                            )
                            translated_words.append({
                                'original_word': row['word'],
                                'original_language': row['language'],
                                'translated_meaning': translated
                            })
                        except Exception as e:
                            st.warning(f"Failed to translate {row['word']}: {e}")
                        
                        progress_bar.progress((idx + 1) / len(df))
                    
                    # Show results
                    if translated_words:
                        st.markdown("### 📊 Translation Results")
                        results_df = pd.DataFrame(translated_words)
                        st.dataframe(results_df, use_container_width=True)
                        
                        # Download option
                        csv = results_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results",
                            data=csv,
                            file_name="translated_words.csv",
                            mime="text/csv"
                        )
                else:
                    st.error("CSV must contain 'word' and 'language' columns")
                    
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
    
    # Add to dictionary modal
    if hasattr(st.session_state, 'add_to_dict'):
        st.markdown("---")
        st.markdown("### ➕ Add to Dictionary")
        
        data = st.session_state.add_to_dict
        
        with st.form("add_to_dict_form"):
            st.markdown(f"**Word:** {data['word']}")
            st.markdown(f"**Meaning:** {data['meaning']}")
            st.markdown(f"**Language:** {data['source_lang']}")
            
            contributor = st.text_input("👤 Your Name", placeholder="Anonymous")
            example = st.text_area("💬 Example Usage", placeholder="Optional example sentence...")
            
            if st.form_submit_button("✅ Add to Dictionary"):
                try:
                    from modules.Database import add_entry
                    
                    entry = {
                        'word': data['word'],
                        'meaning': data['meaning'],
                        'language': data['source_lang'],
                        'type': 'Word',
                        'example': example,
                        'contributor': contributor or 'Anonymous',
                        'audio_file': '',
                        'transcript': ''
                    }
                    
                    success = add_entry(entry)
                    if success:
                        st.success("✅ Word added to JanaBhasha dictionary!")
                        del st.session_state.add_to_dict
                        st.rerun()
                    else:
                        st.error("❌ Failed to add word to dictionary")
                        
                except Exception as e:
                    st.error(f"Error adding to dictionary: {e}")

def get_language_code(language_name):
    """Convert language name to language code for better translation"""
    language_map = {
        "Hindi": "hi",
        "Telugu": "te", 
        "Kannada": "kn",
        "Tamil": "ta",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Gujarati": "gu",
        "Punjabi": "pa",
        "Bengali": "bn",
        "Odia": "or",
        "English": "en",
        "Chinese": "zh",
        "Japanese": "ja",
        "Auto-detect": "auto"
    }
    return language_map.get(language_name, language_name.lower())
