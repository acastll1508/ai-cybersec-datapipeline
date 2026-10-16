# Tests for invalid preprocess input


from src.preprocess.main_function import preprocess_log



def test_preprocess_ignores_invalid_lines():

    lines = [
        "random noise log",
        "another invalid line"
    ]

    df = preprocess_log(lines)

    assert df.empty



def test_preprocess_ignores_malformed_ip():

    lines = [
        "Jan 10 10:03:00 server sshd[123]: Failed password for root from 192x168x1x1 port 22 ssh2"
    ]


    df = preprocess_log(lines)

    assert df.empty



def test_preprocess_ignores_invalid_ipv4():

    lines = [
        "Jan 10 10:04:00 server sshd[123]: Failed password for root from 999.999.999.999 port 22 ssh2"
    ]


    df = preprocess_log(lines)

    assert df.empty



def test_preprocess_mixed_valid_and_invalid_lines():

    lines = [
        "Jan 10 10:00:00 server sshd[123]: Failed password for root from 192.168.1.1 port 22 ssh2",
        "Jan 10 10:01:00 server sshd[123]: Failed password for root from 999.999.999.999 port 22 ssh2",
        "Jan 10 10:02:00 server sshd[123]: Accepted password for admin from 192.168.1.2 port 22 ssh2"
    ]

    df = preprocess_log(lines)

    assert len(df) == 2
    assert df["ip"].tolist() == ["192.168.1.1", "192.168.1.2"]
    assert df["status"].tolist() == ["failed", "success"]
