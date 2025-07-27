import streamlit as st
import requests
from datetime import datetime
import time

class ClimateAIAgent:
    def __init__(self):
        self.climate_keywords = [
            'climate', 'carbon', 'emission', 'greenhouse', 'global warming', 
            'sustainability', 'renewable', 'fossil fuel', 'co2', 'methane',
            'temperature', 'pollution', 'environment', 'green energy',
            'solar', 'wind', 'electric vehicle', 'deforestation'
        ]
    
    def is_climate_related(self, query):
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in self.climate_keywords)
    
    def get_fallback_response(self, query):
        fallback_responses = {
            'carbon footprint': "A carbon footprint measures total greenhouse gas emissions. Reduce it by using renewable energy, sustainable transport, and minimizing waste.",
            'climate change': "Climate change refers to long-term temperature shifts caused by human activities like burning fossil fuels. Solutions include renewable energy and policy changes.",
            'renewable energy': "Renewable energy (solar, wind, hydro) reduces emissions, creates jobs, and improves energy security.",
        }
        
        query_lower = query.lower()
        for key, response in fallback_responses.items():
            if key in query_lower:
                return response
        
        return f"Your question about '{query}' relates to climate action (SDG 13). Consider using our carbon calculator and following sustainability recommendations."

def render_floating_chat():
    # Initialize session state
    if 'chat_open' not in st.session_state:
        st.session_state.chat_open = False
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    agent = ClimateAIAgent()
    
    # CSS for floating chat widget
    st.markdown("""
    <style>
    .chat-widget {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
    }
    
    .chat-button {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #00c851, #007e33);
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 200, 81, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: white;
        transition: all 0.3s ease;
    }
    
    .chat-button:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(0, 200, 81, 0.4);
    }
    
    .chat-popup {
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 350px;
        height: 400px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        z-index: 1001;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }
    
    .chat-header {
        background: linear-gradient(135deg, #00c851, #007e33);
        color: white;
        padding: 15px;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .chat-messages {
        flex: 1;
        padding: 10px;
        overflow-y: auto;
        max-height: 250px;
    }
    
    .chat-input {
        padding: 10px;
        border-top: 1px solid #eee;
    }
    
    .message {
        margin: 8px 0;
        padding: 8px 12px;
        border-radius: 12px;
        max-width: 80%;
    }
    
    .user-message {
        background: #e3f2fd;
        margin-left: auto;
        text-align: right;
    }
    
    .ai-message {
        background: #f1f8e9;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Floating chat button
    if st.button("🤖", key="chat_toggle", help="Climate AI Assistant"):
        st.session_state.chat_open = not st.session_state.chat_open
    
    # Chat popup
    if st.session_state.chat_open:
        with st.container():
            st.markdown('<div class="chat-popup">', unsafe_allow_html=True)
            
            # Header
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown("**🌍 Climate AI Assistant**")
            with col2:
                if st.button("✕", key="close_chat"):
                    st.session_state.chat_open = False
                    st.experimental_rerun()
            
            # Messages
            st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
            for msg_type, message in st.session_state.chat_messages:
                if msg_type == "user":
                    st.markdown(f'<div class="message user-message">You: {message}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="message ai-message">🤖: {message}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Input
            user_input = st.text_input("Ask about climate...", key="chat_input", placeholder="How can I reduce emissions?")
            
            if st.button("Send", key="send_message") and user_input:
                if agent.is_climate_related(user_input):
                    response = agent.get_fallback_response(user_input)
                    st.session_state.chat_messages.append(("user", user_input))
                    st.session_state.chat_messages.append(("ai", response))
                    st.experimental_rerun()
                else:
                    st.warning("Please ask climate-related questions only.")
            
            st.markdown('</div>', unsafe_allow_html=True)

def render_sidebar_chat():
    # Custom CSS for attractive chat widget
    st.markdown("""
    <style>
    .chat-widget {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        color: white;
    }
    .chat-circle {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #00c851, #007e33);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 10px;
        font-size: 20px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .chat-circle:hover {
        transform: scale(1.1);
    }
    .chat-message {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 8px;
        margin: 5px 0;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Circular chat button
    st.sidebar.markdown('<div class="chat-circle" title="Climate AI Assistant">🤖</div>', unsafe_allow_html=True)
    
    # Initialize
    if 'sidebar_messages' not in st.session_state:
        st.session_state.sidebar_messages = []
    if 'chat_expanded' not in st.session_state:
        st.session_state.chat_expanded = False
    
    agent = ClimateAIAgent()
    
    # Toggle chat
    if st.sidebar.button("💬 Climate AI Chat", key="ai_chat_toggle_btn"):
        st.session_state.chat_expanded = not st.session_state.get('chat_expanded', False)
    
    # Chat interface
    if st.session_state.get('chat_expanded', False):
        with st.sidebar:
            st.markdown('<div class="chat-widget">', unsafe_allow_html=True)
            
            # Display messages
            if st.session_state.sidebar_messages:
                for msg_type, message in st.session_state.sidebar_messages[-2:]:
                    if msg_type == "user":
                        st.markdown(f'<div class="chat-message">**You:** {message[:50]}...</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="chat-message">**🤖:** {message[:50]}...</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="chat-message">👋 Ask me about climate!</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Input
            user_input = st.text_input("Climate question:", key="ai_chat_input", placeholder="How to reduce CO2?")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔍 Ask", key="ai_ask_btn"):
                    if user_input and agent.is_climate_related(user_input):
                        response = agent.get_fallback_response(user_input)
                        st.session_state.sidebar_messages.append(("user", user_input))
                        st.session_state.sidebar_messages.append(("ai", response))
                        pass
                    elif user_input:
                        st.warning("Climate topics only!")
            
            with col2:
                if st.button("🗑️ Clear", key="ai_clear_btn"):
                    st.session_state.sidebar_messages = []

if __name__ == "__main__":
    render_sidebar_chat()