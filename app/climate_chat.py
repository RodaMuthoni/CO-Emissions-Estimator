import streamlit as st
import random
import time

# Initialize session state
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []
if 'quiz_mode' not in st.session_state:
    st.session_state.quiz_mode = False
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = None

# Climate knowledge base
CLIMATE_RESPONSES = {
    'carbon footprint': "Your carbon footprint is the total greenhouse gas emissions caused by your activities. Key sources include transportation (29%), electricity (25%), heating (13%), and food (10-15%). Track and reduce by using public transport, renewable energy, and sustainable practices.",
    'renewable energy': "Renewable energy sources like solar, wind, hydro, and geothermal produce minimal CO₂ emissions. Solar panels can reduce household emissions by 3-4 tons annually. Wind energy is now the cheapest electricity source in many regions.",
    'climate change': "Climate change refers to long-term shifts in global temperatures and weather patterns. Since 1880, global temperature has risen by 1.1°C. Main causes: fossil fuel burning (75%), deforestation (11%), agriculture (24%).",
    'greenhouse gases': "Main greenhouse gases: CO₂ (76%), Methane (16%), Nitrous Oxide (6%), Fluorinated gases (2%). CO₂ stays in atmosphere for 300-1000 years. Methane is 25x more potent than CO₂ but lasts only 12 years.",
    'sustainable transport': "Transportation accounts for 29% of global emissions. Solutions: Electric vehicles (reduce emissions by 50-70%), public transport (reduce personal emissions by 45%), cycling/walking (zero emissions), carpooling (reduce by 25%).",
    'energy efficiency': "Energy efficiency can reduce emissions by 40% by 2040. Simple actions: LED bulbs (75% less energy), smart thermostats (10-15% savings), proper insulation (30% heating reduction), Energy Star appliances (10-50% savings).",
    'deforestation': "Deforestation causes 11% of global CO₂ emissions. Forests absorb 2.6 billion tons of CO₂ annually. One mature tree absorbs 48 lbs of CO₂ per year. Amazon rainforest produces 20% of world's oxygen.",
    'ocean acidification': "Oceans absorb 30% of human CO₂ emissions, causing pH to drop by 0.1 units since pre-industrial times. This threatens marine ecosystems, coral reefs, and fisheries that feed 3 billion people.",
    'paris agreement': "Paris Agreement aims to limit global warming to 1.5°C above pre-industrial levels. 196 countries committed to reduce emissions. Current pledges would lead to 2.7°C warming - more action needed.",
    'carbon neutral': "Carbon neutrality means balancing CO₂ emissions with removal/offsetting. Strategies: reduce emissions first, then offset remaining through reforestation, carbon capture, renewable energy projects."
}

SAMPLE_QUESTIONS = [
    "🌡️ What is climate change and its main causes?",
    "🚗 How can I reduce my transportation emissions?",
    "⚡ What are the benefits of renewable energy?",
    "🌳 How does deforestation affect climate?",
    "🏠 What are the best energy efficiency tips?",
    "🌊 What is ocean acidification?",
    "📊 How do I calculate my carbon footprint?",
    "♻️ What does carbon neutral mean?",
    "🌍 What is the Paris Agreement?",
    "💨 What are greenhouse gases?",
    "🔋 How effective are electric vehicles?",
    "🌱 What are sustainable practices?",
    "🏭 Which industries produce most emissions?",
    "❄️ How is climate change affecting polar ice?",
    "🌾 How does agriculture contribute to emissions?"
]

