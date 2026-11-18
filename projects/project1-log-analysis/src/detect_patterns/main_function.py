import pandas as pd

from src.detect_patterns.brute_force import detect_bruteforce as _detect_bruteforce
from src.detect_patterns.validation import (
    validate_columns,
    validate_parameters,
)
from src.detect_patterns.success_after_failures import (
    detect_success_after_failures as _detect_success_after_failures
)
from src.detect_patterns.multiple_users import (
    detect_multiple_users as _detect_multiple_users,
)
from src.detect_patterns.event_frequency import (
    detect_event_frequency as _detect_event_frequency,
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
    window_minutes: int = 5,
) -> pd.DataFrame:
    """Detect successful logins preceded by repeated failures."""

    validate_parameters(threshold, window_minutes)
    validate_columns(
        df,
        required_columns={"timestamp", "ip", "status", "user"},
    )

    return _detect_success_after_failures(
        df,
        threshold=threshold,
        window_minutes=window_minutes,
    )


def detect_multiple_users(
    df: pd.DataFrame,
    threshold: int = 5,
    window_minutes: int = 5,
) -> pd.DataFrame:
    """Detect one IP attempting authentication against multiple users."""

    validate_parameters(threshold, window_minutes)
    validate_columns(
        df,
        required_columns={"timestamp", "ip", "status", "user"},
    )

    return _detect_multiple_users(
        df,
        threshold=threshold,
        window_minutes=window_minutes,
    )


def detect_event_frequency(
    df: pd.DataFrame,
    threshold: int = 21,
    window_minutes: int = 1,
) -> pd.DataFrame:
    """Detect unusually high authentication event frequency from a single IP."""

    validate_parameters(threshold, window_minutes)
    validate_columns(df)

    return _detect_event_frequency(
        df,
        threshold=threshold,
        window_minutes=window_minutes,
    )
