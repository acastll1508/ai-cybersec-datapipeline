import pandas as pd

from src.detect_patterns.brute_force import detect_bruteforce as _detect_bruteforce
from src.detect_patterns.validation import (
    validate_columns,
    validate_parameters,
)
from src.detect_patterns.success_after_failures import (
    detect_success_after_failures as _detect_success_after_failures
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


def detect_success_after_failures(
    df: pd.DataFrame,
    threshold: int = 3,
    window_minutes: int = 5
) -> pd.DataFrame:
    """Detect successful logins preceded by repeated failures."""

    validate_parameters(threshold,window_minutes)
    validate_columns(
        df,
        required_columns={"timestamp", "ip", "status", "user"},
    )

    return _detect_success_after_failures(
        df,
        threshold=threshold,
        window_minutes=window_minutes
    )
