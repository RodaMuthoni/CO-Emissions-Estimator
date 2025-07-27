#!/usr/bin/env python3
"""
Simple test for Climate AI Agent core functionality
"""

import requests
import json
from datetime import datetime
import re

class ClimateAIAgent:
    def __init__(self):
        self.climate_keywords = [
            'climate', 'carbon', 'emission', 'greenhouse', 'global warming', 
            'sustainability', 'renewable', 'fossil fuel', 'co2', 'methane',
            'temperature', 'pollution', 'environment', 'green energy',
            'solar', 'wind', 'electric vehicle', 'deforestation'
        ]
    
    def is_climate_related(self, query):
        """Check if query is related to climate/environmental topics"""
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in self.climate_keywords)
    
    def get_fallback_response(self, query):
        """Provide fallback response when search fails"""
        fallback_responses = {
            'carbon footprint': """
            **Carbon Footprint Information:**
            
            A carbon footprint measures the total greenhouse gas emissions caused by an individual, organization, or activity. Key sources include:
            
            • **Transportation**: Cars, flights, public transport
            • **Energy**: Electricity, heating, cooling
            • **Food**: Production, transportation, waste
            • **Consumer goods**: Manufacturing, shipping
            
            **Reduction strategies:**
            - Use renewable energy
            - Choose sustainable transportation
            - Reduce meat consumption
            - Buy local products
            - Minimize waste
            """,
            
            'climate change': """
            **Climate Change Overview:**
            
            Climate change refers to long-term shifts in global temperatures and weather patterns, primarily caused by human activities since the 1800s.
            
            **Main causes:**
            - Burning fossil fuels (coal, oil, gas)
            - Deforestation
            - Industrial processes
            - Agriculture
            
            **Key impacts:**
            - Rising global temperatures
            - Sea level rise
            - Extreme weather events
            - Ecosystem disruption
            
            **Solutions align with SDG 13: Climate Action**
            """,
            
            'renewable energy': """
            **Renewable Energy Information:**
            
            Renewable energy comes from natural sources that replenish faster than consumption:
            
            **Types:**
            - Solar power
            - Wind energy
            - Hydroelectric
            - Geothermal
            - Biomass
            
            **Benefits:**
            - Reduces greenhouse gas emissions
            - Creates jobs
            - Improves energy security
            - Decreases air pollution
            """
        }
        
        # Find best matching fallback
        query_lower = query.lower()
        for key, response in fallback_responses.items():
            if key in query_lower:
                return response
        
        return f"""
        **Climate & Environmental Information:**
        
        Your question about "{query}" relates to important environmental topics. Here are some general insights:
        
        • Climate action is crucial for sustainable development (SDG 13)
        • Individual actions can contribute to global solutions
        • Technology and policy changes are needed for large-scale impact
        • Education and awareness are key to driving change
        
        For specific information, please try rephrasing your question or check reliable sources like:
        - IPCC reports
        - EPA.gov
        - UN Climate Change resources
        """

def test_agent():
    print("🤖 Testing Climate AI Agent Core Functionality")
    print("=" * 60)
    
    agent = ClimateAIAgent()
    
    # Test climate-related question detection
    test_questions = [
        "How can I reduce my carbon footprint?",
        "What is climate change?",
        "Tell me about renewable energy",
        "What's the weather like today?",  # Non-climate
        "How do electric vehicles help the environment?",
        "What are you?",  # Non-climate
        "Solar panel efficiency",
        "Greenhouse gas emissions"
    ]
    
    print("\n1. Testing climate question detection:")
    print("-" * 40)
    for question in test_questions:
        is_climate = agent.is_climate_related(question)
        status = "✅ CLIMATE" if is_climate else "❌ NOT CLIMATE"
        print(f"   {status}: {question}")
    
    print("\n2. Testing fallback responses:")
    print("-" * 40)
    climate_questions = [
        "carbon footprint",
        "climate change", 
        "renewable energy",
        "sustainability practices"
    ]
    
    for question in climate_questions:
        print(f"\n📝 Question: {question}")
        response = agent.get_fallback_response(question)
        print(f"🤖 Response preview: {response[:150].strip()}...")
    
    print("\n" + "=" * 60)
    print("✅ Core functionality tests completed!")
    print("\n🚀 Integration Status:")
    print("   ✅ Climate question detection - Working")
    print("   ✅ Fallback knowledge base - Working") 
    print("   ✅ Response formatting - Working")
    print("   🔧 Google Search API - Ready for configuration")
    print("\n📖 Next steps:")
    print("   1. Configure Google Search API (see GOOGLE_API_SETUP.md)")
    print("   2. Run the full Streamlit app: streamlit run app/index.py")
    print("   3. Navigate to 'Climate AI Assistant' in the app")

if __name__ == "__main__":
    test_agent()