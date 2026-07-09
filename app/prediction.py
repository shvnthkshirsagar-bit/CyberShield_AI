from pathlib import Path
import streamlit as st
import pandas as pd
import joblib


def prediction_page():

    st.title("🤖 AI Cyber Threat Prediction")

    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_PATH = BASE_DIR / "trained_models" / "cybershield_model.pkl"

    try:
        model = joblib.load(MODEL_PATH)
        st.success("✅ Model Loaded Successfully")

    except Exception:
        st.error("❌ Model not found!")
        return

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        protocol = st.selectbox(
            "Protocol",
            ["TCP", "UDP", "ICMP"]
        )

        packet_size = st.number_input(
            "Packet Size",
            min_value=0,
            value=500
        )

        duration = st.number_input(
            "Duration",
            min_value=0,
            value=10
        )

        failed_logins = st.number_input(
            "Failed Logins",
            min_value=0,
            value=0
        )

        login_attempts = st.number_input(
            "Login Attempts",
            min_value=0,
            value=1
        )

    with col2:

        data_transferred = st.number_input(
            "Data Transferred (MB)",
            min_value=0.0,
            value=15.0
        )

        firewall_alerts = st.number_input(
            "Firewall Alerts",
            min_value=0,
            value=0
        )

        ids_alerts = st.number_input(
            "IDS Alerts",
            min_value=0,
            value=0
        )

        malware_detected = st.selectbox(
            "Malware Detected",
            [0, 1]
        )

        traffic = st.selectbox(
            "Traffic Type",
            [
                "Normal",
                "DDoS",
                "Malware",
                "Phishing",
                "Ransomware"
            ]
        )

    protocol_map = {
        "ICMP": 0,
        "TCP": 1,
        "UDP": 2
    }

    traffic_map = {
        "DDoS": 0,
        "Malware": 1,
        "Normal": 2,
        "Phishing": 3,
        "Ransomware": 4
    }

    if st.button("🔍 Predict"):

        sample = pd.DataFrame([{
            "Protocol": protocol_map[protocol],
            "Packet_Size": packet_size,
            "Duration": duration,
            "Failed_Logins": failed_logins,
            "Login_Attempts": login_attempts,
            "Data_Transferred_MB": data_transferred,
            "Firewall_Alerts": firewall_alerts,
            "IDS_Alerts": ids_alerts,
            "Malware_Detected": malware_detected,
            "Traffic_Type": traffic_map[traffic]
        }])

        prediction = model.predict(sample)[0]

        st.markdown("---")

        if prediction == 0:
            st.success("🟢 Normal Network Traffic")
        else:
            st.error("🚨 Cyber Threat Detected")