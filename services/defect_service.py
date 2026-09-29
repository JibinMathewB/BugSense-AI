from clustering.cluster_engine import ClusterEngine
from services.decision_engine import classify_bug
from sentence_transformers import SentenceTransformer

# Load embedding model and clustering engine once
model = SentenceTransformer("all-MiniLM-L6-v2")
engine = ClusterEngine()

def process_new_bugs(new_bugs, existing_bugs):
    """
    Accepts new bug reports and existing bug reports.
    Returns cluster info + status + confidence.
    """
    # Combine existing + new bugs
    all_bugs = existing_bugs + new_bugs
    embeddings = model.encode(all_bugs)

    # Cluster all embeddings
    labels = engine.cluster(embeddings)

    # Only look at new bug labels
    new_labels = labels[-len(new_bugs):]

    results = []
    for i, label in enumerate(new_labels):
        # Assign a fake similarity score for decision logic
        score = 1.0 if label != -1 else 0.5
        status, confidence = classify_bug(score)
        results.append({
            "bug": new_bugs[i],
            "cluster": int(label),
            "status": status,
            "confidence": confidence
        })

    return results