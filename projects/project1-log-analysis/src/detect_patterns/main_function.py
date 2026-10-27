import pandas as pd

from src.detect_patterns.brute_force import detect_bruteforce as _detect_bruteforce
from src.detect_patterns.validation import (
    validate_columns,
    validate_parameters,
)


def detect_bruteforce(
    df: pd.DataFrame,
    threshold: int = 5,
    window_minutes: int = 5,
) -> pd.DataFrame:
    """Detect possible SSH brute-force attacks."""

    validate_parameters(threshold, window_minutes)
    validate_columns(df)

    return _detect_bruteforce(
        df,
        threshold=threshold,
        window_minutes=window_minutes,
    )
