import os
import sys
import inspect
from PyQt5.QtWidgets import *
from pyHydraulic.utils import loadStylesheet
from pyHydraulic.node_editor_window import NodeEditorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = NodeEditorWindow()
    sys.exit(app.exec_())
