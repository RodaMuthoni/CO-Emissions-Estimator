# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# Remove authentication import since we're implementing it inline

# Custom CSS
st.markdown("""
<style>
.header {color: #1e3a8a;}
.metric {font-size: 1.5rem !important;}
.tip-box {border-left: 4px solid #10b981; padding: 0.5rem 1rem; margin: 1rem 0;}
.footer {margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #e5e7eb;}
</style>
""", unsafe_allow_html=True)

# Load data and model
@st.cache_resource
def load_resources():
    import os
    
    # Use relative path that works in both local and deployed environments
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load CSV - try multiple possible locations
    csv_paths = [
        os.path.join(current_dir, "country_emissions.csv"),
        "country_emissions.csv",
        os.path.join(current_dir, "..", "country_emissions.csv")
    ]
    
    emissions_df = None
    for csv_path in csv_paths:
        try:
            if os.path.exists(csv_path):
                emissions_df = pd.read_csv(csv_path)
                break
        except Exception as e:
            continue
    
    if emissions_df is None:
        st.error("Could not load country emissions data. Please ensure country_emissions.csv is in the project directory.")
        return None, None, []
    
    # Load model (optional)
    model = None
    model_paths = [
        os.path.join(current_dir, "country_emissions_model.pkl"),
        "country_emissions_model.pkl",
        os.path.join(current_dir, "..", "country_emissions_model.pkl")
    ]
    
    for model_path in model_paths:
        try:
            if os.path.exists(model_path):
                model = joblib.load(model_path)
                break
        except:
            continue
    
    country_list = sorted(emissions_df['Country'].unique())
    return model, emissions_df, country_list

# Initialize session state
def init_session():
    if 'comparison_data' not in st.session_state:
        st.session_state.comparison_data = []
    if 'user_location' not in st.session_state:
        st.session_state.user_location = "United States"

# Calculate emissions
def calculate_emissions(model, country, year, emissions_df):
    # Always use fallback method to avoid model issues
    country_data = emissions_df[emissions_df['Country'] == country]
    if not country_data.empty:
        # Use linear interpolation based on existing data
        years = country_data['Year'].values
        emissions = country_data['Per_Capita_CO2_kg'].values
        
        if year in years:
            return country_data[country_data['Year'] == year]['Per_Capita_CO2_kg'].values[0]
        elif len(years) > 1:
            # Simple linear interpolation/extrapolation
            return float(np.interp(year, years, emissions))
        else:
            return country_data['Per_Capita_CO2_kg'].mean()
    
    # Global fallback
    return emissions_df['Per_Capita_CO2_kg'].mean()

# Get country data
def get_country_data(df, country):
    country_data = df[df['Country'] == country].sort_values('Year')
    return country_data

# Get reduction targets   
def get_reduction_targets(current_emissions):
    return {
        "2030 (SDG Target)": current_emissions * 0.5,
        "2040": current_emissions * 0.3,
        "2050 (Net Zero)": current_emissions * 0.1
    }

# Get climate tips
def get_climate_tips(country, current_emissions, avg_emissions):
    tips = []
    
    if current_emissions > avg_emissions * 1.2:
        tips.append(f"🌍 **Reduce energy consumption**: {country}'s emissions are above average. Consider energy-efficient appliances and renewable energy sources.")
    else:
        tips.append(f"🌿 **Maintain sustainable practices**: {country} is performing better than average. Continue efforts to reduce emissions.")
    
    tips.append("🚗 **Promote electric vehicles**: Transportation is a major contributor to emissions. Support EV infrastructure development.")
    tips.append("🌳 **Protect and expand forests**: Natural carbon sinks are crucial for offsetting emissions.")
    tips.append("🏭 **Advocate for industrial regulations**: Support policies that require industries to reduce their carbon footprint.")
    tips.append("💡 **Educate communities**: Raise awareness about sustainable practices and climate action.")
    
    return tips