QUIZ_QUESTIONS = [
    {
        "question": "What percentage of global emissions comes from transportation?",
        "options": ["15%", "29%", "35%", "42%"],
        "correct": 1,
        "explanation": "Transportation accounts for 29% of global greenhouse gas emissions, making it the largest source."
    },
    {
        "question": "How much CO₂ can one mature tree absorb per year?",
        "options": ["25 lbs", "48 lbs", "75 lbs", "100 lbs"],
        "correct": 1,
        "explanation": "One mature tree can absorb approximately 48 pounds of CO₂ per year."
    },
    {
        "question": "By how much has global temperature risen since 1880?",
        "options": ["0.5°C", "1.1°C", "1.8°C", "2.3°C"],
        "correct": 1,
        "explanation": "Global temperature has risen by approximately 1.1°C since 1880."
    },
    {
        "question": "What is the most potent greenhouse gas?",
        "options": ["CO₂", "Methane", "Nitrous Oxide", "Water Vapor"],
        "correct": 1,
        "explanation": "Methane is 25 times more potent than CO₂, though it stays in the atmosphere for a shorter time."
    },
    {
        "question": "How much of human CO₂ emissions do oceans absorb?",
        "options": ["15%", "20%", "30%", "45%"],
        "correct": 2,
        "explanation": "Oceans absorb about 30% of human CO₂ emissions, which causes ocean acidification."
    }
]

def get_ai_response(user_input):
    """Generate AI response based on user input"""
    user_input_lower = user_input.lower()
    
    # Check for specific topics
    for topic, response in CLIMATE_RESPONSES.items():
        if topic in user_input_lower:
            return response
    
    # General climate keywords
    climate_keywords = ['climate', 'carbon', 'emission', 'greenhouse', 'sustainability', 'renewable', 'environment', 'global warming', 'pollution']
    
    if any(keyword in user_input_lower for keyword in climate_keywords):
        general_responses = [
            "Climate action is crucial for our planet's future. Focus on reducing energy consumption, using sustainable transport, and supporting renewable energy initiatives.",
            "Every small action counts! Consider switching to renewable energy, reducing meat consumption, and using public transportation to lower your carbon footprint.",
            "The key to fighting climate change is collective action. Start with personal changes and advocate for policy reforms in your community.",
            "Sustainable living involves conscious choices: energy-efficient appliances, local food, minimal waste, and supporting eco-friendly businesses."
        ]
        return random.choice(general_responses)
    
    return "I specialize in climate and environmental topics. Please ask me about carbon emissions, renewable energy, sustainability, or climate change!"

