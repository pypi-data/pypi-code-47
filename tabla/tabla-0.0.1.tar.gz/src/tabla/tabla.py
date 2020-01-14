from collections import namedtuple
from pathlib import Path
from typing import AnyStr, IO, List, Optional, Union

import pandas as pd
import numpy as np

HLINE = "\\hline\n"
EOL = "\\\\ \n"

TableColumn = namedtuple("TableColumn", ["name", "unit", "fmt", "print_name"])


class Table:
    """
    Create LaTeX table and write and compile to output directory

    Attributes
    ----------
    name: str
        Name of the table.
    columns: List[TableColumn]
        List of TableColumn objects defining column attributes.
    df: pd.DataFrame
        DataFrame with containing columns in `write_columns`
    extra_row_height: int
        number of points to increase table row height by
    dpi: int
        The resolution of the image to be generated.
    empty_str: str
        The string to use in place of null values.
    title: str
        Bolded title of table
    caption: str
        Caption explaining the table
    label: str
        label for linking to tabel in LaTeX
    notes: str
        Notes regarding table which appear below table
    header_units: bool
        Enable generation of a second header row with column units.
    centering: bool
        Center table on page
    tiny: bool
        use `tiny` LaTeX command
    adjustwidth: bool
        adjust table to use full width of the page
    """

    def __init__(
        self,
        name: str,
        columns: List[TableColumn],
        df: pd.DataFrame,
        extra_row_height: int = 0,
        dpi: int = 300,
        empty_str: str = "-",
        title: Optional[str] = None,
        caption: Optional[str] = None,
        label: Optional[str] = None,
        notes: Optional[str] = None,
        header_units: bool = True,
        centering: bool = True,
        tiny: bool = False,
        adjustwidth: bool = False,
    ):
        self.name = name
        self.columns = columns
        self.header_units = header_units
        self.df = df
        self.df_str = Table.string_dataframe(df, columns)
        self.adjustwidth = adjustwidth
        self.title = title
        self.caption = caption
        self.extra_row_height = extra_row_height
        self.label = label
        self.notes = notes
        self.dpi = dpi
        self.empty_str = empty_str
        self.centering = centering
        self.tiny = tiny

    def dumps(self) -> str:
        """Return table as a string"""
        return "".join(
            [self._create_header(), self._create_body(), self._create_footer()]
        )

    def dump(self, fileobj: Union[IO, Path, AnyStr]):
        """Write table to file"""
        if isinstance(fileobj, (str, bytes, Path)):
            with open(fileobj, "r") as fh:
                return self._dump(fh)
        else:
            return Table._dump(fileobj)

    def _dump(self, fh: IO) -> str:
        """Write string table output to file handler"""
        return fh.write(self.dumps)

    def _create_header(self) -> str:
        """Create LaTeX multirow table header"""

        head = "\\begin{table}[!ht]\n"

        if self.adjustwidth:
            head += "\\begin{adjustwidth}{-2.25in}{0in}\n"

        if self.tiny:
            head += "\\tiny\n"

        if self.centering:
            head += "\\centering\n"

        if self.title or self.caption:
            cap_str = "\\caption{"
            if self.title:
                cap_str += f"{self.title}"
            if self.caption:
                cap_str += self.caption
            cap_str + "}\n"
            head += cap_str

        if self.extra_row_height:
            head += f"\\setlength\\extrarowheight{{ {str(self.extra_row_height)} pt}}\n"

        head += f"\\begin{{tabular}}{{  {'c ' * len(self.columns)} }}\n"
        head += HLINE

        head += Table._creat_row([c.print_name for c in self.columns], bold=True)

        if self.header_units:
            head += Table._creat_row([c.unit for c in self.columns])

        head += HLINE

        return head

    def _create_body(self) -> str:
        """Create LaTeX table body"""
        rows = [Table._creat_row(elems.values) for _, elems in self.df_str.iterrows()]
        return "".join(rows + ["\n"])

    def _create_footer(self) -> str:
        """Create LaTeX table footer"""

        footer = "\\end{{tabular}} \n"

        if self.notes:
            footer += f"\\begin{{flushleft}} {self.notes} \n \\end{{flushleft}} \n"

        if self.label:
            footer += r"\label{" + self.label + "}\n"

        if self.adjustwidth:
            footer += "\\end{{adjustwidth}} \n"

        footer += "\\end{{table}} \n"

        return footer

    @staticmethod
    def string_dataframe(
        df: pd.DataFrame, columns: List[TableColumn], empty_str: str = "-"
    ):
        """
        Generate a new DataFrame with all column dtypes as `object` and values as strings

        Parameters
        ----------
        df: pd.DataFrame
            DataFrame to convert to strings.
        columns: List[TableColumn]
            List of TableColumn objects defining column attributes.
        empty_str: str
            String to replace null values with.

        Return
        ------
        df_str: pd.DataFrame
            DataFrame converted to strings
        """
        df_str = df.copy()

        for i, column in enumerate(columns):
            series = df[column.name]

            if np.issubdtype(series.dtype, np.datetime64):
                if column.fmt:
                    df_str[column.name] = series.apply(
                        pd.Timestamp.strftime, format=column.fmt
                    )
                else:
                    df_str[column.name] = series.apply(pd.Timestamp.isoformat, sep=" ")
            elif series.dtype == object:
                df_str[column.name] = series.astype(str)
            else:
                if column.fmt:
                    df_str[column.name] = series.apply(lambda s: column.fmt.format(s))
                else:
                    df_str[column.name] = series.astype(str)
            df_str[column.name].replace("nan", empty_str, inplace=True)

        return df_str

    @staticmethod
    def _creat_row(elems: List[str], bold: bool = False) -> str:
        """
        Create table row from list of strings

        Parameters
        ----------
        elems: List[str]
            List of strings to format to a LaTeX tabular row.
        bold: bool
            Bold strings when set to `True`.

        Returns
        -------
        str
            Header row stings concatenated into LaTeX tabular row.
        """
        fmt = " \\textbf{{ {} }} " if bold else " {} "

        return " ".join(["&".join([fmt] * len(elems)).format(*elems), EOL])
