import streamlit as st
import pandas as pd
import hashlib
import os

USER_DB = "users.csv"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    df = pd.read_csv(USER_DB)
    return dict(zip(df['username'], df['password']))

def save_user(username, password_hash):
    if os.path.exists(USER_DB):
        df = pd.read_csv(USER_DB)
        if username in df['username'].values:
            return False
        df = pd.concat([df, pd.DataFrame([{'username': username, 'password': password_hash}])], ignore_index=True)
    else:
        df = pd.DataFrame([{'username': username, 'password': password_hash}])
    df.to_csv(USER_DB, index=False)
    return True

def login_signup():
    st.sidebar.header("🔒 Authentication")
    auth_mode = st.sidebar.radio("Choose mode", ["Login", "Sign Up"])
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    users = load_users()

    if auth_mode == "Login":
        if st.sidebar.button("Login"):
            if username in users and users[username] == hash_password(password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.sidebar.success(f"Welcome, {username}!")
            else:
                st.sidebar.error("Invalid credentials")
    else:
        if st.sidebar.button("Sign Up"):
            if username in users:
                st.sidebar.error("Username already exists")
            elif username and password:
                if save_user(username, hash_password(password)):
                    st.sidebar.success("Account created! Please log in.")
                else:
                    st.sidebar.error("Error creating account")
            else:
                st.sidebar.error("Please enter username and password")

    if not st.session_state.get("authenticated", False):
        st.stop()
