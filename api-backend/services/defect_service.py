from ai.embedding_engine import EmbeddingEngine
from ai.similarity_search import SimilaritySearch
from ai.vector_store import VectorStore
from enhancer.report_enhancer import enhance_bug_report
from clustering.cluster_utils import generate_confidence
import config


# ------------------------------------
# Load AI components once at startup
# ------------------------------------

embedding_engine = EmbeddingEngine(config.EMBEDDING_MODEL_NAME)

# Load FAISS index and metadata
index, metadata = VectorStore.load(
    config.FAISS_INDEX_PATH,
    config.METADATA_PATH
)

similarity_search = SimilaritySearch(index, metadata)


def analyze_bug(request):
    """
    Main backend pipeline for defect analysis.

    Steps:
    1. Combine bug fields
    2. Generate embedding
    3. Perform similarity search
    4. Classify duplicate status
    5. Enhance bug report
    """

    # ------------------------------------
    # Combine bug fields
    # ------------------------------------

    combined_text = f"""
    {request.title}
    {request.description}
    {request.steps}
    {request.environment}
    """.strip()

    # ------------------------------------
    # Generate embedding
    # ------------------------------------

    query_embedding = embedding_engine.encode_query(combined_text)

    # ------------------------------------
    # Similarity search
    # ------------------------------------

    results = similarity_search.search(
        query_embedding,
        top_k=5
    )

    # ------------------------------------
    # Determine duplicate decision
    # ------------------------------------

    if results:
        top_score = results[0]["score"]
    else:
        top_score = 0.0

    # derive confidence and decision from the top score
    confidence = generate_confidence(top_score)

    if confidence == "high":
        decision = "duplicate"
    elif confidence == "medium":
        decision = "possible_duplicate"
    else:
        decision = "new"

    # ------------------------------------
    # Generate cluster id
    # ------------------------------------

    if results:
        cluster_id = f"cluster_{results[0]['bug_id']}"
    else:
        cluster_id = "cluster_new"

    # ------------------------------------
    # Enhance bug report
    # ------------------------------------

    enhanced = enhance_bug_report({
        "title": request.title,
        "description": request.description,
        "steps": request.steps,
        "environment": request.environment
    })

    # ------------------------------------
    # Final response
    # ------------------------------------

    result = {
        "decision": decision,
        "confidence": confidence,
        "cluster_id": cluster_id,
        "top_matches": results,
        "improved_title": enhanced["title"],
        "improved_summary": enhanced["summary"]
    }

    return result