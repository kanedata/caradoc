import tempfile

import pandas as pd

from dataanalysis import DataOutput


def test_dataoutput():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]})
    do.add_table(df, "test", title="test")
    assert do.sheets["test"][0].df.equals(df)


def test_dataoutput_excel():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]})
    do.add_table(df, "test", title="test")
    with tempfile.TemporaryDirectory() as tmp:
        do.write(tmp + "/test.xlsx")
        assert pd.read_excel(tmp + "/test.xlsx", sheet_name="test", skiprows=2).equals(
            df
        )
