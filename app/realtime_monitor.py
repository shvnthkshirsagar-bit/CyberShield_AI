import streamlit as st
import psutil
import pandas as pd
import plotly.express as px
import random
from streamlit_autorefresh import st_autorefresh


def realtime_monitor_page():

    st.set_page_config(
        page_title="Real-Time Monitoring",
        page_icon="🛡️",
        layout="wide"
    )

    # Refresh every 3 seconds
    st_autorefresh(interval=3000, key="refresh")

    st.title("🛡️ CyberShield AI - Real-Time Monitoring")

    # ==============================
    # System Metrics
    # ==============================
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    col1, col2, col3 = st.columns(3)

    col1.metric("💻 CPU Usage", f"{cpu}%")
    col2.metric("🧠 RAM Usage", f"{ram}%")
    col3.metric("💾 Disk Usage", f"{disk}%")

    st.divider()

    # ==============================
    # Threat Metrics
    # ==============================
    c1, c2, c3 = st.columns(3)

    c1.metric("🚨 Threats Detected", random.randint(10, 100))
    c2.metric("📦 Packets Processed", random.randint(5000, 15000))
    c3.metric("⚠️ High Risk Alerts", random.randint(1, 20))

    st.divider()

    # ==============================
    # Live Traffic Chart
    # ==============================
    traffic = pd.DataFrame({
        "Time": list(range(20)),
        "Packets": [random.randint(50, 200) for _ in range(20)]
    })

    fig = px.line(
        traffic,
        x="Time",
        y="Packets",
        title="📈 Live Network Traffic"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==============================
    # Recent Alerts
    # ==============================
    alerts = pd.DataFrame({
        "Source IP": [
            "192.168.1.5",
            "10.0.0.2",
            "172.16.1.20"
        ],
        "Prediction": [
            "DDoS",
            "Normal",
            "Port Scan"
        ],
        "Risk": [
            "High",
            "Low",
            "Medium"
        ]
    })

    st.subheader("📋 Recent Alerts")
    st.dataframe(alerts, use_container_width=True)