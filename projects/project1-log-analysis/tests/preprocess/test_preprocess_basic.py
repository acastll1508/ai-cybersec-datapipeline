# Test for preproces


from src.preprocess.main_function import preprocess_log


def test_preprocess_basic():


    lines = [
        "Dec 11 22:41:19 server sshd[2245]: Accepted password for admin from 92.118.12.77 port 55214 ssh2",
        "Jan 10 10:00:00 server sshd[123]: Failed password for root from 192.168.1.1 port 22 ssh2",
        "Jan 10 10:01:00 server sshd[123]: Accepted password for admin from 192.168.1.2 port 22 ssh2"
    ]

    df = preprocess_log(lines)

    assert len(df) == 3
    assert "ip_int" in df.columns
    assert df.iloc[1]["status"] == "failed"
    assert df.iloc[2]["status"] == "success"
    assert "is_private" in df.columns
    assert "ip_version" in df.columns
    assert df.iloc[1]["ip_int"] == 3232235777
    assert df.iloc[1]["is_private"]
    assert df.iloc[1]["ip_version"] == 4
