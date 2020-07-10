import pandas as pd

def read_csv_file(path_to_file):
    """
    Read in a csv file and return a pandas dataframe
    """
    return pd.read_csv(path_to_file)
