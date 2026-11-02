import pandas as pd
import pytest

from src.detect_patterns import detect_success_after_failures


def test_detect_success_after_three_failures():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00"
        ],
        "ip": ["192.168.1.10"] * 4,
        "user": ["alice"] * 4,
        "status": ["failed", "failed", "failed", "success"]
    })

    result = detect_success_after_failures(df)

    assert len(result) == 1
    assert result.iloc[0]["ip"] == "192.168.1.10"
    assert result.iloc[0]["user"] == "alice"
    assert result.iloc[0]["failed_attempts"] == 3


def test_does_not_match_different_users():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00"
        ],
        "ip": ["192.168.1.10"] * 4,
        "user": ["alice", "alice", "bob", "alice"],
        "status": ["failed", "failed", "failed", "success"]
    })

    assert detect_success_after_failures(df).empty


def test_does_not_match_success_without_enough_prior_failures():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00"
        ],
        "ip": ["192.168.1.10"] * 3,
        "user": ["alice"] * 3,
        "status": ["failed", "failed", "success"]
    })

    assert detect_success_after_failures(df).empty


def test_respects_time_window():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:10:00"
        ],
        "ip": ["192.168.1.10"] * 4,
        "user": ["alice"] * 4,
        "status": ["failed", "failed", "failed", "success"]
    })

    assert detect_success_after_failures(df).empty


def test_rejects_missing_user_column():
    df = pd.DataFrame(columns=["timestamp", "ip", "status"])

    with pytest.raises(ValueError, match="user"):
        detect_success_after_failures(df)


def test_rejects_invalid_parameters():
    df = pd.DataFrame(
        columns=["timestamp", "ip", "user", "status"]
    )

    with pytest.raises(ValueError):
        detect_success_after_failures(df, threshold=0)

    with pytest.raises(ValueError):
        detect_success_after_failures(df, window_minutes=0)
