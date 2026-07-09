import streamlit as st


def about_page():

    st.title("ℹ️ About CyberShield AI")

    st.markdown("---")

    st.header("🛡️ Project Description")

    st.write("""
CyberShield AI is an Artificial Intelligence based Cyber Threat Detection System.

The system analyzes network traffic and predicts whether the traffic is:

- ✅ Normal
- 🚨 DDoS Attack
- 🚨 Malware
- 🚨 Phishing
- 🚨 Ransomware

using Machine Learning algorithms.
""")

    st.markdown("---")

    st.header("💻 Technologies Used")

    st.write("""
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib
""")

    st.markdown("---")

    st.header("📂 Project Modules")

    st.write("""
✔ Data Preprocessing

✔ Model Training

✔ Model Evaluation

✔ Threat Prediction

✔ Feature Importance

✔ Model Performance Dashboard
""")

    st.markdown("---")

    st.header("🚀 Future Improvements")

    st.write("""
- Real-time Network Monitoring

- Live Packet Capture

- Deep Learning Models

- Intrusion Detection Integration

- Cloud Deployment
""")

    st.markdown("---")

    st.success("CyberShield AI Version 1.0")