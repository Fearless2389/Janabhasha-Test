import streamlit as st
import pandas as pd
import plotly.express as px
import modules.Database as db
import os

def show():
    st.markdown("## 📚 Multilingual Dictionary")
    st.markdown("Explore words, phrases, folk songs, and stories from various Indian languages.")
    
    # Search and filter section
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        search_query = st.text_input("🔍 Search words, meanings, or examples", placeholder="Enter search term...")
    
    with col2:
        languages = [""] + db.get_languages()
        selected_language = st.selectbox("🌍 Language", languages)
    
    with col3:
        entry_types = [""] + db.get_entry_types()
        selected_type = st.selectbox("📝 Type", entry_types)
    
    with col4:
        view_mode = st.selectbox("👁️ View", ["Table", "Cards"])
    
    # Search functionality
    df = db.search_entries(search_query, selected_language, selected_type)
    
    if df.empty:
        st.info("No entries found. Try adjusting your search criteria or contribute new content!")
        return
    
    # Display results count
    st.markdown(f"**Found {len(df)} entries**")
    
    if view_mode == "Table":
        show_table_view(df)
    else:
        show_card_view(df)

def show_table_view(df):
    """Display data in an interactive table format"""
    
    # Display the dataframe with Streamlit's built-in dataframe
    st.dataframe(
        df,
        use_container_width=True,
        height=600,
        column_config={
            "id": st.column_config.NumberColumn("ID", width="small"),
            "word": st.column_config.TextColumn("Word/Title", width="medium"),
            "meaning": st.column_config.TextColumn("Meaning", width="large"),
            "example": st.column_config.TextColumn("Example", width="large"),
            "language": st.column_config.TextColumn("Language", width="small"),
            "type": st.column_config.TextColumn("Type", width="small"),
            "contributor": st.column_config.TextColumn("Contributor", width="medium"),
            "verified": st.column_config.CheckboxColumn("Verified", width="small")
        }
    )
    
    # Add row selection functionality
    st.markdown("### 📖 Entry Details")
    selected_index = st.selectbox(
        "Select an entry to view details:",
        options=range(len(df)),
        format_func=lambda x: f"{df.iloc[x]['word']} ({df.iloc[x]['language']})"
    )
    
    if selected_index is not None:
        selected_row = df.iloc[selected_index]
        show_entry_details(selected_row)

def show_card_view(df):
    """Display data in card format"""
    
    # Pagination
    items_per_page = 20
    total_pages = (len(df) + items_per_page - 1) // items_per_page
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        current_page = st.selectbox("Page", range(1, total_pages + 1), index=0)
    
    # Calculate start and end indices
    start_idx = (current_page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, len(df))
    
    # Display cards for current page
    for idx in range(start_idx, end_idx):
        row = df.iloc[idx]
        show_entry_card(row)

def show_entry_card(entry):
    """Display a single entry as a card"""
    
    # Card styling
    st.markdown("""
    <style>
    .entry-card {
        background: white;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .entry-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .entry-word {
        font-size: 1.5em;
        font-weight: bold;
        color: #667eea;
    }
    .entry-badge {
        background: #667eea;
        color: white;
        padding: 4px 8px;
        border-radius: 15px;
        font-size: 0.8em;
    }
    .entry-meaning {
        font-size: 1.1em;
        margin: 10px 0;
        color: #333;
    }
    .entry-example {
        font-style: italic;
        color: #666;
        margin: 10px 0;
        padding: 10px;
        background: #f8f9fa;
        border-radius: 5px;
    }
    .entry-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 15px;
        font-size: 0.9em;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create card content
    card_html = f"""
    <div class="entry-card">
        <div class="entry-header">
            <span class="entry-word">{entry['word']}</span>
            <span class="entry-badge">{entry['type']}</span>
        </div>
        <div class="entry-meaning"><strong>Meaning:</strong> {entry['meaning']}</div>
    """
    
    # Add translation if available
    if pd.notna(entry.get('translated_word')) and entry.get('translated_word'):
        card_html += f"""
        <div style="background: #e8f5e8; padding: 10px; border-radius: 5px; margin: 10px 0;">
            <strong>🌐 English:</strong> {entry['translated_word']} - {entry.get('translated_meaning', '')}
        </div>
        """
    
    if pd.notna(entry['example']) and entry['example']:
        card_html += f'<div class="entry-example"><strong>Example:</strong> {entry["example"]}</div>'
    
    # Add audio player if available
    if pd.notna(entry['audio_file']) and entry['audio_file']:
        audio_path = os.path.join("data", "Audio_Transcripts", entry['audio_file'])
        if os.path.exists(audio_path):
            st.audio(audio_path, format='audio/wav')
    
    # Add transcript if available
    if pd.notna(entry['transcript']) and entry['transcript']:
        with st.expander("📝 View Transcript"):
            st.write(entry['transcript'])
    
    card_html += f"""
        <div class="entry-footer">
            <span>🌍 {entry['language']}</span>
            <span>👤 {entry['contributor']}</span>
            <span>{'✅ Verified' if entry['verified'] else '⏳ Pending'}</span>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)

