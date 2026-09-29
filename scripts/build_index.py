# scripts/build_index.py
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
import os

os.makedirs("models/vector_index", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_bug_reports.csv")

# Combine text fields
texts = (df['title'] + " " + df['description']).tolist()

# Load model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(texts, show_progress_bar=True)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "models/vector_index/faiss_index.bin")

# Save metadata
with open("models/vector_index/metadata.pkl", "wb") as f:
    pickle.dump(df['bug_id'].tolist(), f)

print("✅ FAISS index and metadata saved to models/vector_index/")