# Tests for preprocess

#from src.preprocess import preprocess_auth_log
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


def test_preprocess_valid_ipv6():

    lines = [
        "Jan 10 10:05:00 server sshd[123]: Failed password for root from 2001:db8::1 port 22 ssh2"
    ]


    df = preprocess_log(lines)

    assert len(df) == 1
    assert df.iloc[0]["ip"] == "2001:db8::1"
    assert df.iloc[0]["ip_version"] == 6
