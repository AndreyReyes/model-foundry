"""Data cleaning utilities."""

import pandas as pd


def clean_events(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and normalize raw event records."""
    cleaned = df.copy()

    cleaned["timestamp"] = pd.to_datetime(
        cleaned["timestamp"], format="ISO8601", errors="coerce", utc=True
    )
    cleaned["message_len"] = pd.to_numeric(
        cleaned["message_len"], errors="coerce"
    )
    cleaned["contains_link"] = pd.to_numeric(
        cleaned["contains_link"], errors="coerce"
    )
    cleaned["label_is_spam"] = pd.to_numeric(
        cleaned["label_is_spam"], errors="coerce"
    )

    cleaned = cleaned.dropna(
        subset=["timestamp", "message_len", "contains_link", "label_is_spam"]
    ).astype(
        {
            "message_len": "int64",
            "contains_link": "int64",
            "label_is_spam": "int64",
        }
    )

    return cleaned
