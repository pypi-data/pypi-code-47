import re
from html import escape
from IPython.core.magic import Magics, magics_class, cell_magic, line_magic, needs_local_scope
from IPython.display import display_javascript
try:
    from traitlets.config.configurable import Configurable
    from traitlets import Bool, Int, Unicode
except ImportError:
    from IPython.config.configurable import Configurable
    from IPython.utils.traitlets import Bool, Int, Unicode
try:
    from pandas.core.frame import DataFrame, Series
except ImportError:
    DataFrame = None
    Series = None

from sqlalchemy.exc import ProgrammingError, OperationalError

import sql.connection
import sql.parse
import sql.run
from pyspark.sql import SparkSession
from IPython.core.display import HTML
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
BIND_VARIABLE_PATTERN = re.compile(r'{([A-Za-z0-9_]+)}')



@magics_class
class SqlMagic(Magics, Configurable):
    """Runs SQL statement on a database, specified by SQLAlchemy connect string.

    Provides the %%sql magic."""

    autolimit = Int(0, config=True, allow_none=True, help="Automatically limit the size of the returned result sets")
    style = Unicode('DEFAULT', config=True, help="Set the table printing style to any of prettytable's defined styles (currently DEFAULT, MSWORD_FRIENDLY, PLAIN_COLUMNS, RANDOM)")
    short_errors = Bool(True, config=True, help="Don't display the full traceback on SQL Programming Error")
    displaylimit = Int(None, config=True, allow_none=True, help="Automatically limit the number of rows displayed (full result set is still stored)")
    autopandas = Bool(False, config=True, help="Return Pandas DataFrames instead of regular result sets")
    column_local_vars = Bool(False, config=True, help="Return data into local variables from column names")
    feedback = Bool(True, config=True, help="Print number of rows affected by DML")
    dsn_filename = Unicode('odbc.ini', config=True, help="Path to DSN file. "
                           "When the first argument is of the form [section], "
                           "a sqlalchemy connection string is formed from the "
                           "matching section in the DSN file.")
    autocommit = Bool(True, config=True, help="Set autocommit mode")


    def __init__(self, shell):
        Configurable.__init__(self, config=shell.config)
        Magics.__init__(self, shell=shell)

        # Add ourself to the list of module configurable via %config
        self.shell.configurables.append(self)

    @needs_local_scope
    @line_magic('sql')
    @cell_magic('sql')
    def execute(self, line, cell='', local_ns={}):
        """Runs SQL statement against a database, specified by SQLAlchemy connect string.

        If no database connection has been established, first word
        should be a SQLAlchemy connection string, or the user@db name
        of an established connection.

        Examples::

          %%sql postgresql://me:mypw@localhost/mydb
          SELECT * FROM mytable

          %%sql me@mydb
          DELETE FROM mytable

          %%sql
          DROP TABLE mytable

        SQLAlchemy connect string syntax examples:

          postgresql://me:mypw@localhost/mydb
          sqlite://
          mysql+pymysql://me:mypw@localhost/mydb

        """
        # save globals and locals so they can be referenced in bind vars
        user_ns = self.shell.user_ns.copy()
        user_ns.update(local_ns)

        parsed = sql.parse.parse('%s\n%s' % (line, cell), self)
        flags = parsed['flags']
        try:
            conn = sql.connection.Connection.set(parsed['connection'])
        except Exception as e:
            print(e)
            print(sql.connection.Connection.tell_format())
            return None

        if flags.get('persist'):
            return self._persist_dataframe(parsed['sql'], conn, user_ns)

        try:
            result = sql.run.run(conn, parsed['sql'], self, user_ns)

            if result is not None and not isinstance(result, str) and self.column_local_vars:
                #Instead of returning values, set variables directly in the
                #users namespace. Variable names given by column names

                if self.autopandas:
                    keys = result.keys()
                else:
                    keys = result.keys
                    result = result.dict()

                if self.feedback:
                    print('Returning data to local variables [{}]'.format(
                        ', '.join(keys)))

                self.shell.user_ns.update(result)

                return None
            else:

                if flags.get('result_var'):
                    result_var = flags['result_var']
                    print("Returning data to local variable {}".format(result_var))
                    self.shell.user_ns.update({result_var: result})
                    return None

                #Return results into the default ipython _ variable
                return result

        except (ProgrammingError, OperationalError) as e:
            # Sqlite apparently return all errors as OperationalError :/
            if self.short_errors:
                print(e)
            else:
                raise

    legal_sql_identifier = re.compile(r'^[A-Za-z0-9#_$]+')
    def _persist_dataframe(self, raw, conn, user_ns):
        """Implements PERSIST, which writes a DataFrame to the RDBMS"""
        if not DataFrame:
            raise ImportError("Must `pip install pandas` to use DataFrames")

        frame_name = raw.strip(';')

        # Get the DataFrame from the user namespace
        if not frame_name:
            raise SyntaxError('Syntax: %sql PERSIST <name_of_data_frame>')
        frame = eval(frame_name, user_ns)
        if not isinstance(frame, DataFrame) and not isinstance(frame, Series):
            raise TypeError('%s is not a Pandas DataFrame or Series' % frame_name)

       # Make a suitable name for the resulting database table
        table_name = frame_name.lower()
        table_name = self.legal_sql_identifier.search(table_name).group(0)

        frame.to_sql(table_name, conn.session.engine)
        return 'Persisted %s' % table_name


