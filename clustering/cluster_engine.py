from sklearn.cluster import DBSCAN
import numpy as np


class ClusterEngine:
    """
    Performs clustering on bug embeddings using DBSCAN.
    Clusters represent groups of similar defects.
    """

    def __init__(self, eps: float = 0.3, min_samples: int = 2):
        """
        Initialize clustering model.

        Args:
            eps: Maximum distance between two samples
            min_samples: Minimum samples required to form a cluster
        """

        self.model = DBSCAN(
            eps=eps,
            min_samples=min_samples,
            metric="cosine"
        )

    def cluster(self, embeddings):
        """
        Perform clustering on embeddings.

        Args:
            embeddings: list or numpy array of embeddings

        Returns:
            list of cluster labels
        """

        if embeddings is None or len(embeddings) == 0:
            return []

        embeddings = np.array(embeddings).astype(np.float32)

        labels = self.model.fit_predict(embeddings)

        return labels.tolist()

    def get_cluster_ids(self, labels):
        """
        Convert numeric cluster labels into readable cluster IDs.

        Example:
            [-1,0,0,1] -> ["noise","cluster_0","cluster_0","cluster_1"]
        """

        cluster_ids = []

        for label in labels:

            if label == -1:
                cluster_ids.append("noise")
            else:
                cluster_ids.append(f"cluster_{label}")

        return cluster_ids