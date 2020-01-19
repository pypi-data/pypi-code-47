import pymysql

def add_iteration(conn, config, **kwargs):
    '''Add data from every iteration of each method for each instance

    Parameter:
        - conn (object): mysql connection
        - config (dict): configuration of experiment
        - kwargs:
            + method_id
            + instance_id
            + best
            + mean
            + std
            + best_solution
            + num_iteration
            + num_evaluation
            + seed
    '''
    cur = conn.cursor()
    fields = ','.join(kwargs.keys())
    values = []
    for _ in kwargs.values():
        if type(_) == str:
            values.append("'%s'" % _)
        else:
            values.append(str(_))
    values = ','.join(values)
    query = 'INSERT INTO iteration (%s) VALUES (%s)' % (fields, values)
    try:
        cur.execute(query)
        conn.commit()
    except pymysql.err.IntegrityError:
        if config['verbose']:
            print('[iteration|error] add_iteration(%s), reason: iteration duplicated' % values)
    else:
        if config['verbose']:
            print('[iteration|ok] add_iteration(%s)' % values)

def get_iteration(conn, config, **kwargs):
    '''Get data from every interation of each method for each instance

    Parameter:
        - conn (object): mysql connection
        - config (dict): configuration of experiment
        - kwargs:
            + method_id
            + instance_id
    '''
    cur = conn.cursor()
    values = []
    for key in kwargs:
        values.append('%s=%d' % (key, kwargs[key]))
    query = '''SELECT * FROM iteration WHERE %s ''' % ' AND '.join(values)
    cur.execute(query)
    for _ in cur.fetchall():
        yield _
























