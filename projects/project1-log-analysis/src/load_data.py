# Load log files

import os 
import pandas as pd
#from typing import Union 



def load_text_log(filepath: str) -> list:
    """
    Load a plain text log file (.log, .txt).
    Returns a list where each element is one line of the log.

    Cargar un archivo de registro de texto plano (.log, .txt).
    Retorna una lista en la que cada elemento es una linea del regitro log.

    Parameters
    ----------
    filepath: str
        Path to the log file.
    
    Returns
    -------
    list
        Lines of the log file as strings.
    """
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, "r", encoding = "utf-8", errors = "ignore") as f:
        lines = f.readlines()
    

    return [line.strip() for line in lines ]


def load_csv(filepath: str)  ->  pd.DataFrame:
    """

    Load a CSV file into a pandas DataFrame.
    Carga un archivo CSV en un DataFrame de pandas.

    Parametres
    ----------
    filepath : str

    Returns
    -------
    pandas.DataFrame
    """

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath)



def detect_file_type(filepath: str)  ->  str:
    """
    Identify the type of file based on extension.
    Identifica el tipo de archivo basado en su extensión.

    Returns: "text" or "csv"
    """

    ext = os.path.splitext(filepath)[1].lower()

    if ext in [".log", ".txt"]:
        return "text"
    elif ext == ".csv":
        return "csv"
    else:
        return "unknown"
    


#def load_any(filepath: str)  -> Union[list[str], pd.DataFrame]:
def load_any(filepath: str)  -> list[str] | pd.DataFrame:
    """
    Load ANY supported file (log, txt, csv).
    Automatically detects the file type.
    
    Detecta automáticamente el tipo de archivo.

    Returns 
    -------
    list OR pandas.DataFrame
    """

    filetype = detect_file_type(filepath)

    if filetype == "text":
        return load_text_log(filepath)
    elif filetype == "csv":
        return load_csv(filepath)
    else:
        raise ValueError(f"Unsopported file type: {filepath}")


if __name__ == "__main__":
    data = load_any("data/raw/auth.log")
    print(data[:3])