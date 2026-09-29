import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config


def test_config_values():

    # Validate important config values exist
    assert config.RAW_DATA_PATH is not None
    assert config.PROCESSED_DATA_PATH is not None
    assert config.CLEANED_DATASET_PATH is not None

    assert config.EMBEDDING_MODEL_NAME is not None

    assert config.FAISS_INDEX_PATH.endswith(".bin")
    assert config.METADATA_PATH.endswith(".pkl")

    assert config.DUPLICATE_THRESHOLD > config.POSSIBLE_DUPLICATE_THRESHOLD

    assert config.API_PORT == 8000

    assert config.DBSCAN_EPS > 0
    assert config.DBSCAN_MIN_SAMPLES > 0

    assert config.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]

    print("Config validation passed ✅")