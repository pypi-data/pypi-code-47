
def add_instance(conn, name, kind):
    cur = conn.cursor()
    cur.execute('''INSERT INTO instance (name, kind) VALUES ('%s', '%s')''' % (name, kind))
