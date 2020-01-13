import os

from pandas import DataFrame
from randomcsv.Column import Column
from randomcsv.FileUtils import write


class CsvGenerator:
    """
    Main Class, used to generate CSV files and pandas.DataFrame

    Methods
    -------
    add_column: Configure Columns by adding Column Objects.
    calculate_column: Add further Columns by calculating values based on existing columns

    Example
    -------
    >>> generator = CsvGenerator(out_dir='output')
    >>> generator.add_column(StringColumn("Names"))
    >>> generator.add_column(IntColumn("Integers", start=1))
    >>> generator.add_column(RandomNumberColumn("Random"))
    >>> generator.add_column(CategoryColumn("Categories", [1, 2, 3, 4]))
    >>> generator.calculate_column("Calculated", ["Integers", "Categories"], lambda number, category: f'{number}-{category}')
    >>> generator.generate_data_frame(2)
         Names  Integers    Random Categories Calculated
    0   Hannes         1  0.169415          4        1-4
    1  Charlos         2  0.493438          1        2-1

    >>> generator.create_csv(2, 'test_data.txt')
    content of file './output/test_data.txt' (relative to script)
    Names,Integers,Random,Categories,Calculated
    Hannes,1,0.9508151821959357,3,1-3
    Charlos,2,0.9761199341020395,2,2-2

    Note
    ----
    Content differs every time generate_data_frame or create_csv are called, except all columns are provided an value
    for random_state
    """

    def __init__(self, out_dir=''):
        self.columns = []
        self.instructions = []
        self.out_dir = out_dir

    def add_column(self, column: Column):
        """
        Add column object.
        Note: Data generation happens later when calling generate_data_frame or create_csv

        Example
        -------
        generator.add(RandomNumberColumn("MyRandomNumbers", low=10, high=20))
        """
        self.columns.append(column)

    def calculate_column(self, column_name, source_columns, function):
        """
        Adds column, which is calculated using values from other columns.

        The order of source_columns and the parameters of the function must match.
        The source_columns must exist during generation, but can be added after the calculated column, except when the
        source column is also calculated.

        Parameter
        ---------
        :param column_name: Name of the column
        :param source_columns: A List of column names. Must match parameters of function.
        :param function: A function or lambda accepting values of type and order of source_columns.

        Example
        -------
        generator.add_column(IntColumn('Numbers', start=1))
        generator.add_column(CategoryColumn('Characters', ['A', 'B', 'C']))
        generator.calculate_column('Calculated', ['Numbers', 'Characters'], lambda number, character: number * character)
        """
        self.instructions.append(Instruction(column_name, source_columns, function))

    def generate_data_frame(self, count):
        """
        Generates a pandas DataFrame with the columns, which have been added, and <count> rows.

        Parameters
        ----------
        :param count: Number of rows which will be generated
        :return: A DataFrame with 'count' rows
        """
        data = DataFrame()
        for column in self.columns:
            data[column.name] = column.generate_entries(count)
        for instruction in self.instructions:
            data[instruction.column_name] = data.apply(instruction.create_row_function(), axis=1)
        return data

    def create_csv(self, count, file_name, delimiter=','):
        """
        Generates the configured DataFrame with <count> rows and writes it to a file with path '<out_dir>/<file_name>'

        Parameters
        ----------
        :param count: Number of rows which will be generated
        :param file_name: File name of generated CSV file. Path can be specified. Example 'output/date.csv'
        :param delimiter: Character, which separates values (default ',')
        """
        data_frame: DataFrame = self.generate_data_frame(count)
        file_path = os.path.join(self.out_dir, file_name)
        write(file_path, data_frame.to_csv(sep=delimiter, index=False))


class Instruction:
    def __init__(self, column_name, source_columns, function):
        self.column_name = column_name
        self.source_columns = source_columns
        self.function = function

    def create_row_function(self):
        def row_function(row):
            arguments = [row[source] for source in self.source_columns]
            return self.function(*arguments)

        return row_function


def __extract_arguments(row, source_columns):
    return [row[column] for column in source_columns]
