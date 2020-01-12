import sqlite3

CURRENT_DB_VERSION = 1


def upgrade_db(from_version, db_conn):
    print("Current DB version: " + str(from_version))
    print("Most curent DB version: " + str(CURRENT_DB_VERSION))

    if(from_version == CURRENT_DB_VERSION):
        print("Database is already up to date!")
        return

    # Iterate over the upgrade functions until we reach the current version
    incremental_upgrade_funcs = [
        zero_to_one,
        # one_to_two,
        # two_to_three,
        # etc...
    ]
    for upgrade_func in incremental_upgrade_funcs[from_version:CURRENT_DB_VERSION]:
        upgrade_func(db_conn)


def create_current_db_version(db_conn):
    c = db_conn.cursor()
    c.execute("""Create TABLE nodes (id integer PRIMARY KEY, name TEXT, path TEXT)""")
    c.execute("""Create TABLE links (id INTEGER PRIMARY KEY, node_id1 INTEGER, node_id2 INTEGER, name TEXT)""")
    c.execute("""Create TABLE metadata (idx INTEGER PRIMARY KEY, key TEXT, value TEXT)""")
    c.execute("""INSERT INTO metadata (key, value) VALUES ("node_links_version", 1)""")
    db_conn.commit()
    return CURRENT_DB_VERSION


def zero_to_one(db_conn):
    c = db_conn.cursor()
    c.execute("""Create TABLE metadata (idx INTEGER PRIMARY KEY, key TEXT, value TEXT)""")
    c.execute("""INSERT INTO metadata (key, value) VALUES ("node_links_version", 1)""")
    db_conn.commit()
    return 1
