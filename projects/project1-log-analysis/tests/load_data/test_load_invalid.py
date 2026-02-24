import pytest
from src.load_data import load_any


def test_load_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        load_any("data/raw/does_not_exist.log")



