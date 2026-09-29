import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

# Load FAISS index
index = faiss.read_index("models/vector_index/faiss_index.bin")

# Load metadata
with open("models/vector_index/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Example bug report
new_bug = "App crashes when clicking submit"
embedding = model.encode([new_bug])
D, I = index.search(np.array(embedding), k=5)

print("Top 5 duplicate bug IDs for:", new_bug)
for idx in I[0]:
    bug_id = metadata[idx]
    print("-", bug_id)