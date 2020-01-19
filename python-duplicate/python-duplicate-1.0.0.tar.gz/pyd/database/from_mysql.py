# Third party import
import pymysql

# Local import
from .utils import MySQL


class FromMySQL(MySQL):
    """
    Handle search of duplicate or unique item inside a MySQL table

    :param dict info_dict: Param to connect to MySQL
    :param str table: Param to select the right table
    :param str column: Param to search duplicate or unique on
    """

    def __init__(self, info_dict: dict, table: str, column: str) -> None:
        MySQL.__init__(self, table, column)
        self.info_dict = info_dict
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        self.pk = self.get_pk_name()

    def connect(self) -> object:
        """
        Connect to MySQL (with information given to the class)

        :return: PyMySQL connection object
        """
        connection = pymysql.connect(
            host=self.info_dict.get('HOST'),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT')
        )
        return connection

    def disconnect(self) -> None:
        """
        Disconnect of MySQL
        """
        if self.connection is not None and self.connection.open:
            self.connection.close()

    def get_pk_name(self) -> str:
        """

        :return: Primary key name
        """
        self.cursor.execute(self.select_pk_name_query())
        rows = self.cursor.fetchall()
        if len(rows) > 1:  # instead of self.cursor.rowcount for test ease
            msg = f"The table '{self.table}' contains more than one primary key"
            raise ValueError(msg)
        return rows[0][0]

    def select_duplicate(self, rows_list: bool = False) -> list:
        """

        :param rows_list: Boolean to return list of pk or rows
        :return: Duplicate entries
        """
        if rows_list:
            self.cursor.execute(self.select_duplicate_query())
            return self.cursor.fetchall()

        self.cursor.execute(self.select_duplicate_pk_query(self.pk))
        return [row[0] for row in self.cursor.fetchall()]

    def select_unique(self, rows_list: bool = False) -> list:
        """

        :param rows_list: Boolean to return list of pk or rows
        :return: Unique entries
        """
        if rows_list:
            self.cursor.execute(self.select_unique_query())
            return self.cursor.fetchall()

        self.cursor.execute(self.select_unique_pk_query(self.pk))
        return [row[0] for row in self.cursor.fetchall()]
