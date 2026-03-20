import pandas as pd

from model_foundry.data.clean import clean_events


def test_clean_events_parses_timestamp_and_normalizes_types() -> None:
    df = pd.DataFrame(
        [
            {
                "timestamp": "2026-03-01T10:00:00Z",
                "user_id": "u1",
                "role": "expert",
                "channel_id": "c1",
                "message_len": "120",
                "contains_link": "0",
                "device_type": "desktop",
                "label_is_spam": "0",
            }
        ]
    )

    cleaned = clean_events(df)

    assert len(cleaned) == 1
    assert str(cleaned["timestamp"].dtype).startswith("datetime64")
    assert cleaned["message_len"].dtype == "int64"
    assert cleaned["contains_link"].dtype == "int64"
    assert cleaned["label_is_spam"].dtype == "int64"


def test_clean_events_drops_rows_with_invalid_required_fields() -> None:
    df = pd.DataFrame(
        [
            {
                "timestamp": "not-a-date",
                "user_id": "u1",
                "role": "expert",
                "channel_id": "c1",
                "message_len": 120,
                "contains_link": 0,
                "device_type": "desktop",
                "label_is_spam": 0,
            },
            {
                "timestamp": "2026-03-01T10:00:00Z",
                "user_id": "u2",
                "role": "ops",
                "channel_id": "c2",
                "message_len": 15,
                "contains_link": 1,
                "device_type": "mobile",
                "label_is_spam": 1,
            },
        ]
    )

    cleaned = clean_events(df)

    assert len(cleaned) == 1
    assert cleaned.iloc[0]["user_id"] == "u2"
