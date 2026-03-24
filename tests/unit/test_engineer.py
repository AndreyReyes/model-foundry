import pandas as pd

from model_foundry.features.engineer import build_features


def test_build_features_adds_hour_utc_and_returns_x_y() -> None:
    df = pd.DataFrame(
        [
            {
                "timestamp": pd.Timestamp("2026-03-01T10:00:00Z"),
                "user_id": "u1",
                "role": "expert",
                "channel_id": "c1",
                "message_len": 120,
                "contains_link": 0,
                "device_type": "desktop",
                "label_is_spam": 0,
            }
        ]
    )

    x, y = build_features(df)

    assert list(x.columns) == [
        "message_len",
        "contains_link",
        "hour_utc",
        "role",
        "device_type",
    ]
    assert y.name == "label_is_spam"
    assert x.iloc[0]["hour_utc"] == 10
    assert y.iloc[0] == 0
