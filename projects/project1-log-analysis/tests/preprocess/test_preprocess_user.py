# Tests for user extraction en preprocess

from src.preprocess.main_function import preprocess_log


def test_preprocess_invalid_user_prefix():

    lines = [
        "Jan 10 10:00:00 server sshd[123]: Failed password for invalid user admin from 192.168.1.1 port 22 ssh2"
    ]

    df = preprocess_log(lines)

    assert len(df) == 1
    assert df.iloc[0]["user"] == "admin"


def test_preprocess_user_with_hyphen():

    lines = [
        "Jan 10 10:00:00 server sshd[123]: Failed password for juan-perez from 192.168.1.1 port 22 ssh2"
    ]

    df = preprocess_log(lines)

    assert df.iloc[0]["user"] == "juan-perez"


def test_preprocess_user_with_dot():

    lines = [
        "Jan 10 10:00:00 server sshd[123]: Accepted password for ana.lopez from 192.168.1.2 port 22 ssh2"
    ]

    df = preprocess_log(lines)

    assert df.iloc[0]["user"] == "ana.lopez"
