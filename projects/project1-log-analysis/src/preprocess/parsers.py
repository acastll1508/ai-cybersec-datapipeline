import re
from src.preprocess.specific_processor import process_auth

AUTH_PATTERN = re.compile(
     r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+).*?"
    r"(?P<event>Failed password|Accepted password).*?"
    r"for (?P<user>\w+).*?"
    r"from (?P<ip>[0-9A-Fa-f:.]+)(?=\s)"
)

PARSERS = [
    {
        "name" : "auth",
        "pattern" : AUTH_PATTERN,
        "processor" : process_auth
    }
]
