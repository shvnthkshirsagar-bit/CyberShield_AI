from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

print("=" * 60)
print("CyberShield AI - Model Training")
print("=" * 60)

# -------------------------------
# Project Paths
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "dataset" / "processed_cyber_threat_dataset.csv"
MODEL_DIR = BASE_DIR / "trained_models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_FILE = MODEL_DIR / "cybershield_model.pkl"

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv(DATASET)

print("\nDataset Loaded Successfully!")
print("Shape:", df.shape)

# -------------------------------
# Features and Label
# -------------------------------
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
# Machine Learning Models
# -------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Support Vector Machine": SVC()
}

best_model = None
best_accuracy = 0
best_model_name = ""

print("\nTraining Models...\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name:<25} Accuracy : {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

# -------------------------------
# Save Best Model
# -------------------------------
# Save Random Forest model
rf_model = models["Random Forest"]

rf_model.fit(X_train, y_train)

joblib.dump(rf_model, MODEL_FILE)

print("\n" + "=" * 60)
print("Final Model : Random Forest")
print("Accuracy :", round(accuracy_score(y_test, rf_model.predict(X_test)) * 100, 2), "%")
print("=" * 60)

print("\nModel Saved Successfully!")
print("Location:", MODEL_FILE)