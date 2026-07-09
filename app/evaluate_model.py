from pathlib import Path
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

print("=" * 60)
print("CyberShield AI - Model Evaluation")
print("=" * 60)

# -------------------------------
# Project Paths
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "dataset" / "processed_cyber_threat_dataset.csv"
MODEL = BASE_DIR / "trained_models" / "cybershield_model.pkl"

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv(DATASET)

X = df.drop("Label", axis=1)
y = df["Label"]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load(MODEL)

# -------------------------------
# Prediction
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Metrics
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nAccuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall   :", round(recall * 100, 2), "%")
print("F1 Score :", round(f1 * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# -------------------------------
# Confusion Matrix
# -------------------------------
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Normal", "Threat"]
)

disp.plot(cmap="Blues")

plt.title("CyberShield AI - Confusion Matrix")

plt.show()