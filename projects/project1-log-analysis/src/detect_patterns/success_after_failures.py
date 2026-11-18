import pandas as pd


def detect_success_after_failures(
        df: pd.DataFrame,
        threshold: int = 3,
        window_minutes: int = 5,
) -> pd.DataFrame:
    """Detect successful login preceded by repeated failures."""

    result_columns = [
            "ip",
            "user",
            "failed_attempts",
            "first_failure",
            "success_time",
            "window_seconds"
    ]

    events = df.loc[
        df["status"].isin(["failed", "success"]),
        ["timestamp", "ip", "user", "status"],
    ].copy()

    events["timestamp"] = pd.to_datetime(
        events["timestamp"],
        format = "%b %d %H:%M:%S",
        errors = "coerce"
    )

    events = events.dropna(
        subset=["timestamp", "ip", "user"]
    )

    failures = events.loc[events["status"] == "failed"]
    successes = events.loc[events["status"] == "success"]

    window = pd.Timedelta(minutes=window_minutes)
    alerts = []

    for (ip, user), group in failures.groupby(["ip", "user"]):
        failure_times = group["timestamp"].sort_values()

        matching_successes = successes.loc[
            (successes["ip"] == ip)
            & (successes["user"] == user)
        ]

        for success_time in matching_successes["timestamp"].sort_values():
            recent_failures = failure_times.loc[
                (failure_times >= success_time - window)
                & (failure_times < success_time)
            ]

            if len(recent_failures) < threshold:
                continue

            first_failure = recent_failures.iloc[-threshold]

            alerts.append(
                {
                    "ip": ip,
                    "user": user,
                    "failed_attempts": len(recent_failures),
                    "first_failure": first_failure,
                    "success_time": success_time,
                    "window_seconds": (
                        success_time - first_failure
                    ).total_seconds()
                }
            )

    return pd.DataFrame(alerts, columns=result_columns)