def load_ipython_extension(ip):
    """Load the extension in IPython."""

    # this fails in both Firefox and Chrome for OS X.
    # I get the error: TypeError: IPython.CodeCell.config_defaults is undefined

    # js = "IPython.CodeCell.config_defaults.highlight_modes['magic_sql'] = {'reg':[/^%%sql/]};"
    # display_javascript(js, raw=True)
    ip.register_magics(SqlMagic)
    ip.register_magics(SparkSql)


@magics_class
class SparkSql(Magics, Configurable):
    max_num_rows = Int(None, config=True, allow_none=True, help="自动限制显示的行数(仍然存储完整的结果集)")

    @needs_local_scope
    @cell_magic
    @magic_arguments()
    @argument('variable', nargs='?', type=str, help='查询结果赋值给一个变量')
    @argument('-c', '--cache', action='store_true', help='缓存查询数据')
    @argument('-e', '--eager', action='store_true', help='立即加载数据')
    @argument('-v', '--view', type=str, help='根据数据集，创建或替换到临时视图')
    def sparksql(self, line='', cell='', local_ns=None):
        if local_ns is None:
            local_ns = {}

        user_ns = self.shell.user_ns.copy()
        user_ns.update(local_ns)

        args = parse_argstring(self.sparksql, line)

        spark = get_instantiated_spark_session()

        if spark is None:
            print("spark没有活动的会话")
            return

        df = spark.sql(bind_variables(cell, user_ns))
        if args.cache or args.eager:
            # print('cache dataframe with %s load' % ('eager' if args.eager else 'lazy'))
            df = df.cache()
            if args.eager:
                df.count()
        if args.view:
            print('创建临时表 `%s`' % args.view)
            df.createOrReplaceTempView(args.view)
        if args.variable:
            print('赋值到变量 `%s`' % args.variable)
            self.shell.user_ns.update({args.variable: df})

        header, contents = get_results(df, self.max_num_rows)
        if len(contents) > self.max_num_rows:
            print('Top %d .' % self.max_num_rows)

        html = make_tag('tr', ''.join(map(lambda x: make_tag('td', escape(x), style='font-weight: bold'), header)), style='border-bottom: 1px solid')
        for index, row in enumerate(contents[:self.max_num_rows]):
            html += make_tag('tr', ''.join(map(lambda x: make_tag('td', escape(x)), row)))
        return HTML(make_tag('table', html))


def make_tag(tag_name, body='', **kwargs):
    attributes = ' '.join(map(lambda x: '%s="%s"' % x, kwargs.items()))
    if attributes:
        return '<%s %s>%s</%s>' % (tag_name, attributes, body, tag_name)
    else:
        return '<%s>%s</%s>' % (tag_name, body, tag_name)


def get_instantiated_spark_session():
    return SparkSession._instantiatedSession


def bind_variables(query, user_ns):
    def fetch_variable(match):
        variable = match.group(1)
        if variable not in user_ns:
            raise NameError('variable `%s` is not defined', variable)
        return str(user_ns[variable])

    return re.sub(BIND_VARIABLE_PATTERN, fetch_variable, query)


def get_results(df, max_num_rows):
    def convert_value(value):
        if value is None:
            return 'null'
        return str(value)

    header = df.columns
    contents = list(map(lambda row: list(map(convert_value, row)), df.take(max_num_rows + 1)))

    return header, contents