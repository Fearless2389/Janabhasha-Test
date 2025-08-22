# 🌍 JanaBhasha - Multilingual Dictionary & Corpus

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6B6B?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/)

> **Preserving India's Linguistic Heritage - One Word at a Time**

JanaBhasha is a community-powered, AI-driven multilingual dictionary that aims to preserve and promote India's rich linguistic diversity. Built during the **VISWAM Summer of AI** program, it combines the power of AI with open-source collaboration to create a comprehensive repository of words, phrases, folk songs, and stories from various Indian languages.

## 🚀 Features

### 📚 **Dictionary Features**
- **Multilingual Search**: Search across multiple Indian languages
- **Dual View Modes**: Table view and card view for different browsing preferences
- **Advanced Filtering**: Filter by language, type, and search terms
- **Audio Integration**: Listen to pronunciations and folk songs
- **AI Enhancement**: Get enhanced meanings and cultural context with OpenAI
- **Cultural Analysis**: Deep insights into word significance and history
- **Related Words**: AI-powered suggestions for synonyms and related terms

### ➕ **Contribution System**
- **Easy Submission**: Simple forms for adding words, phrases, and stories
- **Audio Upload**: Support for audio files with automatic transcription
- **AI Enhancement**: Optional AI-powered meaning enhancement
- **Community Verification**: Crowdsourced content validation
- **Smart Suggestions**: AI-generated example sentences and cultural context
- **Batch Processing**: Upload CSV files for bulk translation and enhancement

### 📊 **Analytics Dashboard**
- **Real-time Statistics**: Track growth and community engagement
- **Language Distribution**: Visualize contributions by language
- **Growth Trends**: Monitor project progress over time
- **Contributor Insights**: Recognize top contributors

### 🎤 **Audio Features**
- **OpenAI Whisper**: High-quality audio transcription with language detection
- **Audio Playback**: Listen to pronunciations and folk songs
- **Transcript Display**: View transcribed content with expandable sections
- **Fallback Support**: Local Whisper model for offline transcription

## 🛠️ Technology Stack

### **Frontend & Backend**
- **Streamlit**: Python-based web framework for rapid development
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive charts and visualizations

### **AI & Machine Learning**
- **Puter.js**: Free access to OpenAI models via Puter.js
- **OpenAI GPT-3.5**: Advanced text translation and enhancement
- **OpenAI Whisper**: High-quality audio transcription
- **Cultural Analysis**: AI-powered cultural context and related word suggestions
- **Local Whisper**: Fallback audio transcription (offline support)

### **Data & Storage**
- **CSV Files**: Simple, portable database format
- **Local File System**: Audio file storage and management
- **JSON**: Configuration and metadata storage

### **Deployment**
- **Hugging Face Spaces**: Free hosting and deployment
- **GitHub**: Version control and collaboration
- **Streamlit Cloud**: Alternative deployment option

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/janabhasha/janabhasha.git
   cd janabhasha
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run Home.py
   ```

### Docker Setup (Optional)

```bash
# Build the Docker image
docker build -t janabhasha .

# Run the container
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key janabhasha
```

## 🚀 Quick Start

1. **Open the application** in your browser at `http://localhost:8501`

2. **AI Features Ready** (no API key required!)
   - Using Puter.js for free OpenAI access
   - All AI features like translation, enhancement, and cultural analysis are available

3. **Start contributing**
   - Navigate to the "Contribute" page
   - Add words, phrases, or stories in your language
   - Upload audio files for pronunciation
   - Use AI enhancement for better meanings and context

4. **Use the Translation Hub**
   - Navigate to the "Translate" page
   - Translate text between languages
   - Enhance words with cultural context
   - Process batch translations from CSV files

5. **Explore the dictionary**
   - Use the search and filter features
   - Switch between table and card views
   - Listen to audio pronunciations
   - Get AI-powered insights for any word

## 📁 Project Structure

```
JanaBhasha/
├── Home.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── pages/                 # Application pages
│   ├── Dictionary.py      # Dictionary browsing interface
│   ├── Contribute.py      # Contribution form
│   ├── Translate.py       # Translation hub with OpenAI integration
│   ├── Analytics.py       # Analytics dashboard
│   └── About_Us.py        # Team and project information
├── modules/               # Core functionality modules
│   ├── Database.py        # Data management and CSV operations
│   └── Translate.py       # OpenAI translation and enhancement utilities
└── data/                  # Data storage
    ├── Dictionary.csv     # Main dictionary database
    └── Audio_Transcripts/ # Audio files and transcripts
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### **Adding Content**
1. Use the web interface to add words, phrases, or stories
2. Provide accurate translations and examples
3. Upload audio files for better pronunciation

### **Code Contributions**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### **Reporting Issues**
- Use the GitHub issue tracker
- Provide detailed descriptions and steps to reproduce

### **Feature Requests**
- Open a GitHub issue with the "enhancement" label
- Describe the feature and its benefits

## 🌍 Supported Languages

Currently supporting:
- **Hindi** (हिंदी)
- **Telugu** (తెలుగు)
- **Kannada** (ಕನ್ನಡ)
- **Tamil** (தமிழ்)
- **Malayalam** (മലയാളം)
- **Marathi** (मराठी)
- **Gujarati** (ગુજરાતી)
- **Punjabi** (ਪੰਜਾਬੀ)
- **Bengali** (বাংলা)
- **Odia** (ଓଡ଼ିଆ)
- **English**
- **Chinese** (中文)
- **Japanese** (日本語)
- **Others** (More languages welcome!)

## 📊 Project Statistics

- **Total Entries**: Growing daily
- **Languages**: 14+ supported
- **Contributors**: Community-driven
- **Audio Files**: Pronunciation support
- **AI Enhancements**: OpenAI integration

## 🎯 Roadmap

### **Phase 1 (Current)**
- ✅ Basic dictionary functionality
- ✅ Audio upload and transcription
- ✅ AI enhancement features
- ✅ Analytics dashboard

### **Phase 2 (Next)**
- 🔄 Voice-based search
- 🔄 User authentication
- 🔄 Contributor profiles
- 🔄 Language leaderboards

### **Phase 3 (Future)**
- 📱 Mobile app development
- 🤖 Advanced AI features
- 🌐 API for developers
- 🏆 Gamification elements

## 🙏 Acknowledgments

- **SWECHA** for the VISWAM Summer of AI program
- **OpenAI** for providing powerful AI models
- **Streamlit** for the amazing web framework
- **Hugging Face** for hosting our application
- **All contributors** who make this project possible

## 📞 Contact & Support

- **Email**: team@janabhasha.org
- **GitHub**: [github.com/janabhasha](https://github.com/janabhasha)
- **Discord**: [Join our community](https://discord.gg/janabhasha)
- **Twitter**: [@JanaBhasha](https://twitter.com/JanaBhasha)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=janabhasha/janabhasha&type=Date)](https://star-history.com/#janabhasha/janabhasha&Date)

---

**Made with ❤️ by the JanaBhasha Team**

*Preserving linguistic heritage, one word at a time.*
