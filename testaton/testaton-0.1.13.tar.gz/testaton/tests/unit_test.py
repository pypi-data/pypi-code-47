from testaton.generate_sql import generate_uniqueness_sql, generate_filter_sql, generate_fk_sql, generate_data_load_check_sql, generate_fk_sql_joins, generate_field_sql, generate_dataset_size_sql, decode_date, decode_filter_statement, generate_uniqueness_multiple_no_with
from collections import Counter
import pytest

class testDataset:
    def __init__(self,tableName):
        self.table_name = tableName

flights = testDataset("flights")
carriers = testDataset("carriers")
airports = testDataset("airports")
date_table = testDataset("date_table")
data = {"flights": flights, "carriers": carriers, "airports": airports, "date_table": date_table}

def test_dataset_size_sql():
    test_def = {
        "description": "make sure airport is good",
        "test_type": "dataset_size",
        "dataset": "flights",
        "min_value": "1000",
        "max_value": "2000",
        "filter": "carrier != 'American Airlines'"
    }
    generated = generate_dataset_size_sql(data, test_def).split()
    expected = "select count(*) from flights where carrier != 'American Airlines'".split()
    assert "".join(generated) == "".join(expected) and Counter(generated) == Counter(expected), "not same contents"

def test_uniqueness_sql():
    test_def = {
        "description": "airport lookup does not have any duplicates",
        "test_type": "unique",
        "dataset": "airports",
        "field": "Code",
        "severity": "Error"
    }
    generated = generate_uniqueness_sql(data, test_def).split()
    expected = "select Code, count(1) as dupes from airports group by Code having count(1) > 1  order by dupes desc  limit 10".split()
    assert "".join(generated) == "".join(expected) and Counter(generated) == Counter(expected), "uniqueness wrong"

def test_filter_sql():
    test_def = {
        "description": "filter test time",
        "test_type": "filter",
        "dataset": "flights",
        "filter": "ORIGIN != 'CVG'",
        "severity": "Info"
    }
    generated = generate_filter_sql(data, test_def).split()
    expected = "select count(1) as result_count from flights where ORIGIN != 'CVG'".split()
    assert "".join(generated) == "".join(expected) and Counter(generated) == Counter(expected), "filter wrong"

def test_fk_sql():
    test_def = {
        "description": "airports vs flight origin and destinations test",
        "test_type": "foreign_key",
        "parent_dataset": "airports",
        "parent_field": "Code",
        "child_dataset": "flights",
        "child_field": "DEST",
        "severity": "Error"
    }
    generated = generate_fk_sql_joins(data, test_def).split()
    expected = "select sum(case when c_DEST is not null then 1 else 0 end) / sum(inc) as pc_populated, sum(case when c_DEST is null then 1 else 0 end) as result_count from (select distinct p.Code as p_Code, c.DEST as c_DEST, 1 as inc from airports p left outer join flights c on p.Code = c.DEST) a".split()
    assert "".join(generated) == "".join(expected), "fk wrong"

def test_field_accuracy_sql():
    test_def = {
        "description": "checks if the carrier names are the same",
        "test_type": "field_accuracy",
        "dataset": "flights",
        "fields": ["ORIGIN_AIRPORT_SEQ_ID", "ORIGIN_AIRPORT_ID"]
    }
    generated = generate_field_sql(data, test_def).split()
    expected = "select ORIGIN_AIRPORT_SEQ_ID, ORIGIN_AIRPORT_ID from flights".split()
    assert "".join(generated) == "".join(expected) and Counter(generated) == Counter(expected)

def test_data_load_check_sql():
    test_def = {
        "description": "Check to make sure flights have been added",
        "test_type": "data_load_check",
        "date_field": "DATE",
        "dataset": "flights",
        "start_date": "20190101",
        "end_date": "20200101",
        "date_table": "date_table",
        "date_type": "string_8ch"   
    }
    generated = generate_data_load_check_sql(data, test_def).split()
    expected = """select d.date_id, data.records
    from date_table d left outer join
            (select DATE as date_id, count(1) records
            from flights
            where DATE >= '20190101' and DATE <= '20200101'
            group by DATE ) data
            on d.date_id = data.date_id
    where d.date_id >= '20190101' and d.date_id <= '20200101'
          and data.records is null
    order by d.date_id desc
    limit 10""".split()
    assert "".join(generated) == "".join(expected) and Counter(generated) == Counter(expected) 

#For the generate_uniqueness_multiple_no_with function
def test_generate_uniqueness_multiple_no_with_sql():
    test_def = {
        "description": "makes sure that there are unique origin, dest, and carrier",
        "test_type": "unique",
        "dataset": "flights",
        "field": ["origin", "dest", "carrier"],
        "severity": "Error"
    }
    generated = generate_uniqueness_multiple_no_with(data, test_def).split()
    expected = "select origin, dest, carrier, count(1) as dupes from (select origin, dest, carrier from flights)inr group by origin, dest, carrier having count(1) > 1 order by dupes desc limit 10".split()
    assert "".join(generated) == "".join(expected) and Counter(generated) == Counter(expected)

def main():
    test_dataset_size_sql()
    test_uniqueness_sql()
    test_filter_sql()
    test_fk_sql()
    test_field_accuracy_sql()
    test_data_load_check_sql()
    test_generate_uniqueness_multiple_no_with_sql()

main()



