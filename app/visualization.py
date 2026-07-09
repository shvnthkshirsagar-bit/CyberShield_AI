from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px


def visualization_page():

    st.title("📊 CyberShield AI - Data Visualization")

    BASE_DIR = Path(__file__).resolve().parent.parent
    DATASET = BASE_DIR / "dataset" / "processed_cyber_threat_dataset.csv"

    try:
        df = pd.read_csv(DATASET)

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return

    st.success("✅ Dataset Loaded Successfully")

    # ----------------------------
    # Dataset Preview
    # ----------------------------

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    # ----------------------------
    # Dataset Shape
    # ----------------------------

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.markdown("---")

    # ----------------------------
    # Label Distribution
    # ----------------------------

    st.subheader("🛡️ Normal vs Threat")

    fig = px.pie(
        df,
        names=df["Label"].map({0: "Normal", 1: "Threat"}),
        title="Traffic Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Protocol Distribution
    # ----------------------------

    st.subheader("📡 Protocol Distribution")

    fig = px.histogram(
        df,
        x="Protocol",
        color="Protocol",
        text_auto=True
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Traffic Type
    # ----------------------------

    st.subheader("🌐 Traffic Type Distribution")

    fig = px.histogram(
        df,
        x="Traffic_Type",
        color="Traffic_Type",
        text_auto=True
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Packet Size
    # ----------------------------

    st.subheader("📦 Packet Size")

    fig = px.box(
        df,
        x="Traffic_Type",
        y="Packet_Size",
        color="Traffic_Type"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Failed Logins
    # ----------------------------

    st.subheader("🔐 Failed Logins")

    fig = px.scatter(
        df,
        x="Login_Attempts",
        y="Failed_Logins",
        color="Traffic_Type",
        size="Packet_Size"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Firewall Alerts
    # ----------------------------

    st.subheader("🔥 Firewall Alerts")

    fig = px.bar(
        df,
        x="Traffic_Type",
        y="Firewall_Alerts",
        color="Traffic_Type"
    )

    st.plotly_chart(fig, use_container_width=True)