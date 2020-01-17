
def add_instance(name, kind):
    cur = conn.cursor()
    cur.execute('''INSERT INTO instance (name, kind) VALUES ('%s', '%s')''' % (name, kind))
