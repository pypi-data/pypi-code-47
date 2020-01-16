def test_get_data_qa_etl_historical():
    data_source = dm.get_datasource_by_id(QA_ETL_UUID)
    company = dm.get_company_by_id(79)
    df = data_source.get_data(company, end_date="2017-09-01")
    assert len(df) == 244
    df = data_source.get_data(company, end_date="2019-01-01")
    assert_data_frame(df, 2192, "int64")
    records = {
        "dimensions": {"country": "USA", "category": "small"},
        "end_date": pandas.to_datetime("2017-07-01"),
        "start_date": pandas.to_datetime("2017-07-01"),
        "value": 1701,
        "time_span": datetime.timedelta(days=1),
    }
    assert_frame_equal(df.head(1), pandas.DataFrame.from_records([records]))
    df = data_source.get_data(company, start_date="2018-12-10", end_date="2019-01-01")
    assert_data_frame(df, 84, "int64")
    records = {
        "dimensions": {"country": "USA", "category": "small"},
        "end_date": pandas.to_datetime("2018-12-10"),
        "start_date": pandas.to_datetime("2018-12-10"),
        "value": 11210,
        "time_span": datetime.timedelta(days=1),
    }
    assert_frame_equal(df.head(1), pandas.DataFrame.from_records([records]))
    df = data_source.get_data(
        company, Aggregation(period="quarter", company=company), end_date="2019-01-01"
    )
    assert_data_frame(df, 24)
    records = {
        "dimensions": {"country": "USA", "category": "small"},
        "end_date": pandas.to_datetime("2017-09-30"),
        "start_date": pandas.to_datetime("2017-07-01"),
        "value": 1814.75,
        "time_span": datetime.timedelta(days=92),
    }
    assert_frame_equal(df.head(1), pandas.DataFrame.from_records([records]))
