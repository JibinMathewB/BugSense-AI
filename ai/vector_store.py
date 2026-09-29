import faiss
import numpy as np
import pickle
import os


class VectorStore:
    """
    Handles creation, storage, and loading of the FAISS vector index
    used for bug similarity search.
    """

    def __init__(self, dimension: int):
        """
        Initialize FAISS index.

        Args:
            dimension: embedding dimension (MiniLM = 384)
        """
        self.dimension = dimension

        # Inner Product index (cosine similarity when embeddings normalized)
        self.index = faiss.IndexFlatIP(dimension)

    def add_embeddings(self, embeddings: np.ndarray):
        """
        Add embeddings to the FAISS index.

        Args:
            embeddings: numpy array of shape (n_samples, dimension)
        """

        if embeddings is None or len(embeddings) == 0:
            raise ValueError("Embeddings array is empty.")

        if embeddings.dtype != np.float32:
            embeddings = embeddings.astype(np.float32)

        if embeddings.shape[1] != self.dimension:
            raise ValueError(
                f"Embedding dimension mismatch. Expected {self.dimension}, got {embeddings.shape[1]}"
            )

        self.index.add(embeddings)

    def save_index(self, index_path: str):
        """
        Save FAISS index to disk.
        """

        os.makedirs(os.path.dirname(index_path), exist_ok=True)

        faiss.write_index(self.index, index_path)

    def save_metadata(self, metadata, metadata_path: str):
        """
        Save bug metadata so we can map FAISS results back to bug reports.
        """

        os.makedirs(os.path.dirname(metadata_path), exist_ok=True)

        with open(metadata_path, "wb") as f:
            pickle.dump(metadata, f)

    @staticmethod
    def load(index_path: str, metadata_path: str):
        """
        Load FAISS index and metadata from disk.
        """

        if not os.path.exists(index_path):
            raise FileNotFoundError(f"FAISS index not found at {index_path}")

        if not os.path.exists(metadata_path):
            raise FileNotFoundError(f"Metadata file not found at {metadata_path}")

        index = faiss.read_index(index_path)

        with open(metadata_path, "rb") as f:
            metadata = pickle.load(f)

        return index, metadata