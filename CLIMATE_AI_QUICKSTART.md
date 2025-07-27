# 🚀 Climate AI Assistant - Quick Start Guide

## 🌟 What's New?

Your CO₂ Emissions Estimator now includes an **AI-powered Climate Assistant** that can answer questions about climate change, sustainability, and environmental topics using live data from Google Search API!

## ⚡ Quick Setup (2 minutes)

### Option 1: Use Built-in Knowledge (No setup required)
1. Run the app: `streamlit run app/index.py`
2. Navigate to "🤖 Climate AI Assistant" 
3. Start asking climate questions immediately!

### Option 2: Enable Live Search (Enhanced experience)
1. Get Google API credentials (see [GOOGLE_API_SETUP.md](GOOGLE_API_SETUP.md))
2. Enter API key and Search Engine ID in the app
3. Enjoy real-time climate information!

## 🎯 What Can You Ask?

### ✅ Perfect Questions:
- "How can I reduce my carbon footprint?"
- "What are the latest climate change impacts?"
- "Tell me about renewable energy benefits"
- "How do electric vehicles help the environment?"
- "What is the Paris Climate Agreement?"
- "How does deforestation affect climate?"

### ❌ Questions Outside Scope:
- General weather queries
- Non-environmental topics
- Personal advice unrelated to climate

## 🔧 Features

| Feature | Built-in Mode | API Mode |
|---------|---------------|----------|
| Climate Q&A | ✅ | ✅ |
| Real-time data | ❌ | ✅ |
| Latest research | ❌ | ✅ |
| Current statistics | ❌ | ✅ |
| Offline usage | ✅ | ❌ |

## 🎨 Interface Overview

```
🤖 Climate AI Assistant
├── 🔧 API Configuration (expandable)
├── 💬 Chat Interface
├── 🗑️ Clear Chat Button
├── 💡 Suggested Questions
└── 📚 About Section
```

## 🧪 Test Before Using

Run the test script to verify everything works:
```bash
python simple_test.py
```

Expected output:
```
✅ Climate question detection - Working
✅ Fallback knowledge base - Working
✅ Response formatting - Working
🔧 Google Search API - Ready for configuration
```

## 🌍 Educational Use Cases

### For Educators:
- Interactive climate lessons
- Q&A sessions with students
- Real-time fact checking
- Current event discussions

### For NGOs:
- Community workshops
- Climate awareness campaigns
- Policy discussion support
- Environmental education

### For Individuals:
- Personal climate learning
- Sustainability guidance
- Environmental research
- Green lifestyle tips

## 🔒 Privacy & Security

- **No personal data stored**
- **API keys entered locally**
- **Chat history session-based only**
- **No external data collection**

## 🆘 Troubleshooting

### Common Issues:

**"Please ask climate-related questions"**
- Solution: Include climate/environment keywords in your question

**"No relevant information found"**
- Solution: Check API configuration or use built-in mode

**"Search error"**
- Solution: Verify API key and internet connection

### Getting Help:
1. Check [GOOGLE_API_SETUP.md](GOOGLE_API_SETUP.md) for API issues
2. Run `python simple_test.py` to test core functionality
3. Ensure all dependencies are installed: `pip install -r requirements.txt`

## 🎉 Ready to Start!

1. **Launch the app**: `streamlit run app/index.py`
2. **Navigate to**: "🤖 Climate AI Assistant"
3. **Start with**: "How can I reduce my carbon footprint?"
4. **Explore**: Use suggested questions or ask your own!

---

**Supporting SDG 13: Climate Action through AI-powered education and awareness** 🌱