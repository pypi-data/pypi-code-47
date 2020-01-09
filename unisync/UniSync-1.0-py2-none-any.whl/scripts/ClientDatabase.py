import sqlite3


def make_database():
    SQLconn = sqlite3.connect("FileDB.db")
    cursor = SQLconn.cursor()
    try:
        sqlite_create_table = '''CREATE TABLE Files (
                                id INTEGER PRIMARY KEY,
                                path TEXT NOT NULL UNIQUE,
                                modifytime TEXT NOT NULL);'''
        cursor.execute(sqlite_create_table)
        SQLconn.commit()
        cursor.close()
    except sqlite3.Error as error:
        a = 1
    #            print("An error has occured:", error)
    finally:
        if (SQLconn):
            SQLconn.close()


#                print("The SQLite connection is closed")

def GetEntry(filepath):
    sqliteConnection = None
    record = None
    try:
        sqliteConnection = sqlite3.connect('FileDB.db')
        cursor = sqliteConnection.cursor()
        sql_delete_query = """Select * from Files where path = ? """
        cursor.execute(sql_delete_query, (filepath, ))
        record = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        return None
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            return record


def removeRecords():
    sqliteConnection = None
    try:
        sqliteConnection = sqlite3.connect('FileDB.db')
        cursor = sqliteConnection.cursor()
        sql_delete_query = """DELETE from Files"""
        cursor.execute(sql_delete_query)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        pass
    finally:
        if (sqliteConnection):
            sqliteConnection.close()




def removeEntry(filepath):
    sqliteConnection = None
    try:
        sqliteConnection = sqlite3.connect('FileDB.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query = """DELETE from Files where path = ?"""
        cursor.execute(sql_delete_query, (filepath,))
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def isDatabaseEmpty(table):
    conn = None
    data = None
    try:
        conn = sqlite3.connect("FileDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Files;")
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        pass
    finally:
        if (conn):
            conn.close()
            if len(data) == 0:
                return True
            else:
                return False


def insertIntoTable(path, mtime):
    SQLconn = sqlite3.connect("FileDB.db")

    try:
        cursor = SQLconn.cursor()
        cursor.execute("insert into Files (path, modifytime) values (?, ?)", (path, mtime))
        SQLconn.commit()
        cursor.close()


    except sqlite3.Error as error:
        pass
    finally:
        if (SQLconn):
            SQLconn.close()




def executeQuery(Query):
    SQLconn = sqlite3.connect("FileDB.db")
    cursor = SQLconn.cursor()
    try:
        cursor.execute(Query)
        SQLconn.commit()
        cursor.close()
    except sqlite3.Error as error:
        pass
    finally:
        if (SQLconn):
            SQLconn.close()




def readSqliteTable(tablename):
    records = None
    SQLconn = sqlite3.connect("FileDB.db")
    cursor = SQLconn.cursor()
    try:
        sqlite_select_query = """SELECT * from """ + tablename
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()  # all data in table
        cursor.close()
    except sqlite3.Error as error:
        a = 1

    finally:
        if (SQLconn):
            SQLconn.close()
            return records
