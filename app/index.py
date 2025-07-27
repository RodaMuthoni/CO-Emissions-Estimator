import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="EcoSafari - Carbon Footprint Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Handle missing logo file gracefully
try:
    st.logo("Images/menu.png")
except:
    pass  # Skip logo if file doesn't exist

# --- Buy Me A Coffee Button (Global, top right) 
st.markdown(
    """
    <div style="text-align:right; margin-top:-30px; margin-bottom:10px;">
        <a href="https://www.buymeacoffee.com/michaelranda" target="_blank">
            <img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg" alt="Buy Us Coffee" style="height: 60px;" />
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state for navigation
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = 'app'

# Navigation sections
st.sidebar.markdown("### App Navigations")
app_nav = st.sidebar.radio("App Navigation", [
    "🏠 Home",
    "👨‍💻 Developers | Team"
], key="app_nav", label_visibility="collapsed")

# Check if app navigation changed
if app_nav != st.session_state.get('last_app_nav', "🏠 Home"):
    st.session_state.selected_section = 'app'
    st.session_state.last_app_nav = app_nav

st.sidebar.markdown("### Modules")
module_nav = st.sidebar.radio("Module Navigation", [
    "🐾 Calculate My Carbon Footprint",
    "🤹‍♂️ Recommendations", 
    "🏭 Global Carbon Emission",
    "🌍 Country CO₂ Analyzer",
    "🌱 Sustainable Practices"
], key="module_nav", label_visibility="collapsed")

# Check if module navigation changed
if module_nav != st.session_state.get('last_module_nav', "🐾 Calculate My Carbon Footprint"):
    st.session_state.selected_section = 'module'
    st.session_state.last_module_nav = module_nav

# Determine selected page based on active section
if st.session_state.selected_section == 'app':
    page = app_nav
else:
    page = module_nav

# Add parent directory to path for imports
import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Get current directory path
current_dir = os.path.dirname(__file__)

# Add AI Chat Widget at bottom of sidebar
st.sidebar.markdown("---")
st.sidebar.markdown('<div style="text-align:center;"><div style="width:50px;height:50px;border-radius:50%;background:linear-gradient(135deg,#00c851,#007e33);display:flex;align-items:center;justify-content:center;margin:0 auto 10px;font-size:20px;color:white;">🤖</div></div>', unsafe_allow_html=True)

if 'chat_expanded' not in st.session_state:
    st.session_state.chat_expanded = False
if 'sidebar_messages' not in st.session_state:
    st.session_state.sidebar_messages = []

if st.sidebar.button("💬 Climate AI Chat"):
    st.session_state.chat_expanded = not st.session_state.chat_expanded

if st.session_state.chat_expanded:
    user_input = st.sidebar.text_input("Ask about climate:", placeholder="How to reduce CO2?")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("🔍 Ask") and user_input:
            climate_keywords = ['climate', 'carbon', 'emission', 'greenhouse', 'sustainability', 'renewable', 'environment']
            if any(keyword in user_input.lower() for keyword in climate_keywords):
                response = "Reduce emissions by using renewable energy, sustainable transport, and minimizing waste. Support climate action (SDG 13)!"
                st.session_state.sidebar_messages.append(("user", user_input))
                st.session_state.sidebar_messages.append(("ai", response))
            else:
                st.sidebar.warning("Climate topics only!")
    with col2:
        if st.button("🗑️ Clear"):
            st.session_state.sidebar_messages = []
    
    for msg_type, message in st.session_state.sidebar_messages[-2:]:
        if msg_type == "user":
            st.sidebar.markdown(f"**You:** {message[:50]}...")
        else:
            st.sidebar.markdown(f"**🤖:** {message[:50]}...")

# Page routing
if page == "🏠 Home":
    try:
        exec(open(os.path.join(current_dir, "home.py")).read())
    except Exception as e:
        st.error(f"Error loading Home: {e}")
        
elif page == "👨‍💻 Developers | Team":
    try:
        exec(open(os.path.join(current_dir, "developers.py")).read())
    except Exception as e:
        st.error(f"Error loading Developers: {e}")
        
elif page == "🐾 Calculate My Carbon Footprint":
    try:
        exec(open(os.path.join(current_dir, "user_input.py")).read())
    except Exception as e:
        st.error(f"Error loading Carbon Footprint Calculator: {e}")
        
elif page == "🤹‍♂️ Recommendations":
    try:
        exec(open(os.path.join(current_dir, "recommendations.py")).read())
    except Exception as e:
        st.error(f"Error loading Recommendations: {e}")
        
elif page == "🏭 Global Carbon Emission":
    try:
        exec(open(os.path.join(current_dir, "Global_Climate.py")).read())
    except Exception as e:
        st.error(f"Error loading Global Climate: {e}")
        
elif page == "🌍 Country CO₂ Analyzer":
    try:
        # Import and run the main function instead of exec
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        from app import main
        main()
    except Exception as e:
        st.error(f"Error loading Country CO₂ Analyzer: {e}")
        
elif page == "🌱 Sustainable Practices":
    try:
        exec(open(os.path.join(current_dir, "sustainability.py")).read())
    except Exception as e:
        st.error(f"Error loading Sustainability: {e}")