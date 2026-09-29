"""
Project-wide constants used across AI pipeline, scripts, and services.
"""

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Embedding dimension (MiniLM)
EMBEDDING_DIMENSION = 384


# Similarity thresholds
DUPLICATE_THRESHOLD = 0.90
POSSIBLE_DUPLICATE_THRESHOLD = 0.75


# Vector search
TOP_K_RESULTS = 5


# Dataset paths
RAW_DATA_PATH = "data/raw/bugzilla_raw.csv"
CLEAN_DATA_PATH = "data/processed/cleaned_bug_reports.csv"


# FAISS index paths
FAISS_INDEX_PATH = "models/vector_index/faiss_index.bin"
METADATA_PATH = "models/vector_index/metadata.pkl"