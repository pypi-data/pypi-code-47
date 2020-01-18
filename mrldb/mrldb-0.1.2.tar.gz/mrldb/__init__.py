__all__=["MrlDBMsql", "MrlDBCassandra", "MrlDBSqlite", "MrlDBCluster", "mdbcl", "mdbstr", "MrlDBMsqlAsync"]
from .db_types import *
from .mrl_cluster import *
from .dbutils import dbutils as mdbstr
##version#start##
__version__='0.1.2'
##version#end##
__doc__=f"""mrldb v{__version__} by Rémi "Mr e-RL" LANGDORPH
Copyright (c) 2019 Rémi LANGDORPH - mrerl@warlegend.net
under MIT License (https://github.com/merlleu/mrldb/blob/master/LICENSE)
"""