def show_entry_details(entry):
    """Show detailed view of selected entry"""
    
    st.markdown("---")
    st.markdown("### 📖 Entry Details")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 🌍 Original Content")
        st.markdown(f"**Word/Title:** {entry['word']}")
        st.markdown(f"**Meaning:** {entry['meaning']}")
        
        if entry['example']:
            st.markdown(f"**Example:** {entry['example']}")
        
        if entry['transcript']:
            st.markdown(f"**Transcript:** {entry['transcript']}")
        
        # Show translations if available
        if entry.get('translated_word') or entry.get('translated_meaning'):
            st.markdown("#### 🌐 English Translation")
            if entry.get('translated_word'):
                st.markdown(f"**Word/Title:** {entry['translated_word']}")
            if entry.get('translated_meaning'):
                st.markdown(f"**Meaning:** {entry['translated_meaning']}")
            if entry.get('translated_example'):
                st.markdown(f"**Example:** {entry['translated_example']}")
            if entry.get('translated_transcript'):
                st.markdown(f"**Transcript:** {entry['translated_transcript']}")
    
    with col2:
        st.markdown(f"**Language:** {entry['language']}")
        st.markdown(f"**Type:** {entry['type']}")
        st.markdown(f"**Contributor:** {entry['contributor']}")
        st.markdown(f"**Status:** {'✅ Verified' if entry['verified'] else '⏳ Pending'}")
        
        # Audio player
        if entry['audio_file']:
            audio_path = os.path.join("data", "Audio_Transcripts", entry['audio_file'])
            if os.path.exists(audio_path):
                st.audio(audio_path, format='audio/wav')
    
    # AI enhancement using Puter.js
    if st.button("🤖 Enhance with AI"):
        with st.spinner("Enhancing with AI..."):
            try:
                from modules.PuterTranslate import enhance_meaning, suggest_related_words, analyze_cultural_significance
                
                # Enhanced meaning
                enhanced = enhance_meaning(entry['word'], entry['meaning'], entry['language'])
                
                if enhanced['enhanced_meaning'] != entry['meaning']:
                    st.markdown("### 🤖 AI Enhancement")
                    st.markdown(f"**Enhanced Meaning:** {enhanced['enhanced_meaning']}")
                    
                    if enhanced['related_words']:
                        st.markdown(f"**Related Words:** {', '.join(enhanced['related_words'])}")
                    
                    if enhanced['cultural_context']:
                        st.markdown(f"**Cultural Context:** {enhanced['cultural_context']}")
                
                # Additional AI features
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("🔍 Get More Related Words"):
                        related_words = suggest_related_words(entry['word'], entry['language'])
                        if related_words:
                            st.markdown("**🔍 Related Words:**")
                            for word in related_words:
                                st.markdown(f"- {word}")
                
                with col2:
                    if st.button("🏛️ Cultural Analysis"):
                        cultural = analyze_cultural_significance(entry['word'], entry['meaning'], entry['language'])
                        if cultural.get('cultural_significance'):
                            st.markdown("**🏛️ Cultural Analysis:**")
                            st.markdown(f"**Significance:** {cultural['cultural_significance']}")
                            if cultural.get('historical_context'):
                                st.markdown(f"**History:** {cultural['historical_context']}")
            
            except Exception as e:
                st.error(f"AI enhancement failed: {e}")

def show_language_stats(df):
    """Show language distribution chart"""
    if not df.empty:
        lang_counts = df['language'].value_counts()
        
        fig = px.pie(
            values=lang_counts.values,
            names=lang_counts.index,
            title="Language Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        st.plotly_chart(fig, use_container_width=True)
