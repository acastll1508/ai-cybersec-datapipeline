import pandas as pd

from src.detect_patterns.event_frequency import detect_event_frequency


def create_event(timestamps, ips=None, statuses=None):
    """Create a DataFrame with authentication events."""

    if ips is None:
        ips = ["203.0.113.10"] * len(timestamps)

    if statuses is None:
        statuses = ["failed"] * len(timestamps)

    return pd.DataFrame({
        "timestamp": timestamps,
        "ip": ips,
        "status": statuses,
    })


def test_detect_twenty_one_events_within_one_minute():
    timestamps = [
        f"Jan 10 10:00:{second:02d}"
        for second in range(21)
    ]

    df = create_event(timestamps)

    result = detect_event_frequency(df)

    assert len(result) == 1
    assert result.iloc[0]["event_count"] == 21


def test_does_not_detect_twenty_events_within_one_minute():
    timestamps = [
        f"Jan 10 10:00:{second:02d}"
        for second in range(20)
    ]

    df = create_event(timestamps)

    result = detect_event_frequency(df)

    assert result.empty


def test_counts_failed_and_successful_events():
    timestamps = [
        f"Jan 10 10:00:{second:02d}"
        for second in range(21)
    ]

    statuses = [
        "failed" if second % 2 == 0 else "success"
        for second in range(21)
    ]

    df = create_event(
        timestamps=timestamps,
        statuses=statuses,
    )

    result = detect_event_frequency(df)

    assert len(result) == 1
    assert result.iloc[0]["event_count"] == 21


def test_does_not_combine_events_from_different_ips():
    timestamps = [
        f"Jan 10 10:00:{second:02d}"
        for second in range(21)
    ]

    ips = [
        "203.0.113.10" if second < 11 else "203.0.113.20"
        for second in range(21)
    ]

    df = create_event(
        timestamps=timestamps,
        ips=ips,
    )

    result = detect_event_frequency(df)

    assert result.empty


def test_does_not_detect_events_outside_time_window():
    timestamps = [
        "Jan 10 10:00:00",
        "Jan 10 10:00:02",
        "Jan 10 10:00:04",
        "Jan 10 10:00:06",
        "Jan 10 10:00:08",
        "Jan 10 10:00:10",
        "Jan 10 10:00:12",
        "Jan 10 10:00:14",
        "Jan 10 10:00:16",
        "Jan 10 10:00:18",
        "Jan 10 10:00:20",
        "Jan 10 10:00:22",
        "Jan 10 10:00:24",
        "Jan 10 10:00:26",
        "Jan 10 10:00:28",
        "Jan 10 10:00:30",
        "Jan 10 10:00:32",
        "Jan 10 10:00:34",
        "Jan 10 10:00:36",
        "Jan 10 10:00:38",
        "Jan 10 10:01:01",
    ]

    df = create_event(timestamps)

    result = detect_event_frequency(df)

    assert result.empty


def test_ignores_invalid_timestamps_and_missing_ips():
    timestamps = [
        "Jan 10 10:00:00",
        "invalid timestamp",
        "Jan 10 10:00:02",
    ]

    ips = [
        "203.0.113.10",
        "203.0.113.10",
        None,
    ]

    df = create_event(
        timestamps=timestamps,
        ips=ips,
    )

    result = detect_event_frequency(df)

    assert result.empty


def test_generates_only_one_alert_per_ip():
    timestamps = [
        f"Jan 10 10:00:{second:02d}"
        for second in range(30)
    ]

    df = create_event(timestamps)

    result = detect_event_frequency(df)

    assert len(result) == 1
    assert result.iloc[0]["event_count"] >= 21
