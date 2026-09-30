"""
config.py

Root configuration file for Duplicate Defect Finder & Bug Report Enhancer.

This file stores all important constants and configuration values
used across the project to avoid hardcoding values in multiple files.
"""

# =========================
# DATA PATHS
# =========================
# Paths for raw and processed datasets

RAW_DATA_PATH = "data/raw/bugzilla_raw.csv"

PROCESSED_DATA_PATH = "data/processed/cleaned_bug_reports.csv"

# Alias kept intentionally to avoid breaking imports
CLEANED_DATASET_PATH = PROCESSED_DATA_PATH


# =========================
# MODEL SETTINGS
# =========================
# Embedding model used for generating text embeddings

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Embedding vector dimension for MiniLM model
EMBEDDING_DIMENSION = 384


# =========================
# VECTOR INDEX SETTINGS
# =========================
# Paths for FAISS index and metadata

FAISS_INDEX_PATH = "models/vector_index/faiss_index.bin"
METADATA_PATH = "models/vector_index/metadata.pkl"


# =========================
# SIMILARITY SEARCH SETTINGS
# =========================

TOP_K_RESULTS = 5


# =========================
# SIMILARITY THRESHOLDS
# =========================
# Thresholds for duplicate detection logic

DUPLICATE_THRESHOLD = 0.90
POSSIBLE_DUPLICATE_THRESHOLD = 0.75


# =========================
# API CONFIG
# =========================
# FastAPI server configuration

import os

API_HOST = "0.0.0.0"
API_PORT = int(os.getenv("PORT", "8000"))


# =========================
# CLUSTER SETTINGS
# =========================
# Settings for clustering similar bug reports

CLUSTER_ALGORITHM = "DBSCAN"
DBSCAN_EPS = 0.5
DBSCAN_MIN_SAMPLES = 5


# =========================
# LOGGING SETTINGS
# =========================

LOG_LEVEL = "INFO"