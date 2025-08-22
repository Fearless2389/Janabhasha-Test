# 🚀 JanaBhasha Setup Guide

## Quick Start with OpenAI Integration

### 1. **Get Your OpenAI API Key**

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in to your account
3. Click "Create new secret key"
4. Copy your API key (it starts with `sk-`)

### 2. **Configure the Application**

#### Option A: Environment Variable (Recommended)
Create a `.env` file in your project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

#### Option B: In-App Configuration
1. Run the application: `streamlit run Home.py`
2. Open your browser to `http://localhost:8501`
3. In the sidebar, paste your OpenAI API key
4. Click "Save" to store it for the session

### 3. **Test the Features**

Once configured, you can:

#### 🌐 **Automatic Translation**
- Submit words in any Indian language
- Get instant English translations
- View both original and translated content

#### 🤖 **AI Enhancement**
- Get enhanced meanings with cultural context
- Receive related words and synonyms
- Access cultural significance analysis

#### 🎤 **Audio Transcription**
- Upload audio files in regional languages
- Get automatic transcription using OpenAI Whisper
- View both original and translated transcripts

## 🎯 How It Works

### **Automatic Translation Flow**
1. **Submit Content**: User enters word/song/story in regional language
2. **AI Translation**: OpenAI automatically translates to English
3. **Store Both**: Original and translated versions saved to CSV
4. **Real-time Updates**: Analytics reflect new translations immediately

### **Database Structure**
The CSV now includes these new columns:
- `translated_word`: English translation of the word
- `translated_meaning`: English translation of the meaning
- `translated_example`: English translation of the example
- `translated_transcript`: English translation of audio transcript

### **Analytics Features**
- **Translation Progress**: Track how many entries are translated
- **Language Breakdown**: See translation rates by language
- **Real-time Updates**: Refresh data to see latest contributions

## 🔧 Troubleshooting

### **API Key Issues**
- **Invalid Key**: Make sure your API key starts with `sk-`
- **Rate Limits**: OpenAI has usage limits, check your account
- **Network Issues**: Ensure stable internet connection

### **Translation Not Working**
- Check if API key is properly configured
- Verify the language is supported
- Try refreshing the page

### **Audio Transcription Issues**
- Ensure audio file is in supported format (MP3, WAV, etc.)
- Check file size (OpenAI has limits)
- Verify audio quality is clear

## 💡 Best Practices

### **For Contributors**
1. **Provide Clear Audio**: Speak clearly for better transcription
2. **Use Native Script**: Enter words in original script when possible
3. **Add Context**: Include examples and cultural notes
4. **Verify Translations**: Check AI translations for accuracy

### **For Developers**
1. **Monitor API Usage**: Track your OpenAI usage
2. **Backup Data**: Regularly backup your CSV file
3. **Test Features**: Try all features before deployment
4. **Update Regularly**: Keep dependencies updated

## 🌟 Advanced Features

### **Batch Translation**
- Upload CSV files with multiple words
- Get bulk translations
- Download results as CSV

### **Cultural Analysis**
- Get historical context for words
- Learn about regional variations
- Understand cultural significance

### **Related Words**
- Find synonyms and antonyms
- Discover semantically related terms
- Build vocabulary connections

## 📞 Support

If you encounter issues:
1. Check this setup guide
2. Review the README.md file
3. Check your OpenAI account status
4. Ensure all dependencies are installed

---

**Happy contributing to JanaBhasha! 🌍**
