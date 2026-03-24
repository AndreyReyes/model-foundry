from pathlib import Path

import pandas as pd

from model_foundry.data.ingest import load_csv


def test_load_csv_returns_dataframe() -> None:
    path = Path("data/sample/events.csv")

    df = load_csv(path)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert list(df.columns) == [
        "timestamp",
        "user_id",
        "role",
        "channel_id",
        "message_len",
        "contains_link",
        "device_type",
        "label_is_spam",
    ]
