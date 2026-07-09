import streamlit as st

from visualization import visualization_page
from prediction import prediction_page
from feature_importance import feature_importance_page
from model_performance import model_performance_page
from about import about_page

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🛡️ CyberShield AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Data Visualization",
        "🤖 Threat Prediction",
        "📈 Feature Importance",
        "📉 Model Performance",
        "ℹ️ About"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":

    st.title("🛡️ CyberShield AI")
    st.subheader("AI-Powered Cyber Threat Detection System")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    col1.metric("AI Model", "Ready")
    col2.metric("Dataset", "Loaded")
    col3.metric("Status", "Online")

    st.markdown("---")

    st.header("Project Overview")

    st.write("""
CyberShield AI is an Artificial Intelligence based Cyber Threat Detection System.

### Features

✅ Machine Learning Based Threat Detection

✅ Detects Normal and Malicious Traffic

✅ Feature Importance Analysis

✅ Model Performance Evaluation

✅ Interactive Prediction Dashboard
""")

    st.markdown("---")

    st.header("Workflow")

    st.write("""
1. Load Dataset

2. Preprocess Data

3. Train Machine Learning Model

4. Evaluate Model

5. Predict Cyber Threats
""")

    st.success("Project Ready Successfully")

elif page == "📊 Data Visualization":
    visualization_page()

# -----------------------------
# Threat Prediction
# -----------------------------

elif page == "🤖 Threat Prediction":
    prediction_page()

# -----------------------------
# Feature Importance
# -----------------------------
elif page == "📈 Feature Importance":
    feature_importance_page()

# -----------------------------
# Model Performance
# -----------------------------
elif page == "📉 Model Performance":
    model_performance_page()

# -----------------------------
# About
# -----------------------------
elif page == "ℹ️ About":
    about_page()