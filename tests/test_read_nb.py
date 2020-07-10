import pandas as pd

import csv_data_explorer


def test_read_gives_notebook():
    df = csv_data_explorer.read_csv_file("test.csv")
    assert type(df) is pd.DataFrame
