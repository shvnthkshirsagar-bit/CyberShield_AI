from pathlib import Path
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


def prediction_page():

    st.title("🤖 AI Cyber Threat Prediction")

    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_PATH = BASE_DIR / "trained_models" / "cybershield_model.pkl"

    try:
        model = joblib.load(MODEL_PATH)
        st.success("✅ AI Model Loaded Successfully")
    except Exception as e:
        st.error(f"❌ Unable to load model.\n\n{e}")
        st.stop()

    tab1, tab2 = st.tabs(
        [
            "📝 Manual Prediction",
            "📂 Batch Prediction"
        ]
    )

    #########################################################
    # Batch Prediction
    #########################################################

    with tab2:

        st.header("📂 Upload Network Traffic Dataset")

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.success("✅ Dataset Uploaded Successfully")

            st.subheader("Dataset Preview")
            st.dataframe(df.head())

            required_columns = [
                "Protocol",
                "Packet_Size",
                "Duration",
                "Failed_Logins",
                "Login_Attempts",
                "Data_Transferred_MB",
                "Firewall_Alerts",
                "IDS_Alerts",
                "Malware_Detected",
                "Traffic_Type"
            ]

            missing = [
                col
                for col in required_columns
                if col not in df.columns
            ]

            if missing:
                st.error(
                    f"Missing Required Columns:\n{missing}"
                )
                st.stop()

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

            df["Protocol"] = (
                df["Protocol"]
                .replace(protocol_map)
            )

            df["Traffic_Type"] = (
                df["Traffic_Type"]
                .replace(traffic_map)
            )

            if st.button(
                "🚀 Predict Uploaded Dataset"
            ):

                predictions = model.predict(df)

                df["Prediction"] = predictions

                total = len(df)

                threats = (
                    df["Prediction"] == 1
                ).sum()

                normal = (
                    df["Prediction"] == 0
                ).sum()

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Total Records",
                    total
                )

                c2.metric(
                    "Normal",
                    normal
                )

                c3.metric(
                    "Threat",
                    threats
                )

                st.markdown("---")

                pie = px.pie(
                    values=[normal, threats],
                    names=[
                        "Normal",
                        "Threat"
                    ],
                    title="Threat Distribution"
                )

                st.plotly_chart(
                    pie,
                    use_container_width=True
                )

                bar = px.bar(
                    x=["Normal", "Threat"],
                    y=[normal, threats],
                    title="Prediction Summary"
                )

                st.plotly_chart(
                    bar,
                    use_container_width=True
                )

                st.dataframe(df)

                csv = df.to_csv(
                    index=False
                )

                st.download_button(
                    "📥 Download Results",
                    csv,
                    "prediction_results.csv",
                    "text/csv"
                )

    #########################################################
    # Manual Prediction
    #########################################################

    with tab1:

        st.header("📝 Manual Prediction")

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

        if st.button("🔍 Predict Network Traffic"):

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

            if prediction == 0:
                result = "Normal"
                color = "success"
                normal = 1
                threat = 0
            else:
                result = "Cyber Threat"
                color = "error"
                normal = 0
                threat = 1

            st.markdown("---")

            if color == "success":
                st.success("🟢 Normal Network Traffic")
            else:
                st.error("🚨 Cyber Threat Detected")

            c1, c2, c3 = st.columns(3)

            c1.metric("Prediction", result)
            c2.metric("Normal", normal)
            c3.metric("Threat", threat)

            chart = pd.DataFrame({
                "Category": ["Normal", "Threat"],
                "Count": [normal, threat]
            })

            fig1 = px.pie(
                chart,
                names="Category",
                values="Count",
                title="Prediction Distribution"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

            fig2 = px.bar(
                chart,
                x="Category",
                y="Count",
                title="Threat Analysis"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

            st.subheader("Input Features")

            st.dataframe(sample)

            st.info(
                "💡 Tip: Use the 'Batch Prediction' tab to upload an entire network traffic dataset and analyze all records at once."
            )