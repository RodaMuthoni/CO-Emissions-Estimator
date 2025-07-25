# -*- coding: utf-8 -*-
import streamlit as st

@st.cache_data
def circular_image(image_path, width=140):
    # Display the image using Streamlit with error handling
    try:
        st.image(image_path, width=width, use_container_width=False)
    except:
        st.markdown("👤")  # Fallback emoji

# Handle logo with error handling
try:
    st.logo("Images/team.png")
except:
    pass

try:
    st.image("Images/team.png",width=145)
except:
    st.markdown("👥 **Team Photo**")
st.title("Meet the Team Behind the Suite")
st.write("""
    This project was developed by a team of dedicated students from Power Learn Project, with a passion for creating tools that improve academic experiences.
    Our team consists of:
    """)

st.write("---")
# Display each developer's profile picture and details
circular_image("Images/mike.jpg")  # Replace with your image path
st.subheader("Michael Randa")
st.write("Role: Lead Developer | Specializes in backend development and Machine Learning Algorithms.")

st.markdown("""
I am a results-oriented individual with a strong work ethic. I'm also a team player and have excellent communication skills and passionate about software development, data science, machine learning and have a strong foundation in Java, Python, data structures & algorithms, software engineering principles and practical statistics.
""")

st.write("""Reach out through:""")
st.write("""📧 Email: michaelranda95@gmail.com""")
st.write("""GitHub: https://github.com/MikeMitch88""")
st.write("""LinkedIn: https://www.linkedin.com/in/www.linkedin.com/in/michael-randa

""")
            
st.markdown("""
I'm constantly exploring the latest advancements in AI and technology. This proactive approach keeps me ahead of the curve, eager to contribute to what's next.
""")

# Developer 2
circular_image("Images/val.jpeg")
st.subheader("Sabulkong Valentine")
st.write("Role: Project Manager | Specializes in team coordination, task tracking, and agile workflows.")
st.markdown("""
I’m passionate about building strong, collaborative teams and delivering products on time. With a background in IT and leadership, I guide our development sprints, manage task prioritization, and ensure communication flows smoothly between departments.
""")
st.write("Reach out through:")
st.write("📧 Email: sabulkongvalentine@gmail.com")
st.write("GitHub: https://github.com/sabulkong")
st.write("LinkedIn: https://www.linkedin.com/in/valentine-jerono-1b8802359/")

# Developer 3
circular_image("Images/roda.png")
st.subheader("Roda Muthoni")
st.write("Role: Data Scientist | Specializes in data analysis, visualization, and model validation.")
st.markdown("""
As a data enthusiast, I enjoy transforming raw datasets into powerful insights. I'm skilled in exploratory data analysis, model tuning, and generating visual reports that tell meaningful stories. I ensure that the numbers behind our app are robust and accurate.
""")
st.write("Reach out through:")
st.write("📧 Email: ")
st.write("GitHub: https://github.com/dev3")
st.write("LinkedIn: https://www.linkedin.com/in/dev3")

# Developer 4
circular_image("Images/rose.jpeg")
st.subheader("Rose Onyango")
st.write("Role: Frontend Developer | Specializes in UI/UX Design and React.")
st.markdown("""
Creative and detail-driven, I bring user interfaces to life with React and modern frontend tools. I believe in making user experiences beautiful, fast, and intuitive. I work closely with the backend team to ensure seamless integration and responsive design across devices.
""")


st.write("Reach out through:")
st.write("📧 Email: roseonyango44@gmail.com")
st.write("GitHub: https://github.com/RosetheOnly")
st.write("LinkedIn: https://www.linkedin.com/in/rose-onyango-b252b2119/")


# Developer 5
circular_image("Images/nick.png")
st.subheader("Nickson Onsombi")
st.write("Role: QA & DevOps Coordinator | Focuses on quality assurance and deployment pipelines.")
st.markdown("""
My passion lies in ensuring that every feature works flawlessly before it reaches the user. I handle automated testing, monitor CI/CD pipelines, and help deploy our app reliably to cloud platforms. I advocate for clean code, efficiency, and maintainability.
""")

st.write("Reach out through:")
st.write("📧 Email: nicksononsombi515@gmail.com")
st.write("GitHub: https://github.com/Nicky123-sud")
st.write("LinkedIn: https://www.linkedin.com/in/nickson-nyaboga-7977222a0/")


# Simple Footer

st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 14px; padding: 10px; color: #666;">
    <p><strong>🌿 Sustainability Dashboard</strong></p>
    <p>
        Informing and inspiring change for a sustainable future. 
        Together, we can make a difference. 🌏
    </p>
    <p>© 2025 | Created with ❤️ and responsibility.</p>
</div>
""", unsafe_allow_html=True)
