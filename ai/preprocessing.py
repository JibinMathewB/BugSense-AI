import re
import pandas as pd


def clean_text(text: str) -> str:
    """
    Clean bug report text while preserving semantic meaning.
    """

    if not isinstance(text, str):
        return ""

    # Lowercase normalization
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove special characters but keep numbers
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def combine_bug_fields(row: pd.Series) -> str:
    """
    Combine important bug report fields into a single searchable text block.
    Supports multiple bug tracker schemas (Bugzilla, Jira, GitBugs).
    """

    fields = [
        "title",
        "description",
        "steps",
        "expected",
        "actual",
        "environment",
        "logs",
        "product",
        "component",
        "severity"
    ]

    text_parts = []

    for field in fields:
        value = row.get(field, "")
        if isinstance(value, str):
            text_parts.append(value)

    combined_text = " ".join(text_parts)

    return clean_text(combined_text)


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare dataset for embedding generation by creating a combined_text column.
    """

    # Replace NaN values
    df = df.fillna("")

    # Generate combined text for embeddings
    df["combined_text"] = df.apply(combine_bug_fields, axis=1)

    return df