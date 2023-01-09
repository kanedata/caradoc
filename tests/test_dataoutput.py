import tempfile

import pandas as pd

from dataanalysis import DataOutput, ExcelTable


def test_dataoutput():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]})
    do.add_table(df, "test", title="test")
    assert do.sheets["test"][0].df.equals(df)


def test_dataoutput_exceltable():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]})
    tb = ExcelTable(df, title="test")
    do.add_table(tb, "test")
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


def test_dataoutput_excel_true_index():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]}, index=["A", "B", "C"])
    do.add_table(df, "test", title="test")
    with tempfile.TemporaryDirectory() as tmp:
        do.write(tmp + "/test.xlsx")
        assert pd.read_excel(tmp + "/test.xlsx", sheet_name="test", skiprows=2).equals(
            df.reset_index()
        )


def test_dataoutput_excel_summary_notes():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]})
    do.add_table(df, "test", title="test", summary="summary", notes="notes")
    with tempfile.TemporaryDirectory() as tmp:
        do.write(tmp + "/test.xlsx")
        # length should be:
        # 1 row for title
        # 1 row for summary
        # 1 row gap
        # 4 rows for data
        # 1 row for notes
        # = 8
        assert (
            len(pd.read_excel(tmp + "/test.xlsx", sheet_name="test", header=None)) == 8
        )


def test_dataoutput_summary_notes():
    do = DataOutput()
    df = pd.DataFrame({"a": [1, 2, 3]})
    do.add_table(df, "test", title="test", summary="summary", notes="notes")
    assert do.sheets["test"][0].df.equals(df)
