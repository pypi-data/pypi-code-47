from typing import List, Dict

import dataset
from tqdm import tqdm

from .Template import DataBroker


class DataBrokerSqlite(DataBroker):
    """
    Class to handle saving FinanceJSON data into an
    sqlite database.
    """

    def __init__(self, sqliteuri):
        super(DataBrokerSqlite, self).__init__()
        self.db = dataset.connect(sqliteuri)

    def _create_index(self, table: dataset.table, indexList: List[str]):
        table.create_index(indexList, name='main')

    def save(self, data: List[Dict], collection: 'str', indexList: List[str]):
        table = self.db.create_table(collection)
        if not isinstance(data, list):
            data = [data]

        for row in tqdm(data):
            try:
                table.insert_ignore(row, indexList, ensure=True)
            except:
                print(",".join(indexList))
                print(row)
                break

        self._create_index(table, indexList)

    def load(self, collection: str, searchdict: Dict, *args, **kwargs):
        try:
            table = list(self.db.load_table(collection).find(**searchdict))
            for t in table:
                t.pop('id')
            return table
        except:
            print(f'Table {collection} not found')
