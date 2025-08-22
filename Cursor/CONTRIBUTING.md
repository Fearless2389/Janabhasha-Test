# 🤝 Contributing to JanaBhasha

Thank you for your interest in contributing to JanaBhasha! We're excited to have you join our mission to preserve India's linguistic heritage.

## 🌟 How to Contribute

### 1. **Adding Content (No Code Required!)**

The easiest way to contribute is by adding words, phrases, or stories to our dictionary:

1. **Visit our live application** at [janabhasha.org](https://janabhasha.org)
2. **Navigate to the "Contribute" page**
3. **Fill out the form** with:
   - Word/phrase in native script
   - Meaning in English
   - Example sentence
   - Language selection
   - Optional audio file
4. **Submit your contribution**

### 2. **Code Contributions**

If you're a developer, here's how to contribute code:

#### **Prerequisites**
- Python 3.8+
- Git
- Basic knowledge of Streamlit/Python

#### **Setup Development Environment**

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/janabhasha.git
   cd janabhasha
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Test your changes locally

5. **Test your changes**
   ```bash
   streamlit run Home.py
   ```

6. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill out the PR template

### 3. **Reporting Issues**

Found a bug? Here's how to report it:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear title describing the problem
   - Detailed description of the issue
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Browser/OS information

### 4. **Feature Requests**

Have an idea for a new feature?

1. **Check the roadmap** to see if it's already planned
2. **Create a feature request issue** with:
   - Clear description of the feature
   - Use cases and benefits
   - Mockups or examples (if applicable)
   - Priority level

## 📋 Development Guidelines

### **Code Style**
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused

### **Commit Messages**
Use conventional commit format:
```
type(scope): description

feat: add new audio transcription feature
fix: resolve search filter issue
docs: update README with new features
style: format code according to PEP 8
refactor: simplify database operations
test: add unit tests for search functionality
```

### **Testing**
- Test your changes locally before submitting
- Add unit tests for new functionality
- Ensure the app runs without errors
- Test with different data scenarios

### **Documentation**
- Update README.md if adding new features
- Add comments for complex logic
- Update docstrings for new functions
- Include usage examples

## 🎯 Areas That Need Help

### **High Priority**
- [ ] Voice-based search functionality
- [ ] User authentication system
- [ ] Mobile-responsive design improvements
- [ ] Performance optimization for large datasets

### **Medium Priority**
- [ ] Advanced filtering options
- [ ] Export functionality (PDF, CSV)
- [ ] Social sharing features
- [ ] Multi-language UI support

### **Low Priority**
- [ ] Dark mode theme
- [ ] Keyboard shortcuts
- [ ] Advanced analytics features
- [ ] API development

## 🌍 Language Contributions

We especially welcome contributions for:

### **Endangered Languages**
- Tribal and indigenous languages
- Regional dialects
- Lesser-known scripts

### **Content Types**
- Folk songs and stories
- Proverbs and idioms
- Cultural expressions
- Traditional knowledge

### **Audio Content**
- Pronunciation guides
- Folk song recordings
- Story narrations
- Cultural performances

## 🏆 Recognition

Contributors will be recognized in several ways:

1. **Contributor Hall of Fame** on our website
2. **GitHub Contributors** page
3. **Special mentions** in release notes
4. **Community badges** for different contribution types

## 📞 Getting Help

Need help with contributing?

- **Discord**: Join our [community server](https://discord.gg/janabhasha)
- **GitHub Discussions**: Use the [Discussions tab](https://github.com/janabhasha/janabhasha/discussions)
- **Email**: Contact us at team@janabhasha.org

## 🎉 First Time Contributors

New to open source? Here are some easy ways to start:

1. **Fix a typo** in documentation
2. **Add a new language** to the supported languages list
3. **Improve error messages**
4. **Add sample data** for testing
5. **Update documentation**

## 📄 Code of Conduct

We're committed to providing a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## 🚀 Quick Start for Developers

```bash
# Clone and setup
git clone https://github.com/janabhasha/janabhasha.git
cd janabhasha
pip install -r requirements.txt

# Run locally
streamlit run Home.py

# Make changes and test
# Create PR when ready
```

---

**Thank you for contributing to JanaBhasha! Together, we can preserve India's linguistic heritage for future generations.** 🌍
