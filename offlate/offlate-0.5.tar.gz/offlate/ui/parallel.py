#   Copyright (c) 2019 Julien Lepiller <julien@lepiller.eu>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
####

from PyQt5.QtCore import *
from ..formats.formatException import UnsupportedFormatException
from ..systems.systemException import ProjectNotFoundSystemException

class RunnableCallback:
    def progress(self, amount):
        if int(round(amount)) > self.oldamount:
            self.oldamount = int(round(amount))
            self.signals.progress.emit(self.name, amount)

    def project_exists(self):
        self.error = self.parent.tr('A project with the same name already exists. \
The new project was not created. You should first remove the same-named project.')

    def project_present(self, directory):
        self.error = self.parent.tr('Your filesystem contains a same-named \
directory for your new project. The new project was not created. You should \
first remove the same-named directory: "{}".'.format(directory))

    def project_error(self, error):
        if isinstance(error, UnsupportedFormatException):
            self.error = self.parent.tr('The project you added uses the {} format, \
but it is not supported yet by Offlate. You can try to update the application, \
or if you are on the latest version already, report it as a bug.'.format(error.unsupportedFormat))
        elif isinstance(error, ProjectNotFoundSystemException):
            self.error = self.parent.tr('The project {} you added could not be found \
in the translation platform you selected. Did you make a typo while entering the \
name or other parameters?'.format(error.projectNotFound))
        else:
            self.error = self.parent.tr('An unexpected error occured while \
fetching the project: {}. You should report this as a bug.'.format(str(error)))

class RunnableSignals(QObject):
    finished = pyqtSignal(str)
    progress = pyqtSignal(str, int)
    error = pyqtSignal(str, str)
    restart_required = pyqtSignal(str, str, int, dict, str)
