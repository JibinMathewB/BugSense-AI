# scripts/load_bugzilla.py
from datasets import load_dataset
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

# Load dataset
dataset = load_dataset("AliArshad/Bugzilla_Eclipse_Bug_Reports_Dataset", split="train")

# Convert to pandas
df = pd.DataFrame(dataset)

# Save CSV
df.to_csv("data/raw/bugzilla_raw.csv", index=False)

print("✅ Dataset saved to data/raw/bugzilla_raw.csv")