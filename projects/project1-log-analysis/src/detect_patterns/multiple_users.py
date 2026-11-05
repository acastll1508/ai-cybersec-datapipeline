import pandas as pd


def detect_multiple_users(
    df: pd.DataFrame,
    threshold: int = 5,
    window_minutes: int = 5,
) -> pd.DataFrame:
    """Detect one IP attempting authentication against multiple users."""

    result_columns = [
        "ip",
        "distinct_users",
        "users",
        "start_time",
        "end_time",
        "window_seconds",
    ]

    failed_events = df.loc[df["status"] == "failed"].copy()

    failed_events["timestamp"] = pd.to_datetime(
        failed_events["timestamp"],
        format="%b %d %H:%M:%S",
        errors="coerce",
    )

    failed_events = failed_events.dropna(
        subset=["timestamp", "ip", "user"]
    )

    failed_events = failed_events.sort_values("timestamp")

    window = pd.Timedelta(minutes=window_minutes)
    alerts = []

    for ip, events in failed_events.groupby("ip"):
        events = events.reset_index(drop=True)

        for end_index in range(len(events)):
            end_time = events.loc[end_index, "timestamp"]
            start_time = end_time - window

            window_events = events.loc[
                (events["timestamp"] > start_time)
                & (events["timestamp"] <= end_time)
            ]

            unique_users = window_events["user"].drop_duplicates()

            if len(unique_users) >= threshold:
                first_event = window_events["timestamp"].iloc[0]

                alerts.append({
                    "ip": ip,
                    "distinct_users": len(unique_users),
                    "users": unique_users.tolist(),
                    "start_time": first_event,
                    "end_time": end_time,
                    "window_seconds": (
                        end_time - first_event
                    ).total_seconds(),
                })

                break

    return pd.DataFrame(alerts, columns=result_columns)
