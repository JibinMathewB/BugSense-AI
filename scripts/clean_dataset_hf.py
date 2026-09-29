# scripts/clean_dataset_hf.py
import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# Load raw dataset
df = pd.read_csv("data/raw/bugzilla_raw.csv")

# Select important columns
df = df[['Bug ID', 'Short Description', 'Severity Label']]

# Rename columns
df.columns = ['bug_id', 'title', 'description']

# Remove duplicates & empty rows
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Reduce size to ~15k for hackathon
df = df.sample(n=min(15000, len(df)), random_state=42)

# Save cleaned dataset
df.to_csv("data/processed/cleaned_bug_reports.csv", index=False)

print("✅ Cleaned dataset saved to data/processed/cleaned_bug_reports.csv")