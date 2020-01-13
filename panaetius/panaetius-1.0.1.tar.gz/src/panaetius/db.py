from os import path, urandom
import hashlib
from typing import Tuple
import toml
import io

from pylite.simplite import Pylite

from panaetius.header import __header__ as __header__
import panaetius


class Mask:
    @property
    def hash(self):
        try:
            if not self._hash_exists:
                pass
        except AttributeError:
            self._hash = hashlib.pbkdf2_hmac(
                'sha256',
                self.entry[self.name].encode('utf-8'),
                self.salt,
                100000,
                dklen=12,
            )
            self._hash_exists = True
        finally:
            return self._hash

    @property
    def salt(self):
        self._salt = urandom(32)
        return self._salt

    @staticmethod
    def as_string(obj: bytes) -> str:
        return bytes.hex(obj)

    @staticmethod
    def fromhex(obj: str) -> bytes:
        return bytes.fromhex(obj)

    @staticmethod
    def _from_key(config_var) -> Tuple[str, str]:
        try:
            header, name = config_var.split('.')
        except ValueError:
            header = ''
            name = config_var
        return (header, name)

    def __init__(
        self, config_path: str, config_contents: dict, config_var: str
    ):
        self.table: str = __header__
        self.config_path = config_path
        self.config_contents = config_contents
        self.config_var = config_var.replace('.', '_')
        self.header = self._from_key(config_var)[0]
        self.name = self._from_key(config_var)[1]
        try:
            # If value is under a subsection
            self.entry = self.config_contents[self.table][self.header]
        except KeyError:
            # If value is under the main header
            self.entry = self.config_contents[self.table]

    def _get_database_file(self):
        self.database = self.config_path
        self.database += (
            f'.{self.table}.db'
            if self.config_path[-1] == '/'
            else f'/.{self.table}.db'
        )
        self.database = path.expanduser(self.database)
        return self

    def _open_database(self):
        self.database = Pylite(self.database)

    def _get_table(self):
        tables = [i[0] for i in self.database.get_tables()]
        if self.table not in tables:
            # panaetius.logger.debug(
            #     'Table not present in the database;'
            #     f'creating the table {self.table} now'
            # )
            self.database.add_table(
                f'{self.table}',
                Name='text',
                Hash='text',
                Salt='text',
                Value='text',
            )
        else:
            # panaetius.logger.debug('Table already exists in the database')
            pass
        self.table_name = self.table

    def _check_entries(self):
        var = self.database.get_items(self.table, f'Name="{self.config_var}"')
        if len(var) == 0:
            return False
        else:
            return True

    def _insert_entries(self):
        self.database.insert(
            self.table,
            self.config_var,
            self.as_string(self.hash),
            self.as_string(self.salt),
            self.entry[self.name],
        )

    def update_entries_in_db(self):
        self.database.remove(self.table, f'Name="{self.config_var}"')
        self._insert_entries()

    def run_query(self, query: str):
        cur = self.database.db.cursor()
        cur.execute(query)
        self.database.db.commit()
        self.result = cur.fetchall()
        return self

    def get_all_items(self, where_clause: str = None):
        if where_clause is not None:
            self.result = self.database.get_items(self.table, where_clause)
        else:
            self.result = self.database.get_items(self.table)
        return self

    def process(self):
        if not self._check_entries():
            # panaetius.logger.debug('does not exist')
            self._insert_entries()
            self._update_entries_in_config()
            self.get_all_items()
            # panaetius.logger.debug(f'returning: {self.result[0][3]}')
            return self.entry[self.name]
        else:
            self.get_all_items(f'Name="{self.config_var}"')
            if self.result[0][1] == self.entry[self.name]:
                # panaetius.logger.debug('exists and hash matches')
                # panaetius.logger.debug(f'returning: {self.result[0][3]}')
                return self.result
            else:
                # panaetius.logger.debug('exists and hash doesnt match')
                # panaetius.logger.debug(
                #     f'file_hash={self.entry[self.name]}, {self.result[0][1]}'
                # )
                self.update_entries_in_db()
                self._update_entries_in_config()
                self.get_all_items(f'Name="{self.config_var}"')
                # panaetius.logger.debug(f'returning: {self.result[0][3]}')
                return self.entry[self.name]

    def _open_config_file(self) -> io.TextIOWrapper:
        self.config_path += (
            '/config.toml' if self.config_path[-1] != '/' else 'config.toml'
        )
        c = open(path.expanduser(self.config_path), 'w')
        return c

    def _update_entries_in_config(self):
        self.entry.update({self.name: self.as_string(self.hash)})
        # panaetius.logger.debug(self.config_contents)
        # panaetius.logger.debug(self.entry)
        c = self._open_config_file()
        toml.dump(self.config_contents, c)
        c.close()

    def get_value(self):
        # print(f'key in db {self.config_var}')
        self._get_database_file()
        self._open_database()
        self._get_table()
        self.process()
        return self.result[0][3]
