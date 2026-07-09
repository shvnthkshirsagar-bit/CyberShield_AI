import streamlit as st
print("✅ NEW model_performance.py LOADED")
st.write("✅ New model_performance.py is loaded")
from pathlib import Path
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def model_performance_page():

    st.success("✅ This is the new Model Performance page")

    st.title("📉 Model Performance")

    BASE_DIR = Path(__file__).resolve().parent.parent

    MODEL_PATH = BASE_DIR / "trained_models" / "cybershield_model.pkl"
    DATASET_PATH = BASE_DIR / "dataset" / "processed_cyber_threat_dataset.csv"

    try:
        model = joblib.load(MODEL_PATH)
        df = pd.read_csv(DATASET_PATH)

    except Exception as e:
        st.error(f"Error: {e}")
        return

    # ...rest of your code...
    X = df.drop("Label", axis=1)
    y = df["Label"]

    predictions = model.predict(X)

    accuracy = accuracy_score(y, predictions)
    precision = precision_score(y, predictions)
    recall = recall_score(y, predictions)
    f1 = f1_score(y, predictions)

    st.subheader("📊 Performance Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Accuracy", f"{accuracy*100:.2f}%")
        st.metric("Precision", f"{precision*100:.2f}%")

    with col2:
        st.metric("Recall", f"{recall*100:.2f}%")
        st.metric("F1 Score", f"{f1*100:.2f}%")

    st.markdown("---")

    st.subheader("Confusion Matrix")

    cm = confusion_matrix(y, predictions)

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.imshow(cm)

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    for i in range(len(cm)):
        for j in range(len(cm)):
            ax.text(j, i, str(cm[i][j]), ha="center", va="center")

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Classification Report")

    report = classification_report(y, predictions)

    st.text(report)