from src.load_data import load_any


def test_load_auth_log()  -> list: 
    data = load_any("data/raw/web_access.log")

    assert isinstance(data, list), "Expected list for log file"
    assert len(data) > 0, "Log file is empty"

   



