import pandas as pd
from src.preprocess.general_processor import parse_line

def preprocess_log(lines):

    records = []

    for line in lines:
        parsed = parse_line(line)

        if parsed:
            records.append(parsed)

        
    return pd.DataFrame(records)


