from pathlib import Path
import pandas as pd
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("CyberShield AI - Data Preprocessing")
print("=" * 60)

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset paths
INPUT_FILE = BASE_DIR / "dataset" / "cyber_threat_dataset.csv"
OUTPUT_FILE = BASE_DIR / "dataset" / "processed_cyber_threat_dataset.csv"

# Check if dataset exists
if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Dataset not found:\n{INPUT_FILE}")

# Load dataset
df = pd.read_csv(INPUT_FILE)

print("\nDataset Loaded Successfully!")
print("Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

print("Shape after cleaning:", df.shape)

# Encode categorical columns
encoder = LabelEncoder()

categorical_columns = [
    "Protocol",
    "Traffic_Type"
]

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

# Remove IP columns
df.drop(
    columns=["Source_IP", "Destination_IP"],
    inplace=True
)

# Save processed dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\nProcessed dataset saved successfully!")
print("Location:", OUTPUT_FILE)