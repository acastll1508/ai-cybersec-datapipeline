import pandas as pd
import pytest

from src.detect_patterns.validation import (
        validate_columns,
        validate_parameters
)


@pytest.mark.parametrize(
        "threshold",
        [0, -1, 1.5, True],
)
def test_validate_parameters_rejects_invalid_threshold(threshold):
    with pytest.raises(ValueError):
        validate_parameters(threshold, window_minutes=5)


@pytest.mark.parametrize(
        "window_minutes",
        [0, -1, 1.5, True],
)
def test_validate_parameters_rejects_invalid_window(window_minutes):
    with pytest.raises(ValueError):
        validate_parameters(threshold=5,window_minutes=window_minutes)


def test_validate_parameters_accept_valid_values():
    validate_parameters(threshold=5, window_minutes=5)


def test_validate_columns_accepts_required_columns():
    df = pd.DataFrame(
            columns = ["timestamp", "ip", "status"]
    )

    validate_columns(df)


def test_validate_columns_rejects_missing_columns():
    df = pd.DataFrame(
            columns = ["timestamp", "ip"]
    )

    with pytest.raises(ValueError, match="status"):
        validate_columns(df)
