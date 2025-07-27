# 🔧 Google Search API Setup Guide

This guide helps you configure the Google Custom Search API for the Climate AI Assistant to provide real-time, up-to-date information.

## 📋 Prerequisites

- Google account
- Google Cloud Console access
- Basic understanding of API keys

## 🚀 Step-by-Step Setup

### 1. Enable Google Custom Search API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Navigate to **APIs & Services** > **Library**
4. Search for "Custom Search API"
5. Click on "Custom Search API" and enable it

### 2. Create API Key

1. Go to **APIs & Services** > **Credentials**
2. Click **+ CREATE CREDENTIALS** > **API Key**
3. Copy the generated API key
4. (Optional) Restrict the key to Custom Search API only

### 3. Create Custom Search Engine

1. Visit [Programmable Search Engine](https://programmablesearchengine.google.com/)
2. Click **Add** to create new search engine
3. Configure:
   - **Sites to search**: Leave empty for web-wide search
   - **Name**: "Climate AI Search" (or any name)
   - **Search settings**: Enable "Search the entire web"
4. Click **Create**
5. Copy the **Search engine ID** from the overview page

### 4. Configure in Application

1. Open the Climate AI Assistant in the app
2. Expand the "🔧 API Configuration" section
3. Enter:
   - **Google API Key**: Your API key from step 2
   - **Custom Search Engine ID**: Your search engine ID from step 3
4. The system will show "✅ API configured - Enhanced search enabled"

## 💰 Pricing Information

- **Free tier**: 100 search queries per day
- **Paid tier**: $5 per 1000 queries (after free tier)
- Monitor usage in Google Cloud Console

## 🔒 Security Best Practices

1. **Restrict API Key**:
   - Limit to Custom Search API only
   - Add application restrictions if needed

2. **Environment Variables** (for production):
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   export SEARCH_ENGINE_ID="your_search_engine_id_here"
   ```

3. **Never commit API keys** to version control

## 🛠️ Troubleshooting

### Common Issues:

**"API key not valid"**
- Ensure Custom Search API is enabled
- Check API key restrictions
- Verify billing is enabled (if exceeded free tier)

**"Search engine not found"**
- Verify Search Engine ID is correct
- Ensure search engine is set to "Search the entire web"

**"Quota exceeded"**
- Check daily usage in Google Cloud Console
- Consider upgrading to paid tier

### Fallback Mode:
If API setup fails, the Climate AI Assistant will use its built-in knowledge base to answer questions.

## 📚 Additional Resources

- [Google Custom Search API Documentation](https://developers.google.com/custom-search/v1/overview)
- [Programmable Search Engine Help](https://support.google.com/programmable-search/)
- [Google Cloud Console](https://console.cloud.google.com/)

## 🌍 Benefits of API Integration

With API configured, the Climate AI Assistant provides:
- ✅ Real-time climate data
- ✅ Latest research findings
- ✅ Current policy updates
- ✅ Recent environmental news
- ✅ Up-to-date statistics

Without API, it uses built-in knowledge base with general climate information.