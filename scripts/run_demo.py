import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

CLEAN_FILE = "data/processed/cleaned_bug_reports.csv"
INDEX_FILE = "models/vector_index/faiss_index.bin"

def run_demo(new_bugs):
    df = pd.read_csv(CLEAN_FILE)
    texts = df["clean_text"].tolist()
    
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(texts, convert_to_numpy=True)
    
    index = faiss.read_index(INDEX_FILE)
    
    new_embeddings = model.encode(new_bugs, convert_to_numpy=True)
    
    for i, vec in enumerate(new_embeddings):
        D, I = index.search(np.array([vec]), k=3)
        print(f"\nNew bug: {new_bugs[i]}")
        print("Top matches:")
        for idx, dist in zip(I[0], D[0]):
            print(f"- {texts[idx]} (distance={dist:.2f})")

if __name__ == "__main__":
    sample_bugs = [
        "Login page crashes when clicking submit",
        "Payment fails due to timeout"
    ]
    run_demo(sample_bugs)