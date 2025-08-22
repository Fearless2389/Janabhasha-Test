import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import modules.Database as db

def show():
    st.markdown("## 📊 JanaBhasha Analytics")
    st.markdown("Track the growth and impact of our multilingual dictionary.")
    
    # Real-time refresh button
    if st.button("🔄 Refresh Data", type="primary"):
        st.rerun()
    
    # Load data
    df = db.load_data()
    
    if df.empty:
        st.warning("⚠️ No data available yet. Start contributing to see analytics!")
        return
    
    # Basic stats
    stats = db.get_basic_stats()
    analytics_data = db.get_analytics_data()
    
    # Overview metrics
    st.markdown("### 📈 Overview Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Entries", stats['total_words'])
    with col2:
        st.metric("Languages", stats['languages'])
    with col3:
        st.metric("Audio Files", stats['audio_files'])
    with col4:
        st.metric("Contributors", stats['contributors'])
    
    # Translation metrics
    translated_count = len(df[df['translated_word'].notna() & (df['translated_word'] != '')])
    translation_rate = (translated_count / stats['total_words'] * 100) if stats['total_words'] > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Translated Entries", translated_count)
    with col2:
        st.metric("Translation Rate", f"{translation_rate:.1f}%")
    with col3:
        st.metric("Verified", stats['verified_entries'])
    with col4:
        verification_rate = (stats['verified_entries'] / stats['total_words'] * 100) if stats['total_words'] > 0 else 0
        st.metric("Verification Rate", f"{verification_rate:.1f}%")
    
    st.markdown("---")
    
    # Language distribution
    if analytics_data.get('language_distribution'):
        st.markdown("### 🌍 Language Distribution")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Pie chart
            lang_data = analytics_data['language_distribution']
            fig_pie = px.pie(
                values=list(lang_data.values()),
                names=list(lang_data.keys()),
                title="Contributions by Language",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_layout(height=400)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Language stats table with translation status
            lang_stats = []
            for lang, count in lang_data.items():
                lang_df = df[df['language'] == lang]
                translated_count = len(lang_df[lang_df['translated_word'].notna() & (lang_df['translated_word'] != '')])
                translation_rate = (translated_count / count * 100) if count > 0 else 0
                lang_stats.append({
                    "Language": lang,
                    "Total": count,
                    "Translated": translated_count,
                    "Translation Rate": f"{translation_rate:.1f}%"
                })
            
            lang_df = pd.DataFrame(lang_stats).sort_values("Total", ascending=False)
            st.markdown("**Language Statistics:**")
            st.dataframe(lang_df, use_container_width=True)
    
    # Entry type distribution
    if analytics_data.get('type_distribution'):
        st.markdown("### 📝 Entry Type Distribution")
        
        type_data = analytics_data['type_distribution']
        fig_bar = px.bar(
            x=list(type_data.keys()),
            y=list(type_data.values()),
            title="Contributions by Type",
            color=list(type_data.values()),
            color_continuous_scale="viridis"
        )
        fig_bar.update_layout(height=400)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Recent activity
    st.markdown("### 🕒 Recent Activity")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Recent Activity (30 days)", analytics_data.get('recent_activity', 0))
        
        # Recent entries table
        recent_df = df.copy()
        recent_df['timestamp'] = pd.to_datetime(recent_df['timestamp'])
        recent_entries = recent_df[recent_df['timestamp'] >= (datetime.now() - timedelta(days=30))]
        
        if not recent_entries.empty:
            st.markdown("**Recent Entries:**")
            recent_display = recent_entries[['word', 'language', 'type', 'contributor']].head(10)
            st.dataframe(recent_display, use_container_width=True)
    
    with col2:
        # Top contributors
        if analytics_data.get('top_contributors'):
            st.markdown("**Top Contributors:**")
            top_contrib_df = pd.DataFrame([
                {"Contributor": contributor, "Entries": count}
                for contributor, count in analytics_data['top_contributors'].items()
            ])
            st.dataframe(top_contrib_df, use_container_width=True)
    
    # Translation and Verification Status
    st.markdown("### 🌐 Translation & Verification Status")
    
    verified_count = stats['verified_entries']
    total_count = stats['total_words']
    pending_count = total_count - verified_count
    translated_count = len(df[df['translated_word'].notna() & (df['translated_word'] != '')])
    untranslated_count = total_count - translated_count
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Translated", translated_count)
    with col2:
        st.metric("Untranslated", untranslated_count)
    with col3:
        st.metric("Verified", verified_count)
    with col4:
        st.metric("Pending", pending_count)
    
    # Progress bars
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Translation Progress:**")
        if total_count > 0:
            translation_progress = translated_count / total_count
            st.progress(translation_progress)
            st.caption(f"{translated_count} out of {total_count} entries translated")
    
    with col2:
        st.markdown("**Verification Progress:**")
        if total_count > 0:
            verification_progress = verified_count / total_count
            st.progress(verification_progress)
            st.caption(f"{verified_count} out of {total_count} entries verified")
    
    # Audio content analysis
    if stats['audio_files'] > 0:
        st.markdown("### 🎤 Audio Content Analysis")
        
        audio_df = df[df['audio_file'].notna() & (df['audio_file'] != '')]
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Audio by language
            audio_by_lang = audio_df['language'].value_counts()
            fig_audio = px.bar(
                x=audio_by_lang.index,
                y=audio_by_lang.values,
                title="Audio Files by Language"
            )
            st.plotly_chart(fig_audio, use_container_width=True)
        
        with col2:
            # Audio by type
            audio_by_type = audio_df['type'].value_counts()
            fig_audio_type = px.pie(
                values=audio_by_type.values,
                names=audio_by_type.index,
                title="Audio Files by Type"
            )
            st.plotly_chart(fig_audio_type, use_container_width=True)
    
    # Growth trends (if we have timestamp data)
    st.markdown("### 📈 Growth Trends")
    
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date
        
        # Daily contributions
        daily_contributions = df.groupby('date').size().reset_index(name='contributions')
        
        fig_trend = px.line(
            daily_contributions,
            x='date',
            y='contributions',
            title="Daily Contributions Over Time"
        )
        fig_trend.update_layout(height=400)
        st.plotly_chart(fig_trend, use_container_width=True)
    
    # Community insights
    st.markdown("### 🌟 Community Insights")
    
    insights = []
    
    if stats['total_words'] > 0:
        insights.append(f"📚 **{stats['total_words']}** words, phrases, and stories collected")
    
    if stats['languages'] > 0:
        insights.append(f"🌍 **{stats['languages']}** languages represented")
    
    if stats['contributors'] > 0:
        insights.append(f"👥 **{stats['contributors']}** contributors from the community")
    
    if stats['audio_files'] > 0:
        insights.append(f"🎤 **{stats['audio_files']}** audio recordings preserved")
    
    if analytics_data.get('recent_activity', 0) > 0:
        insights.append(f"📈 **{analytics_data['recent_activity']}** contributions in the last 30 days")
    
    for insight in insights:
        st.markdown(insight)
    
    # Call to action
    st.markdown("---")
    st.markdown("### 🚀 Help Us Grow!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Contribute Now", use_container_width=True):
            st.switch_page("pages/Contribute.py")
    with col2:
        if st.button("📚 Browse Dictionary", use_container_width=True):
            st.switch_page("pages/Dictionary.py")
    with col3:
        if st.button("👥 About Us", use_container_width=True):
            st.switch_page("pages/About_Us.py")
