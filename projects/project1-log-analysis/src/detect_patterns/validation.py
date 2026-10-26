import pandas as pd



REQUIRED_COLUMNS = {"timestamp", "ip", "status"}



def validate_parameters(
    threshold: int,
    window_minutes: int,
) -> None:
    """Validate brute-force detection parameters."""

    if (
        isinstance(threshold, bool)
        or not isinstance(threshold, int)
        or threshold < 1
    ):
        raise ValueError("threshold must be a positive integer")

    if (
        isinstance(window_minutes, bool)
        or not isinstance(window_minutes, int)
        or window_minutes <= 0
    ):
        raise ValueError("window_minutes must be a positive integer")


def validate_columns(df: pd.DataFrame) -> None:
    """Validate the required Dataframe columns."""

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )
