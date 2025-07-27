import streamlit as st
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
    
    def search_google(self, query, api_key, search_engine_id):
        """Search Google Custom Search API"""
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'key': api_key,
                'cx': search_engine_id,
                'q': f"{query} climate change environment sustainability",
                'num': 5
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            st.error(f"Search error: {str(e)}")
            return None
    
    def format_search_results(self, search_data):
        """Format search results into readable text"""
        if not search_data or 'items' not in search_data:
            return "No relevant information found."
        
        formatted_results = []
        for item in search_data['items'][:3]:  # Top 3 results
            title = item.get('title', 'No title')
            snippet = item.get('snippet', 'No description')
            link = item.get('link', '#')
            
            formatted_results.append({
                'title': title,
                'snippet': snippet,
                'link': link
            })
        
        return formatted_results
    
    def generate_climate_response(self, query, search_results):
        """Generate AI response based on search results"""
        if not search_results:
            return self.get_fallback_response(query)
        
        # Create a comprehensive response
        response = f"Based on current information about '{query}':\n\n"
        
        for i, result in enumerate(search_results, 1):
            response += f"**{i}. {result['title']}**\n"
            response += f"{result['snippet']}\n"
            response += f"[Read more]({result['link']})\n\n"
        
        # Add climate action context
        response += self.add_climate_context(query)
        
        return response
    
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
    
    def add_climate_context(self, query):
        """Add relevant climate action context"""
        context = f"""
        ---
        **🌍 Climate Action Context (SDG 13):**
        
        This information supports **Sustainable Development Goal 13: Climate Action**, which aims to:
        - Strengthen resilience to climate-related hazards
        - Integrate climate change measures into policies
        - Improve education and awareness on climate change
        
        **How you can take action:**
        • Calculate your carbon footprint using our tool
        • Follow our sustainability recommendations
        • Share climate knowledge with your community
        • Support renewable energy initiatives
        
        *Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*
        """
        return context

def main():
    st.title("🤖 Climate AI Assistant")
    st.subheader("Ask questions about climate change, sustainability, and environmental topics")
    
    # Initialize AI agent
    agent = ClimateAIAgent()
    
    # API Configuration section
    with st.expander("🔧 API Configuration (Optional)", expanded=False):
        st.info("Configure Google Custom Search API for enhanced responses. Leave empty to use built-in knowledge.")
        
        col1, col2 = st.columns(2)
        with col1:
            api_key = st.text_input("Google API Key", type="password", help="Get from Google Cloud Console")
        with col2:
            search_engine_id = st.text_input("Custom Search Engine ID", help="Create at programmablesearchengine.google.com")
        
        if api_key and search_engine_id:
            st.success("✅ API configured - Enhanced search enabled")
        else:
            st.warning("⚠️ Using built-in knowledge base")
    
    # Chat interface
    st.markdown("---")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for i, (question, answer) in enumerate(st.session_state.chat_history):
        with st.container():
            st.markdown(f"**🙋 You:** {question}")
            st.markdown(f"**🤖 Climate AI:** {answer}")
            st.markdown("---")
    
    # Input section
    user_question = st.text_input("Ask a climate-related question:", placeholder="e.g., How can I reduce my carbon footprint?")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        ask_button = st.button("🔍 Ask", type="primary")
    with col2:
        clear_button = st.button("🗑️ Clear Chat")
    
    if clear_button:
        st.session_state.chat_history = []
        st.experimental_rerun()
    
    if ask_button and user_question:
        # Check if question is climate-related
        if not agent.is_climate_related(user_question):
            st.warning("⚠️ Please ask questions related to climate, environment, or sustainability topics.")
            st.stop()
        
        with st.spinner("🔍 Searching for the latest information..."):
            # Search for information
            search_results = None
            if api_key and search_engine_id:
                search_data = agent.search_google(user_question, api_key, search_engine_id)
                search_results = agent.format_search_results(search_data)
            
            # Generate response
            response = agent.generate_climate_response(user_question, search_results)
            
            # Add to chat history
            st.session_state.chat_history.append((user_question, response))
            
            # Display new response
            st.markdown("**🤖 Climate AI:**")
            st.markdown(response)
    
    # Suggested questions
    st.markdown("---")
    st.markdown("**💡 Suggested Questions:**")
    
    suggestions = [
        "How can I calculate my carbon footprint?",
        "What are the main causes of climate change?",
        "How do renewable energy sources help the environment?",
        "What are the best ways to reduce emissions at home?",
        "How does deforestation affect climate change?",
        "What is the Paris Climate Agreement?",
        "How do electric vehicles impact the environment?",
        "What are sustainable transportation options?"
    ]
    
    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(suggestion, key=f"suggestion_{i}"):
                st.session_state.temp_question = suggestion
                st.experimental_rerun()
    
    # Handle suggested question clicks
    if hasattr(st.session_state, 'temp_question'):
        user_question = st.session_state.temp_question
        del st.session_state.temp_question
        
        with st.spinner("🔍 Searching for information..."):
            search_results = None
            if api_key and search_engine_id:
                search_data = agent.search_google(user_question, api_key, search_engine_id)
                search_results = agent.format_search_results(search_data)
            
            response = agent.generate_climate_response(user_question, search_results)
            st.session_state.chat_history.append((user_question, response))
            st.experimental_rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **🌱 About Climate AI Assistant:**
    - Provides climate and environmental information
    - Supports SDG 13: Climate Action
    - Uses live search when API is configured
    - Built-in knowledge base for offline use
    
    *This tool is designed to educate and promote climate awareness.*
    """)

if __name__ == "__main__":
    main()