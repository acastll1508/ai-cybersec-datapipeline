import pandas as pd
import pytest

from src.detect_patterns import detect_bruteforce


def test_detect_repeated_failed_attempts():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:04:00",
        ],
        "ip": ["192.168.1.10"] * 5,
        "status": ["failed"] * 5,
    })

    result = detect_bruteforce(df)

    assert len(result) == 1
    assert result.iloc[0]["ip"] == "192.168.1.10"
    assert result.iloc[0]["failed_attempts"] == 5


def test_ignores_successful_attempts():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
        ],
        "ip": ["192.168.1.10"] * 3,
        "status": ["failed", "success", "failed"]
    })

    result = detect_bruteforce(df, threshold=3)

    assert result.empty


def test_respects_time_window():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:10:00",
        ],
        "ip": ["192.168.1.10"] * 3,
        "status": ["failed"] * 3,
    })

    result = detect_bruteforce(
       df,
       threshold=3,
       window_minutes=5,
    )

    assert result.empty


def test_detect_only_suspicious_ip():
    df = pd.DataFrame({
        "timestamp": [
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:04:00",
            "Jan 10 10:00:00",
        ],
        "ip": [
            "192.168.1.10",
            "192.168.1.10",
            "192.168.1.10",
            "192.168.1.10",
            "192.168.1.10",
            "192.168.1.20",
        ],
        "status": ["failed"] * 6,
    })

    result = detect_bruteforce(df, threshold=5)

    assert result["ip"].tolist() == ["192.168.1.10"]


def test_rejects_invalid_parameters():
    df = pd.DataFrame(columns=["timestamp", "ip", "status"])

    with pytest.raises(ValueError):
        detect_bruteforce(df, threshold=0)

    with pytest.raises(ValueError):
        detect_bruteforce(df, window_minutes=0)


def test_rejects_missing_columns():
    df = pd.DataFrame(columns=["timestamp", "ip"])

    with pytest.raises(ValueError, match="status"):
        detect_bruteforce(df)
