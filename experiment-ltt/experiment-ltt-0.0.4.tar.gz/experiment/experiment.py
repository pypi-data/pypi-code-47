
def _create_default_instance_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE instance (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT,
            kind TEXT)''')

def _create_default_method_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE method(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT)''')

def _create_default_iteration_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE iteration(
            id INT AUTO_INCREMENT PRIMARY KEY,
            best DOUBLE,
            mean DOUBLE,
            std DOUBLE,
            best_solution MEDIUMBLOB,
            num_iteration INT,
            num_evaluation INT,
            seed INT)''')

def _create_summary_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE summary(
            method_id INT REFERENCES method(id),
            instance_id INT REFERENCES instance(id),
            iteration_id INT REFERENCES iteration(id))''')

def create_experiment(conn, experiment_name):
    '''Create database and tables for the experiment.
    Create a table "experiment" that contain the experimental
    summarization

    Parameters:
        - conn (object): mysql connection
        - experiment_name (str): name of the experiment
    '''
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS %s' % experiment_name)
    conn.select_db(experiment_name)
    _create_default_instance_table(conn)
    _create_default_method_table(conn)
    _create_default_iteration_table(conn)
    _create_summary_table(conn)

def drop_experiment(conn, experiment_name):
    '''Drop database contain experimental results

    Parameters:
        - conn (object): mysql connection
        - experiment_name (str): name of the experiment
    '''
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS %s' % experiment_name)

