# tests/test_faiss_index.py
import faiss
import pickle
from config import FAISS_INDEX_PATH, METADATA_PATH

def main():
    # Test FAISS index
    try:
        index = faiss.read_index(FAISS_INDEX_PATH)
        print("FAISS index loaded successfully.")
        print("Number of vectors in index:", index.ntotal)
    except Exception as e:
        print("Error loading FAISS index:", e)

    # Test metadata
    try:
        with open(METADATA_PATH, "rb") as f:
            df = pickle.load(f)
        print("Metadata loaded successfully.")
        print("Number of entries in metadata:", len(df))
    except Exception as e:
        print("Error loading metadata:", e)

if __name__ == "__main__":
    main()