from src.preprocess.parsers import PARSERS
from src.preprocess.specific_processor import process_auth

def parse_line(line):

    for parser in PARSERS:
        match = parser["pattern"].search(line)

        if match:
            #processor_fn = globals()[parser["processor"]]
            return parser["processor"](match)

    return None
