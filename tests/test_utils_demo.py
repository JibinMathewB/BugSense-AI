import sys
import os

# ensure project root is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.constants import EMBEDDING_MODEL, TOP_K_RESULTS, RAW_DATA_PATH
from utils.file_loader import load_csv
from utils.logger import get_logger


def test_utils_demo():

    logger = get_logger("utils_test")

    logger.info("Starting utils module test")

    # test constants
    assert EMBEDDING_MODEL is not None
    assert TOP_K_RESULTS > 0

    logger.info(f"Embedding model: {EMBEDDING_MODEL}")
    logger.info(f"Top K results: {TOP_K_RESULTS}")

    # test file loader
    df = load_csv(RAW_DATA_PATH)

    assert df is not None
    assert len(df) > 0

    logger.info(f"Dataset loaded successfully with shape: {df.shape}")

    print("\nFirst 3 rows of dataset:\n")
    print(df.head(3))

    logger.info("Utils test completed successfully")


if __name__ == "__main__":
    test_utils_demo()