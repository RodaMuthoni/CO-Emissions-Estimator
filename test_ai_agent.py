#!/usr/bin/env python3
"""
Test script for Climate AI Agent
Run this to test the AI agent functionality without the full Streamlit app
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

# Import the ClimateAIAgent class
exec(open('app/climate_ai_agent.py').read())

def test_agent():
    print("🤖 Testing Climate AI Agent")
    print("=" * 50)
    
    # Create agent instance
    agent = ClimateAIAgent()
    
    # Test climate-related question detection
    test_questions = [
        "How can I reduce my carbon footprint?",
        "What is climate change?",
        "Tell me about renewable energy",
        "What's the weather like today?",  # Non-climate
        "How do electric vehicles help the environment?",
        "What are you?",  # Non-climate
    ]
    
    print("\n1. Testing climate question detection:")
    for question in test_questions:
        is_climate = agent.is_climate_related(question)
        status = "✅ CLIMATE" if is_climate else "❌ NOT CLIMATE"
        print(f"   {status}: {question}")
    
    print("\n2. Testing fallback responses:")
    climate_questions = [
        "carbon footprint",
        "climate change", 
        "renewable energy",
        "sustainability practices"
    ]
    
    for question in climate_questions:
        print(f"\n📝 Question: {question}")
        response = agent.get_fallback_response(question)
        print(f"🤖 Response: {response[:200]}...")
    
    print("\n3. Testing search result formatting:")
    # Mock search results
    mock_search_data = {
        'items': [
            {
                'title': 'Climate Change Basics | EPA',
                'snippet': 'Climate change refers to long-term shifts in global temperatures...',
                'link': 'https://www.epa.gov/climate-change'
            },
            {
                'title': 'What is Carbon Footprint?',
                'snippet': 'A carbon footprint is the total greenhouse gas emissions...',
                'link': 'https://example.com/carbon-footprint'
            }
        ]
    }
    
    formatted = agent.format_search_results(mock_search_data)
    print(f"📊 Formatted results: {len(formatted)} items")
    for i, result in enumerate(formatted, 1):
        print(f"   {i}. {result['title']}")
    
    print("\n✅ All tests completed!")
    print("\n🚀 To use with Google Search API:")
    print("   1. Get API key from Google Cloud Console")
    print("   2. Create Custom Search Engine")
    print("   3. Configure in the Streamlit app")
    print("   4. See GOOGLE_API_SETUP.md for detailed instructions")

if __name__ == "__main__":
    test_agent()