# Main page authentication function
def main_page_auth():
    st.title("🔒 Authentication Required")
    st.write("Please log in or sign up to access the Country CO₂ Emissions Analyzer")
    
    auth_mode = st.radio("Choose mode", ["Login", "Sign Up"], horizontal=True)
    
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("Username")
    with col2:
        password = st.text_input("Password", type="password")
    
    # Load users function from authentication module
    import os
    import hashlib
    
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def load_users():
        # Try multiple locations for users.csv
        current_dir = os.path.dirname(os.path.abspath(__file__))
        user_db_paths = [
            "users.csv",
            os.path.join(current_dir, "users.csv"),
            os.path.join(current_dir, "..", "users.csv")
        ]
        
        for USER_DB in user_db_paths:
            if os.path.exists(USER_DB):
                try:
                    df = pd.read_csv(USER_DB)
                    return dict(zip(df['username'], df['password']))
                except:
                    continue
        return {}
    
    def save_user(username, password_hash):
        # Use the first available location for users.csv
        current_dir = os.path.dirname(os.path.abspath(__file__))
        user_db_paths = [
            "users.csv",
            os.path.join(current_dir, "users.csv")
        ]
        
        USER_DB = user_db_paths[0]  # Default to current directory
        
        try:
            if os.path.exists(USER_DB):
                df = pd.read_csv(USER_DB)
                if username in df['username'].values:
                    return False
                df = pd.concat([df, pd.DataFrame([{'username': username, 'password': password_hash}])], ignore_index=True)
            else:
                df = pd.DataFrame([{'username': username, 'password': password_hash}])
            df.to_csv(USER_DB, index=False)
            return True
        except Exception as e:
            st.error(f"Error saving user data: {e}")
            return False
    
    users = load_users()
    
    if auth_mode == "Login":
        if st.button("Login", type="primary"):
            if username in users and users[username] == hash_password(password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"Welcome, {username}! Loading analyzer...")
                st.balloons()
                return True
            else:
                st.error("Invalid credentials")
    else:
        if st.button("Sign Up", type="primary"):
            if username in users:
                st.error("Username already exists")
            elif username and password:
                if save_user(username, hash_password(password)):
                    st.success("Account created! Please log in.")
                else:
                    st.error("Error creating account")
            else:
                st.error("Please enter username and password")
    
    return False

