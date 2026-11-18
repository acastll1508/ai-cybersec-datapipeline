import pandas as pd


def detect_event_frequency(
    df: pd.DataFrame,
    threshold: int = 21,
    window_minutes: int = 1,
) -> pd.DataFrame:
    """Detect unusually high authentication event frequency from a single IP."""

    columns = [
        "ip",
        "event_count",
        "start_time",
        "end_time",
        "window_seconds",
    ]

    if df.empty:
        return pd.DataFrame(columns=columns)

    events = df.copy()

    events["timestamp"] = pd.to_datetime(
        events["timestamp"],
        format="%b %d %H:%M:%S",
        errors="coerce",
    )

    events = events.dropna(subset=["timestamp", "ip"])
    events = events[events["status"].isin(["failed", "success"])]

    if events.empty:
        return pd.DataFrame(columns=columns)

    events = events.sort_values("timestamp")

    window_seconds = window_minutes * 60
    alerts = []

    for ip, group in events.groupby("ip"):
        group = group.reset_index(drop=True)

        for _, row in group.iterrows():
            end_time = row["timestamp"]
            start_limit = end_time - pd.Timedelta(seconds=window_seconds)

            window_events = group[
                (group["timestamp"] > start_limit)
                & (group["timestamp"] <= end_time)
            ]

            if len(window_events) >= threshold:
                first_event = window_events["timestamp"].iloc[0]

                alerts.append({
                    "ip": ip,
                    "event_count": len(window_events),
                    "start_time": first_event,
                    "end_time": end_time,
                    "window_seconds": int(
                        (end_time - first_event).total_seconds()
                    ),
                })

                break

    return pd.DataFrame(alerts, columns=columns)
