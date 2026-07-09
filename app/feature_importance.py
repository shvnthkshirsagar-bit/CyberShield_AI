from pathlib import Path
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


def feature_importance_page():

    st.title("📈 Feature Importance")

    BASE_DIR = Path(__file__).resolve().parent.parent

    MODEL_PATH = BASE_DIR / "trained_models" / "cybershield_model.pkl"
    DATASET_PATH = BASE_DIR / "dataset" / "processed_cyber_threat_dataset.csv"

    try:
        model = joblib.load(MODEL_PATH)
        df = pd.read_csv(DATASET_PATH)

    except Exception as e:
        st.error(f"Error: {e}")
        return

    X = df.drop("Label", axis=1)

    if hasattr(model, "feature_importances_"):

        importance = pd.DataFrame({
            "Feature": X.columns,
            "Importance": model.feature_importances_
        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        )

        st.dataframe(importance, use_container_width=True)

        fig = px.bar(
            importance,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Feature Importance"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("This model does not support feature importance.")