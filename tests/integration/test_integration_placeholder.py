"""Placeholder integration tests for the repository scaffold."""

from pathlib import Path


def test_sample_data_directory_exists() -> None:
    """Ensure the sample data directory exists for future integration tests."""
    sample_dir = Path("data/sample")
    assert sample_dir.exists()
    assert sample_dir.is_dir()
