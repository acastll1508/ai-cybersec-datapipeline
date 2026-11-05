import pandas as pd

from src.detect_patterns.multiple_users import detect_multiple_users


def create_events(timestamps, users, ips=None, statuses=None):
    """Create a DataFrame with authentication events."""

    if ips is None:
        ips = ["203.0.113.10"] * len(users)

    if statuses is None:
        statuses = ["failed"] * len(users)

    return pd.DataFrame({
        "timestamp": timestamps,
        "ip": ips,
        "user": users,
        "status": statuses,
    })


def test_detects_five_distinct_users():
    df = create_events(
        timestamps=[
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:04:00",
        ],
        users=["admin", "root", "test", "guest", "oracle"],
    )

    result = detect_multiple_users(df)

    assert len(result) == 1
    assert result.iloc[0]["distinct_users"] == 5


def test_does_not_detect_four_distinct_users():
    df = create_events(
        timestamps=[
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
        ],
        users=["admin", "root", "test", "guest"],
    )

    result = detect_multiple_users(df)

    assert result.empty


def test_does_not_count_repeated_users():
    df = create_events(
        timestamps=[
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:04:00",
        ],
        users=["admin", "admin", "root", "root", "test"],
    )

    result = detect_multiple_users(df)

    assert result.empty


def test_does_not_combine_events_from_different_ips():
    df = create_events(
        timestamps=[
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:04:00",
        ],
        users=["admin", "root", "test", "guest", "oracle"],
        ips=[
            "203.0.113.10",
            "203.0.113.10",
            "203.0.113.20",
            "203.0.113.20",
            "203.0.113.30",
        ],
    )

    result = detect_multiple_users(df)

    assert result.empty


def test_does_not_detect_users_outside_time_window():
    df = create_events(
        timestamps=[
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:05:01",
        ],
        users=["admin", "root", "test", "guest", "oracle"],
    )

    result = detect_multiple_users(df)

    assert result.empty


def test_ignores_successful_events():
    df = create_events(
        timestamps=[
            "Jan 10 10:00:00",
            "Jan 10 10:01:00",
            "Jan 10 10:02:00",
            "Jan 10 10:03:00",
            "Jan 10 10:05:01",
        ],
        users=["admin", "root", "test", "guest", "oracle"],
        statuses=["failed", "failed", "failed", "failed", "success"],
    )

    result = detect_multiple_users(df)

    assert result.empty
