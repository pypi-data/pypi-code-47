import pandas as pd

import pytest

from tabla.tabla import Table, TableColumn

@pytest.fixture
def columns():
    return [
        TableColumn("date", "", "%Y-%m-%d", "Date"),
        TableColumn("temp", "(degrees)", "{:0.2}", "Temperature"),
        TableColumn("rate", r"(m day\textsuperscript{-1})", "{:04.3}", "Rate"),
    ]


@pytest.fixture
def dataframe(columns):
    dates = pd.date_range("2020-01-01", "2020-01-02", freq="6H")
    data = list()
    for date in dates:
        d = {"date":date}
        d.update({c: pd.np.random.random() for c in ["temp", "rate"]})
        data.append(d)
    return pd.DataFrame(data)


def test_table(columns, dataframe):
    """Test that the table is generated"""
    table = Table("test_name", columns, dataframe, header_units=True)
    assert table.dumps()
