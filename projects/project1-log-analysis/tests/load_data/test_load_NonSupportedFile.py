import pytest
from src.load_data import load_any


def test_load_unsupported_extension():
    with pytest.raises(ValueError):
        load_any("data/raw/non_supported_ext.img")


