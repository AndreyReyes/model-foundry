"""Data cleaning utilities."""

import pandas as pd


def clean_events(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and normalize raw event records."""
    cleaned = df.copy()

    cleaned["timestamp"] = pd.to_datetime(
        cleaned["timestamp"], format="ISO8601", errors="coerce", utc=True
    )
    cleaned["message_len"] = (
        pd.to_numeric(cleaned["message_len"], errors="coerce").fillna(0).astype(int)
    )
    cleaned["contains_link"] = (
        pd.to_numeric(cleaned["contains_link"], errors="coerce").fillna(0).astype(int)
    )
    cleaned["label_is_spam"] = (
        pd.to_numeric(cleaned["label_is_spam"], errors="coerce").fillna(0).astype(int)
    )

    cleaned = cleaned.dropna(subset=["timestamp"])

    return cleaned
