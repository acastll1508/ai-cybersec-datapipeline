#Tests for IP processing in preprocess

import ipaddress

from src.preprocess.main_function import preprocess_log



def test_preprocess_valid_ipv6():

    lines = [
        "Jan 10 10:05:00 server sshd[123]: Failed password for root from 2001:db8::1 port 22 ssh2"
    ]


    df = preprocess_log(lines)

    assert len(df) == 1
    assert df.iloc[0]["ip"] == "2001:db8::1"
    assert df.iloc[0]["ip_version"] == 6
    assert df.iloc[0]["ip_int"] == int(ipaddress.ip_address("2001:db8::1"))
