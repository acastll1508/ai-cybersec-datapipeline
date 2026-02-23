import pandas as pd
from src.load_data import load_any


def test_load_csv()  ->  pd.DataFrame:
    data = load_any("data/raw/sample.csv")
    assert isinstance(data, pd.DataFrame), "Expected DataFrame for CSV"
    assert not data.empty, "CSV is empty"



