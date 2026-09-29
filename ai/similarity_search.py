import numpy as np


class SimilaritySearch:
    """
    Performs similarity search on the FAISS index to find
    the most similar bug reports.
    """

    def __init__(self, index, metadata):
        """
        Args:
            index: Loaded FAISS index
            metadata: List of bug report metadata corresponding to vectors
        """
        self.index = index
        self.metadata = metadata

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        """
        Search the FAISS index for the most similar bug reports.

        Args:
            query_embedding: embedding vector for the new bug report
            top_k: number of similar bugs to retrieve

        Returns:
            list of similar bug reports with similarity scores
        """

        # Ensure correct dtype for FAISS
        if query_embedding.dtype != np.float32:
            query_embedding = query_embedding.astype(np.float32)

        # FAISS expects 2D array
        query_embedding = np.expand_dims(query_embedding, axis=0)

        # Ensure top_k limit
        top_k = min(top_k, 5)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):

            # FAISS returns -1 if nothing found
            if idx == -1:
                continue

            # Safety check
            if idx >= len(self.metadata):
                continue

            bug = self.metadata[idx]

            # support metadata entries that are either dicts or simple ids
            if isinstance(bug, dict):
                bug_id = bug.get("bug_id", "unknown")
                title = bug.get("title", "")
            else:
                # metadata may be a plain integer id
                bug_id = bug
                title = ""

            results.append({
                "bug_id": bug_id,
                "title": title,
                "score": float(score)
            })

        return results