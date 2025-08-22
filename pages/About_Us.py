import streamlit as st

def show():
    st.markdown("## 👥 About JanaBhasha")
    
    st.markdown("""
    JanaBhasha is a community-powered, AI-driven multilingual dictionary built during the **VISWAM Summer of AI** program.
    Our mission is to protect and promote India's rich linguistic heritage by combining AI and open-source collaboration.
    """)
    
    st.markdown("---")
    
    # Team Member Cards
    st.markdown("### 👩‍💻 Meet the Team")
    
    team = [
        {
            "name": "Karthik",
            "role": "UI/UX & Frontend Developer",
            "github": "https://github.com/karthik123",
            "image": "https://via.placeholder.com/150",
            "quote": "A well-crafted UI can make a dying language feel alive again."
        },
        {
            "name": "Chervith",
            "role": "NLP Engineer & Backend Integration",
            "github": "https://github.com/chervith",
            "image": "https://via.placeholder.com/150",
            "quote": "Language is the oldest dataset in the world. We're just learning how to use it."
        },
        {
            "name": "Pranav",
            "role": "Data Curation & Translation",
            "github": "https://github.com/pranav-ai",
            "image": "https://via.placeholder.com/150",
            "quote": "Each word we collect is a bridge to someone's world."
        },
        {
            "name": "Aryan",
            "role": "Whisper Integration & Audio Processing",
            "github": "https://github.com/aryan-code",
            "image": "https://via.placeholder.com/150",
            "quote": "When you hear your language spoken online, it's like coming home."
        },
        {
            "name": "Ruthvik",
            "role": "Deployment & Documentation",
            "github": "https://github.com/ruthvikreddy",
            "image": "https://via.placeholder.com/150",
            "quote": "Making something work is one thing. Making it reach people — that's the real job."
        },
    ]
    
    cols = st.columns(len(team))
    for col, member in zip(cols, team):
        with col:
            st.image(member["image"], use_container_width=True)
            st.markdown(f"**{member['name']}**")
            st.caption(member["role"])
            st.markdown(f"[🌐 GitHub]({member['github']})")
            st.markdown(f"> {member['quote']}")
    
    st.markdown("---")
    
    # Project Vision
    st.markdown("### 🧭 Our Vision")
    
    st.markdown("""
    India is home to **over 1,600 languages**, many of which are endangered or underrepresented online.
    With JanaBhasha, we aim to:
    - Build a community-contributed, AI-supported dictionary
    - Preserve cultural expressions through regional scripts
    - Empower speakers to be digital contributors, not just consumers
    """)
    
    st.markdown("---")
    
    # Future Features
    st.markdown("### 🚀 What's Next?")
    
    st.markdown("""
    - 🔍 Voice-based dictionary search  
    - 🧑‍💻 Contributor logins & public profiles  
    - 🏆 Language-wise leaderboards  
    - 🤖 Auto-validation with AI/LLMs  
    - 📱 PWA/mobile version of JanaBhasha  
    - 🗣️ Support for rare and tribal dialects  
    """)
    
    st.markdown("---")
    
    # Community Goals
    st.markdown("### 🌍 Community Goals")
    
    st.markdown("""
    JanaBhasha is made **by the people, for the people**. We envision a future where:
    - Every Indian language has a digital presence  
    - Students, elders, and activists can contribute equally  
    - Language learning becomes local, inclusive, and culturally rooted  
    """)
    
    st.markdown("---")
    
    # Technology Stack
    st.markdown("### 🛠️ Technology Stack")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Frontend & Backend:**")
        st.markdown("- Streamlit (Python-based UI)")
        st.markdown("- Pandas (Data manipulation)")
        st.markdown("- Plotly (Interactive charts)")
        
        st.markdown("**AI & ML:**")
        st.markdown("- OpenAI Whisper (Audio transcription)")
        st.markdown("- OpenAI GPT (Text enhancement)")
        st.markdown("- Transformers (NLP models)")
    
    with col2:
        st.markdown("**Data & Storage:**")
        st.markdown("- CSV files (Simple database)")
        st.markdown("- Local file system")
        st.markdown("- Audio file management")
        
        st.markdown("**Deployment:**")
        st.markdown("- Hugging Face Spaces")
        st.markdown("- GitHub integration")
        st.markdown("- Streamlit Cloud")
    
    st.markdown("---")
    
    # Acknowledgments
    st.markdown("### 🙏 Acknowledgments")
    
    st.markdown("""
    Special thanks to:
    - **SWECHA** for the VISWAM Summer of AI program
    - **OpenAI** for providing powerful AI models
    - **Streamlit** for the amazing web framework
    - **Hugging Face** for hosting our application
    - Every contributor who made this vision possible
    """)
    
    # Contact & Links
    st.markdown("---")
    st.markdown("### 📞 Get in Touch")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🌐 Project Links:**")
        st.markdown("- [GitHub Repository](https://github.com/janabhasha)")
        st.markdown("- [Live Demo](https://huggingface.co/spaces/janabhasha)")
        st.markdown("- [Documentation](https://docs.janabhasha.org)")
    
    with col2:
        st.markdown("**📧 Contact:**")
        st.markdown("- Email: team@janabhasha.org")
        st.markdown("- Discord: [Join our community](https://discord.gg/janabhasha)")
        st.markdown("- Twitter: [@JanaBhasha](https://twitter.com/JanaBhasha)")
    
    with col3:
        st.markdown("**🤝 Contribute:**")
        st.markdown("- [Add words](https://janabhasha.org/contribute)")
        st.markdown("- [Report issues](https://github.com/janabhasha/issues)")
        st.markdown("- [Join development](https://github.com/janabhasha)")
    
    # Call to action
    st.markdown("---")
    st.markdown("### 🚀 Ready to Contribute?")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Start Contributing", use_container_width=True):
            st.switch_page("pages/Contribute.py")
    with col2:
        if st.button("📚 Browse Dictionary", use_container_width=True):
            st.switch_page("pages/Dictionary.py")
    with col3:
        if st.button("📊 View Analytics", use_container_width=True):
            st.switch_page("pages/Analytics.py")
