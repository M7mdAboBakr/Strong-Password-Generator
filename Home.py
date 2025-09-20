import streamlit as st
import random

def strong_password_generator(password_length=16): 
    all_things = 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*1234567890'
    all_things += all_things.upper()
    return ''.join(random.sample(all_things, password_length))

# Streamlit UI
st.set_page_config(page_title="Strong Password Generator", page_icon="🔐", layout="centered")

st.title("🔐 Strong Password Generator")
st.write("Generate secure passwords with lowercase, uppercase, numbers, and special characters.")

# Password length slider
length = st.slider("🔢 Choose password length", min_value=8, max_value=50, value=16, step=1)

# Generate button
if st.button("⚡ Generate Password"):
    password = strong_password_generator(length)
    
    st.success("✅ Your strong password has been generated:")
    st.code(password, language="")

    # Copy-to-clipboard
    st.download_button("📋 Copy Password", password, file_name="password.txt", mime="text/plain")

    # Password strength tips
    if length < 12:
        st.warning("⚠️ Your password is a bit short. Consider using at least 12 characters.")
    elif length >= 20:
        st.info("💪 Super strong password length! Good choice.")
