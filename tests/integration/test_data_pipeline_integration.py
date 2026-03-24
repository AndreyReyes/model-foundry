from pathlib import Path

from model_foundry.data.clean import clean_events
from model_foundry.data.ingest import load_csv
from model_foundry.features.engineer import build_features


def test_sample_events_pipeline_end_to_end() -> None:
    path = Path("data/sample/events.csv")

    raw = load_csv(path)
    cleaned = clean_events(raw)
    x, y = build_features(cleaned)

    assert len(raw) == 5
    assert len(cleaned) == 5
    assert list(x.columns) == [
        "message_len",
        "contains_link",
        "hour_utc",
        "role",
        "device_type",
    ]
    assert len(y) == 5
    assert y.name == "label_is_spam"
