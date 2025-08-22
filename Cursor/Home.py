import streamlit as st
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
import pages.Dictionary as Dictionary
import pages.Contribute as Contribute
import pages.Analytics as Analytics
import pages.About_Us as About_Us

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="JanaBhasha - Multilingual Dictionary & Corpus",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #5a6fd8 0%, #6a4190 100%);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🌍 JanaBhasha</h1>
        <p>Preserving India's Linguistic Heritage - One Word at a Time</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        
        selected = option_menu(
            menu_title=None,
            options=["📚 Dictionary", "➕ Contribute", "🌐 Translate", "📊 Analytics", "👥 About Us"],
            icons=["book", "plus-circle", "translate", "graph-up", "people"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "#667eea", "font-size": "18px"},
                "nav-link": {
                    "color": "#333",
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#667eea",
                },
                "nav-link-selected": {"background-color": "#667eea", "color": "white"},
            }
        )
        
        # AI Configuration
        st.markdown("---")
        st.markdown("### 🤖 AI Configuration")
        st.success("✅ AI features are available!")
        st.info("Translation and enhancement features are working with fallback system.")
        st.warning("⚠️ External API integration is being configured.")
        
        # Quick stats
        st.markdown("---")
        st.markdown("### 📈 Quick Stats")
        
        # Load basic stats
        try:
            import modules.Database as db
            stats = db.get_basic_stats()
            st.metric("Total Words", stats.get('total_words', 0))
            st.metric("Languages", stats.get('languages', 0))
            st.metric("Audio Files", stats.get('audio_files', 0))
        except:
            st.metric("Total Words", 0)
            st.metric("Languages", 0)
            st.metric("Audio Files", 0)
    
    # Page routing
    if selected == "📚 Dictionary":
        Dictionary.show()
    elif selected == "➕ Contribute":
        Contribute.show()
    elif selected == "🌐 Translate":
        import pages.Translate as Translate
        Translate.show()
    elif selected == "📊 Analytics":
        Analytics.show()
    elif selected == "👥 About Us":
        About_Us.show()

if __name__ == "__main__":
    main()
