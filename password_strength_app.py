import streamlit as st
import re
import joblib
import pandas as pd
import random
import string
import math

# Load the trained model
model = joblib.load("password_strength_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Function to generate a strong password
def generate_strong_password(weak_password):
    length = random.randint(12, 16)  # Set length between 12-16 chars
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(chars, k=length))

# Function to calculate password entropy
def calculate_entropy(password):
    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    if charset_size == 0:
        return 0  

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

# Function to extract features from a password
def extract_features(password):
    return [
        len(password),  
        bool(re.search(r"\d", password)),  
        bool(re.search(r"[A-Z]", password)),  
        bool(re.search(r"[a-z]", password)),  
        bool(re.search(r"[^a-zA-Z0-9]", password)),  
    ]   

# Feature column names
feature_columns = ["length", "has_digit", "has_upper", "has_lower", "has_special"]

# Label mapping
label_map = {
    0: "Weak",
    1: "Medium",
    2: "Strong",
    "weak": "Weak",
    "medium": "Medium",
    "strong": "Strong"
}

# Streamlit UI
st.title("🔐 Password Strength Tester")

password = st.text_input("Enter a password:", type="password")

if st.button("Check Strength"):
    if password:
        features = extract_features(password)
        features_df = pd.DataFrame([features], columns=feature_columns)

        prediction = model.predict(features_df)[0]
        strength = label_map.get(prediction, "Unknown")

        # Color mapping for strength
        strength_colors = {
            "Weak": "red",
            "Medium": "orange",
            "Strong": "green"
        }

        strength_color = strength_colors.get(strength, "black")

        # Display the result
        st.markdown(
            f"### 🔍 Predicted Strength: <span style='color:{strength_color};'>{strength}</span>", 
            unsafe_allow_html=True
        )

        # Calculate & display password entropy
        entropy = calculate_entropy(password)
        st.info(f"🧠 Password Entropy: **{entropy} bits**")

        # Suggest a stronger password if it's weak
        if strength == "Weak":
            suggested_password = generate_strong_password(password)
            st.warning(f"⚠ Your password is weak! Try using: **{suggested_password}**") 
    else:
        st.warning("⚠ Please enter a password!")