# Page header
st.markdown("""
<div style="background: linear-gradient(135deg, #00c851, #007e33); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color: white; text-align: center; margin: 0;">🤖 Climate AI Assistant</h1>
    <p style="color: white; text-align: center; margin: 5px 0 0 0;">Your intelligent guide to climate action and sustainability</p>
</div>
""", unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 💬 Chat with Climate AI")
    
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages
        for i, (role, message) in enumerate(st.session_state.chat_messages):
            if role == "user":
                st.markdown(f"""
                <div style="background: #2196F3; color: white; padding: 15px; border-radius: 15px; margin: 10px 0; margin-left: 20%; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <strong>You:</strong> {message}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: #4CAF50; color: white; padding: 15px; border-radius: 15px; margin: 10px 0; margin-right: 20%; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <strong>🤖 Climate AI:</strong> {message}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    st.markdown("---")
    user_input = st.text_input("Ask me anything about climate:", placeholder="How can I reduce my carbon footprint?", key="chat_input")
    
    col_send, col_clear = st.columns([1, 1])
    with col_send:
        if st.button("🚀 Send", use_container_width=True) and user_input:
            # Add user message
            st.session_state.chat_messages.append(("user", user_input))
            
            # Generate AI response
            with st.spinner("🤖 Thinking..."):
                time.sleep(1)  # Simulate processing
                response = get_ai_response(user_input)
                st.session_state.chat_messages.append(("ai", response))
    
    with col_clear:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_messages = []

with col2:
    st.markdown("### 🎯 Quick Actions")
    
    # Sample questions
    st.markdown("#### 💡 Sample Questions")
    st.markdown("Click any question to ask:")
    
    for i, question in enumerate(SAMPLE_QUESTIONS[:8]):  # Show first 8
        if st.button(question, key=f"sample_{i}", use_container_width=True):
            # Remove emoji and ask the question
            clean_question = question.split(" ", 1)[1]
            st.session_state.chat_messages.append(("user", clean_question))
            response = get_ai_response(clean_question)
            st.session_state.chat_messages.append(("ai", response))
    
    # Show more questions button
    if st.button("📋 Show More Questions", use_container_width=True):
        st.markdown("#### 🔍 Additional Questions")
        for i, question in enumerate(SAMPLE_QUESTIONS[8:]):
            if st.button(question, key=f"more_{i}", use_container_width=True):
                clean_question = question.split(" ", 1)[1]
                st.session_state.chat_messages.append(("user", clean_question))
                response = get_ai_response(clean_question)
                st.session_state.chat_messages.append(("ai", response))
    
    st.markdown("---")
    
    # Quiz section
    st.markdown("### 🧠 Climate Quiz")
    
    if not st.session_state.quiz_mode:
        if st.button("🎮 Start Climate Quiz", use_container_width=True):
            st.session_state.quiz_mode = True
            st.session_state.current_quiz = random.choice(QUIZ_QUESTIONS)
    else:
        if st.session_state.current_quiz:
            quiz = st.session_state.current_quiz
            st.markdown(f"**Question:** {quiz['question']}")
            
            # Quiz options
            for i, option in enumerate(quiz['options']):
                if st.button(option, key=f"quiz_option_{i}", use_container_width=True):
                    if i == quiz['correct']:
                        st.success("✅ Correct!")
                        st.info(f"💡 {quiz['explanation']}")
                    else:
                        st.error("❌ Incorrect!")
                        st.info(f"💡 {quiz['explanation']}")
                    
                    # Add to chat
                    st.session_state.chat_messages.append(("user", f"Quiz: {quiz['question']}"))
                    result = "✅ Correct!" if i == quiz['correct'] else "❌ Incorrect!"
                    st.session_state.chat_messages.append(("ai", f"{result} {quiz['explanation']}"))
                    
                    st.session_state.quiz_mode = False
                    st.session_state.current_quiz = None
        
        if st.button("🚪 Exit Quiz", use_container_width=True):
            st.session_state.quiz_mode = False
            st.session_state.current_quiz = None
    
    st.markdown("---")
    
    # Advanced features
    st.markdown("### 🚀 Advanced Features")
    
    if st.button("📊 Carbon Calculator", use_container_width=True):
        st.session_state.chat_messages.append(("user", "How do I calculate my carbon footprint?"))
        response = "To calculate your carbon footprint: 1) Track transportation (miles driven, flights taken), 2) Monitor energy use (electricity, heating), 3) Consider diet (meat consumption), 4) Account for consumption (purchases, waste). Use our Carbon Calculator module for detailed analysis!"
        st.session_state.chat_messages.append(("ai", response))
    
    if st.button("🌍 Global Impact", use_container_width=True):
        st.session_state.chat_messages.append(("user", "What's the global climate situation?"))
        response = "Current global situation: CO₂ levels at 421 ppm (highest in 3M years), global temperature +1.1°C since 1880, sea level rising 3.3mm/year. We need 45% emission reduction by 2030 to limit warming to 1.5°C. Every fraction of a degree matters!"
        st.session_state.chat_messages.append(("ai", response))
    
    if st.button("💡 Sustainability Tips", use_container_width=True):
        st.session_state.chat_messages.append(("user", "Give me practical sustainability tips"))
        response = "Top sustainability tips: 1) Switch to LED bulbs (75% energy savings), 2) Use public transport/bike, 3) Eat less meat (reduce by 50% = 0.8 tons CO₂/year), 4) Unplug devices when not in use, 5) Buy local/seasonal food, 6) Use reusable bags/bottles, 7) Support renewable energy, 8) Reduce, reuse, recycle!"
        st.session_state.chat_messages.append(("ai", response))

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>🌱 <strong>Climate AI Assistant</strong> - Supporting SDG 13: Climate Action</p>
    <p>💡 Ask questions • 🧠 Take quizzes • 📊 Learn facts • 🌍 Take action</p>
</div>
""", unsafe_allow_html=True)