# Main application
def main():
    # Check authentication first
    if not st.session_state.get("authenticated", False):
        if main_page_auth():
            # Authentication successful, continue to main app
            pass
        else:
            # Still authenticating, stop here
            return
    
    # Load resources
    model, emissions_df, country_list = load_resources()
    
    # If data loading failed, show error and return
    if emissions_df is None or len(country_list) == 0:
        st.error("Unable to load emissions data. Please check if the data files are available.")
        return

    # Initialize session
    init_session()
    
    # Header
    st.title("🌍 Country CO₂ Emissions Analyzer")
    st.subheader("Explore and Compare National Carbon Emissions for Climate Action (SDG 13)")
    
    # Introduction
    with st.expander("About This Tool & Dataset"):
        st.write("""
        **Dataset**: Carbon (CO₂) Emissions by Country
        - Contains historical CO₂ emissions data for countries worldwide
        - Metrics: Total emissions (kilotons) and per capita emissions (metric tons)
        - Time range: 1990-2019
        
        **How It Works**:
        1. Select a country to analyze its emissions trajectory
        2. Compare with other countries or global averages
        3. Explore reduction targets and climate action strategies
        
        **Supports SDG 13**: Climate Action by providing data-driven insights for policy-making and awareness.
        """)
    
    # Main analysis section
    col1, col2 = st.columns(2)
    with col1:
        # Use the first country as default if United States is not found
        default_index = 0
        if len(country_list) > 0:
            if "United States" in country_list:
                default_index = country_list.index("United States")
            elif "USA" in country_list:
                default_index = country_list.index("USA")
            
            selected_country = st.selectbox(
                "Select Country", 
                country_list,
                index=default_index
            )
        else:
            st.error("No country data available")
            return
    with col2:
        analysis_year = st.slider(
            "Analysis Year", 
            min_value=1990, 
            max_value=2030,
            value=2020
        )
    
    # Get country data
    country_data = get_country_data(emissions_df, selected_country)
    
    if not country_data.empty:
        # Calculate current emissions
        if analysis_year in country_data['Year'].values:
            current_emissions = country_data[country_data['Year'] == analysis_year]['Per_Capita_CO2_kg'].values[0]
        else:
            current_emissions = calculate_emissions(model, selected_country, analysis_year, emissions_df)
        
        # Global average
        global_avg = emissions_df['Per_Capita_CO2_kg'].mean()
        
        # Display metrics
        st.header(f"{selected_country}'s Emissions Profile")
        col1, col2, col3 = st.columns(3)
        col1.metric(f"{analysis_year} Per Capita Emissions", f"{current_emissions:.1f} kg CO₂")
        col2.metric("Compared to Global Average", 
                   f"{current_emissions/global_avg:.1f}x",
                   "Below average" if current_emissions < global_avg else "Above average")
        col3.metric("Historical Peak", 
                   f"{country_data['Per_Capita_CO2_kg'].max():.1f} kg CO₂",
                   f"in {country_data.loc[country_data['Per_Capita_CO2_kg'].idxmax(), 'Year']}")
    
    # Visualization section
    if not country_data.empty:
        st.header("📊 Emissions Trend Analysis")
        
        # Create historical trend chart
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.lineplot(
            x='Year', 
            y='Per_Capita_CO2_kg', 
            data=country_data,
            marker='o',
            color='#1f77b4',
            label=selected_country,
            ax=ax
        )
        
        # Add global average
        global_avg_line = emissions_df.groupby('Year')['Per_Capita_CO2_kg'].mean().reset_index()
        sns.lineplot(
            x='Year', 
            y='Per_Capita_CO2_kg', 
            data=global_avg_line,
            color='red',
            linestyle='--',
            label='Global Average',
            ax=ax
        )
        
        # Add current year marker
        if analysis_year > country_data['Year'].max():
            ax.axvline(x=analysis_year, color='green', linestyle='--', alpha=0.7)
            ax.text(analysis_year+0.5, current_emissions, 
                   f'Prediction: {current_emissions:.1f} kg', 
                   verticalalignment='bottom')
        
        ax.set_title(f"Per Capita CO₂ Emissions Trend: {selected_country}")
        ax.set_ylabel("kg CO₂ per capita")
        ax.set_xlabel("Year")
        ax.legend()
        st.pyplot(fig)
    
    # Comparison section
    st.header("🌐 Country Comparison")
    # Set default comparison countries that exist in the data
    default_compare = []
    for country in ["China", "India", "Germany", "Brazil", "Canada", "Australia"]:
        if country in country_list:
            default_compare.append(country)
        if len(default_compare) >= 3:
            break
    
    compare_countries = st.multiselect(
        "Compare with other countries", 
        country_list,
        default=default_compare
    )
    
    if compare_countries:
        # Prepare comparison data
        comparison_data = []
        for country in [selected_country] + compare_countries:
            country_emissions = get_country_data(emissions_df, country)
            if not country_emissions.empty:
                latest_year = country_emissions['Year'].max()
                latest_emissions = country_emissions[country_emissions['Year'] == latest_year]['Per_Capita_CO2_kg'].values[0]
                comparison_data.append({
                    'Country': country,
                    'Latest Year': latest_year,
                    'Per Capita CO₂ (kg)': latest_emissions
                })
        
        if comparison_data:
            comparison_df = pd.DataFrame(comparison_data)
            
            # Create comparison chart
            fig2, ax2 = plt.subplots(figsize=(10, 4))
            sns.barplot(
                x='Country', 
                y='Per Capita CO₂ (kg)', 
                data=comparison_df,
                palette="viridis",
                ax=ax2
            )
            ax2.axhline(y=global_avg, color='red', linestyle='--', label='Global Average')
            ax2.set_title("Per Capita Emissions Comparison (Latest Available Data)")
            ax2.set_ylabel("kg CO₂ per capita")
            ax2.legend()
            plt.xticks(rotation=45)
            st.pyplot(fig2)
            
            # Display comparison table
            st.dataframe(comparison_df, use_container_width=True)
    
    # Climate action recommendations
    if not country_data.empty:
        st.header("🌱 Climate Action Recommendations")
        
        # Get reduction targets
        targets = get_reduction_targets(current_emissions)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Emission Reduction Targets")
            for target, value in targets.items():
                reduction_pct = ((current_emissions - value) / current_emissions) * 100
                st.metric(target, f"{value:.1f} kg CO₂", f"-{reduction_pct:.0f}%")
        
        with col2:
            st.subheader("Climate Tips")
            tips = get_climate_tips(selected_country, current_emissions, global_avg)
            for tip in tips:
                st.markdown(f"<div class='tip-box'>{tip}</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("<div class='footer'>", unsafe_allow_html=True)
    st.markdown("**Supporting SDG 13: Climate Action** | Data-driven insights for sustainable development")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()