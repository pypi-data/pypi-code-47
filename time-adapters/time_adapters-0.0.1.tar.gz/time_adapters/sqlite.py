import sqlite3

from arrow import Arrow



sqlite3.register_adapter(
    Arrow,
    lambda x: sqlite3.adapt(x.to('UTC').datetime)
)

# https://docs.python.org/3.7/library/sqlite3.html#sqlite3.register_adapter
