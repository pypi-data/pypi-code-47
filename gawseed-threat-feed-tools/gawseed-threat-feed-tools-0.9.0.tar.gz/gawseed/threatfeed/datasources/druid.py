class DruidEnterprise(DataSource):
    def __init__(self, host=None,
                 port='8888', path='/druid/v2/sql', scheme='http',
                 begin_time=None, topic="ssh", max_records=None, table_name="ssh"):
        super().__init__()
        self._host = host
        self._port = port
        self._path = path
        self._scheme = scheme
        self._begin_time = begin_time
        self._topic = topic
        self._max_records = max_records
        self._table_name = table_name

    def open(self):
        from pydruid.db import connect
        conn = connect(host=self._host, port=self._port, path=self._path, scheme=self._scheme)
        self._conn
        self._curs = self._conn.cursor()

        if self._begin_time:
            time_field="where __time > "
            timestamp = parser.parse(self._begin_time).timestamp()
            (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
             tm_sec, tm_wday, tm_yday, tm_isdst) = time.gmtime(timestamp)
            formated_time = "'%04d-%02d-%02d %02d:%02d:%02d'" % (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)
            self._curs.execute("select * from %s where __time > %s limit %d" %
                               (self._table_name, formated_time, args.max_records))
        else:
            self._curs.execute("select * from %s %s limit %d" % (formated_time, args.max_records))

        return self

    def __iter__(self):
        return self

    def __next__(self):
        return(next(self._curs))
        # try:
        #     for row in self._curs:
        #         yield row 
        # except StopIteration as e:
        #     return

