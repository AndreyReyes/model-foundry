"""Feature engineering utilities."""

import pandas as pd


def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Build model features and label from cleaned events."""
    featured = df.copy()
    featured["hour_utc"] = featured["timestamp"].dt.hour.astype(int)

    x = featured[["message_len", "contains_link", "hour_utc", "role", "device_type"]].copy()
    y = featured["label_is_spam"].copy()

    return x, y
