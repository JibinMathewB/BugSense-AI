from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingEngine:
    """
    Handles loading the embedding model and generating embeddings
    for bug reports.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Load the sentence transformer model once.
        """

        # Force CPU to avoid GPU dependency issues
        self.model = SentenceTransformer(model_name, device="cpu")

    def encode_texts(self, texts: list[str], batch_size: int = 32) -> np.ndarray:
        """
        Convert list of bug texts into embeddings.

        Args:
            texts: List of bug report texts
            batch_size: Batch size for faster encoding

        Returns:
            numpy array of embeddings
        """

        if not texts:
            raise ValueError("Input text list is empty.")

        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        # Ensure FAISS compatible dtype
        return embeddings.astype(np.float32)

    def encode_query(self, text: str) -> np.ndarray:
        """
        Encode a single bug report for similarity search.
        """

        if not isinstance(text, str) or text.strip() == "":
            raise ValueError("Query text cannot be empty.")

        embedding = self.model.encode(
            [text],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        # Return single vector
        return embedding[0].astype(np.float32)