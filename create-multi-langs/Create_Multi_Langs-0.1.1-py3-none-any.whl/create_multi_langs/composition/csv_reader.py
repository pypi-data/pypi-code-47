from __future__ import absolute_import
import pandas as pd
from typing import List

FIELD = "_field"
NOTE = "_note"


class CSVReader:
    def __init__(self, csv_file: str, field_wrapper=lambda x: x, sep=','):
        self._df: pd.DataFrame = pd.read_csv(csv_file, sep=sep)
        self._PRESERVED_COLUMN_NAMES: List[str] = [FIELD, NOTE]
        self._field_wrapper = field_wrapper

    def fields(self) -> List[str]:
        return [self._field_wrapper(field) for field in self._df[FIELD]]

    def lang_codes(self) -> List[str]:
        out = []
        for column_name in self._df.columns:
            if column_name not in self._PRESERVED_COLUMN_NAMES:
                out.append(column_name)
        return out

    def rows(self) -> List[dict]:
        return [dict(row) for _, row in self._df.iterrows()]

    def field_notes(self) -> dict:
        out = {}
        for _, row in self._df.iterrows():
            field = self._field_wrapper(row[FIELD])
            out[field] = row[NOTE]
        return out

    def field_values(self, lang_code: str) -> dict:
        out = {}
        for _, row in self._df.iterrows():
            field = self._field_wrapper(row[FIELD])
            out[field] = row[lang_code]
        return out

    def default_lang_code(self) -> str:
        return self.lang_codes()[0]
