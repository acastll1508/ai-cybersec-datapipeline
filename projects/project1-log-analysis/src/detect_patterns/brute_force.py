import pandas as pd



def detect_bruteforce(
    df: pd.DataFrame,
    threshold: int = 5,
    window_minutes: int = 5,
) -> pd.DataFrame:
    """Detect repeated failed authentication attempts from the same IP."""

    failed = df.loc[df["status"] == "failed"].copy()

    result_columns = [
        "ip",
        "failed_attempts",
        "start_time",
        "end_time",
        "window_seconds",
    ]

    if failed.empty:
        return pd.DataFrame(columns=result_columns)

    failed["timestamp"] = pd.to_datetime(
        failed["timestamp"],
        format="%b %d %H:%M:%S",
        errors="coerce",
    )

    failed = failed.dropna(subset=["timestamp", "ip"])

    suspicious = []
    window = pd.Timedelta(minutes=window_minutes)

    for ip, group in failed.groupby("ip"):
        timestamps = group["timestamp"].sort_values().tolist()
        start = 0

        for end in range(len(timestamps)):
            while timestamps[end] - timestamps[start] > window:
                start += 1

            count = end - start + 1

            if count >= threshold:
                suspicious.append(
                    {
                        "ip": ip,
                        "failed_attempts": count,
                        "start_time": timestamps[start],
                        "end_time": timestamps[end],
                        "window_seconds": (
                            timestamps[end] - timestamps[start]
                        ).total_seconds(),
                    }
                )
                break

    return pd.DataFrame(suspicious, columns=result_columns)
