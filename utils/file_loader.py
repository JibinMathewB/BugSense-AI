import os
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset safely.
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError(f"Dataset is empty: {path}")

    return df


def save_csv(df: pd.DataFrame, path: str):
    """
    Save dataframe safely.
    """

    directory = os.path.dirname(path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    df.to_csv(path, index=False)


def file_exists(path: str) -> bool:
    """
    Check if file exists.
    """

    return os.path.exists(path)