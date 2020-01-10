# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
from ..constants import database_table_experiment


class ExperimentGeneric(object):
    """Collection of methods used by all experiments"""

    database_table = database_table_experiment

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentGeneric.database_table) +
                 "(experiment_id text not null, date text not null, time text, type_generic text not null, type_specific text not null, hardware text not null " +
                 ", primary key(experiment_id))")

    @staticmethod
    def has_record(database, experiment_id):
        try:
            res = database.has_record(ExperimentGeneric.database_table, experiment_id=experiment_id)
        except:
            res = False
        return res

    @staticmethod
    def hardware(database, experiment_id):
        return database.query("select hardware from " + database.table("experiment") +
                              " where experiment_id=:experiment_id",
                              experiment_id=experiment_id).first().hardware

    @staticmethod
    def store(database, experiment_id, time, type_generic, type_specific, hardware):
        if ExperimentGeneric.has_record(database, experiment_id):
            return

        date = time.split()[0]
        t = time.split()[1]
        database.query("INSERT INTO " + database.table(ExperimentGeneric.database_table) +
                            "(experiment_id, date, time, type_generic, type_specific, hardware) " +
                            "VALUES(:experiment_id, :date, :time, :typeg, :types, :hardware)",
                            experiment_id=experiment_id, date=date, time=t,
                            typeg=type_generic, types=type_specific, hardware=hardware)


    def __init__(self, db):
        self.database = db
