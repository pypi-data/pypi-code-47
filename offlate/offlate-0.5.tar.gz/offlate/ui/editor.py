#   Copyright (c) 2018 Julien Lepiller <julien@lepiller.eu>
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

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .spellcheckedit import SpellCheckEdit
from .tagclickedit import TagClickEdit
from .parallel import RunnableCallback, RunnableSignals

import math
import platform
import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from time import sleep

class ProjectTab(QTabWidget):
    def __init__(self, parent = None):
        super(ProjectTab, self).__init__(parent)

class Interface:
    def __init__(self):
        self.value = None

    def ok(self):
        self.value = self.qd.textValue()

    def askPassword(self):
        self.qd = QInputDialog()
        self.qd.setLabelText(self.qd.tr("Please enter your password:"))
        self.qd.setTextEchoMode(QLineEdit.Password)
        self.qd.accepted.connect(self.ok)
        self.qd.exec_()
        return self.value

    def gitlabTokenNotFound(self, server):
        self.qd = QErrorMessage()
        self.qd.showMessage(self.qd.tr("Token for {} not found. Have you added this server to your settings?.").format(server))
        self.qd.exec_()

    def gitlabTokenBranchError(self, branch):
        self.qd = QErrorMessage()
        self.qd.showMessage(self.qd.tr("Error while creating branch {}.").format(branch))
        self.qd.exec_()

    def githubBranchError(self, branch):
        self.qd = QErrorMessage()
        self.qd.showMessage(self.qd.tr("Error while creating branch {}.").format(branch))
        self.qd.exec_()

class ProjectView(QWidget):
    translationModified = pyqtSignal()

    def __init__(self, project, showTranslated = True, showUntranslated = True,
                showFuzzy = True, monospace = False, parent = None):
        super(ProjectView, self).__init__(parent)
        self.project = project
        self.content = self.project.content()
        self.currentContent = list(self.content.keys())[0]
        self.showTranslated = showTranslated
        self.showUntranslated = showUntranslated
        self.showFuzzy = showFuzzy
        self.monospace = monospace
        self.fuzzyColor = QBrush(QColor(255, 127, 80))
        self.emptyColor = QBrush(QColor(255, 240, 235))
        self.threadpool = QThreadPool()
        self.initUI()

    def updateContent(self):
        self.treeWidget.clear()
        items = []
        for entry in self.content[self.currentContent]:
            if entry.isObsolete():
                continue
            cont = False
            if self.showTranslated and entry.isTranslated():
                cont = True
            if self.showUntranslated and not entry.isTranslated():
                cont = True
            if self.showFuzzy and entry.isFuzzy():
                cont = True
            if not cont:
                continue
            txt = None
            i = 0
            while txt is None:
                txt = entry.msgids[i] if isinstance(entry.msgids, list) else \
                        list(entry.msgids.items())[i][1]
                i = i + 1
                if i >= len(entry.msgids) and txt is None:
                    txt = ''
            trans = None
            i = 0
            while trans is None:
                trans = entry.msgstrs[i] if isinstance(entry.msgstrs, list) else \
                        list(entry.msgstrs.items())[i][1]
                i = i + 1
                if i >= len(entry.msgstrs) and trans is None:
                    trans = ''

            item = QTreeWidgetItem([txt.replace('\n', ' '),
                                    trans.replace('\n', ' ')])
            if entry.isFuzzy():
                item.setForeground(1, self.fuzzyColor)
            if not entry.isTranslated():
                item.setBackground(1, self.emptyColor)
            item.setFont(0, QFont("sans-serif", 10))
            item.setFont(1, QFont("sans-serif", 10))
            item.setSizeHint(0, QSize(-1, 22))
            item.setData(0, Qt.UserRole, entry)
            items.append(item)
        self.treeWidget.insertTopLevelItems(0, items)
        self.translationModified.emit()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        model = QStandardItemModel()
        self.treeWidget = QTreeWidget()
        self.treeWidget.setColumnCount(2)
        self.msgid = QTextEdit()
        self.msgid.setReadOnly(True)
        self.msgstr = SpellCheckEdit(self.project.lang)
        self.filechooser = QComboBox()
        for project in list(self.content.keys()):
            self.filechooser.addItem(project)
        self.filechooser.currentIndexChanged.connect(self.changefile)
        self.openExternal = QPushButton(self.tr("Open in external editor"))
        self.openExternal.clicked.connect(self.editExternal)

        self.buttons = QVBoxLayout()
        self.copyButton = QPushButton(self.tr("Copy"))
        self.copyButton.clicked.connect(self.copy)
        self.buttons.addWidget(self.copyButton)

        if self.filechooser.count() > 1:
            vbox.addWidget(self.filechooser)

        vbox.addWidget(self.openExternal)

        self.updateContent()
        vbox.addWidget(self.treeWidget, 4)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.msgid)
        self.hbox.addLayout(self.buttons)
        self.hbox.addWidget(self.msgstr)
        vbox.addLayout(self.hbox, 1)
        size = self.treeWidget.size()
        self.treeWidget.setColumnWidth(0, size.width()/2)
        self.treeWidget.currentItemChanged.connect(self.selectItem)

    def editExternal(self):
        self.project.save()
        self.treeWidget.setEnabled(False)
        mfiles = self.project.getExternalFiles()
        files = []
        for f in mfiles:
            files.extend(f)

        worker = []
        for f in files:
            worker.append(ExternalRunnable(f))

        worker2 = WatchRunnable(self.project, len(worker))
        worker2.signals.finished.connect(self.editedExternals)
        worker2.signals.progress.connect(self.intermediateReloadContent)
        for i in range(0, len(worker)):
            worker[i].signals.finished.connect(worker2.stop)
        self.threadpool.start(worker2)
        for i in range(0, len(worker)):
            self.threadpool.start(worker[i])

    def editedExternals(self, name):
        self.reloadContent()
        self.treeWidget.setEnabled(True)

    def intermediateReloadContent(self, name, progress):
        self.reloadContent()

    def reloadContent(self):
        self.project.reload()
        self.content = self.project.content()
        self.updateContent()

    def changefile(self):
        self.currentContent = list(self.content.keys())[self.filechooser.currentIndex()]
        self.updateContent()

    def nextItem(self):
        index = self.treeWidget.currentIndex()
        nextItem = self.treeWidget.itemFromIndex(self.treeWidget.indexBelow(index))
        self.treeWidget.setCurrentItem(nextItem)

    def previousItem(self):
        index = self.treeWidget.currentIndex()
        nextItem = self.treeWidget.itemFromIndex(self.treeWidget.indexAbove(index))
        self.treeWidget.setCurrentItem(nextItem)

    def copy(self):
        if self.msgstr.__class__.__name__ == "SpellCheckEdit":
            text = self.msgid.toPlainText()
            self.msgstr.setText(text)
        else:
            text = self.msgid.currentWidget().toPlainText()
            self.msgstr.currentWidget().setText(text)

    def copyTag(self, tag):
        tag = tag.toDisplayString()[1:]
        tag = unquote(tag)
        if self.msgstr.__class__.__name__ == "SpellCheckEdit":
            self.msgstr.insertPlainText(tag)
            self.msgstr.setFocus(True)
        else:
            self.msgstr.currentWidget.insertPlainText(tag)
            self.msgstr.currentWidget.setFocus(True)

    def selectItem(self, current, old):
        if current == None:
            return
        if self.msgstr.__class__.__name__ == "SpellCheckEdit":
            self.msgstr.clearFocus()
        else:
            self.msgstr.currentWidget().clearFocus()
        data = current.data(0, Qt.UserRole)
        self.hbox.removeWidget(self.msgid)
        self.hbox.removeItem(self.buttons)
        self.hbox.removeWidget(self.msgstr)
        self.msgid.deleteLater()
        self.msgstr.deleteLater()

        font = "monospace" if self.monospace else "sans-serif"
        focuser = None

        if isinstance(data.msgstrs, dict):
            self.msgid = QTabWidget()
            self.msgstr = QTabWidget()
            for k in data.msgids:
                edit = TagClickEdit()
                edit.setFont(QFont(font))
                edit.setReadOnly(True)
                edit.setText(data.msgids[k])
                edit.createLinks()
                edit.anchorClicked.connect(self.copyTag)
                self.msgid.addTab(edit, self.tr(k))
            i = 0
            for k in data.msgstrs:
                form = SpellCheckEdit(self.project.lang)
                form.setFont(QFont(font))
                form.setText(data.msgstrs[k])
                form.textChanged.connect(self.modify)
                self.msgstr.addTab(form, self.tr(k))
                if i == 0:
                    focuser = form
                i=i+1
        elif data.isPlural():
            self.msgid = QTabWidget()
            self.msgstr = QTabWidget()
            singular = TagClickEdit()
            singular.setFont(QFont(font))
            singular.setReadOnly(True)
            singular.setText(data.msgids[0])
            singular.createLinks()
            singular.anchorClicked.connect(self.copyTag)
            plural = TagClickEdit()
            plural.setFont(QFont(font))
            plural.setReadOnly(True)
            plural.setText(data.msgids[1])
            plural.createLinks()
            plural.anchorClicked.connect(self.copyTag)
            self.msgid.addTab(singular, self.tr("Singular"))
            self.msgid.addTab(plural, self.tr("Plural"))
            i = 0
            for msgstr in data.msgstrs:
                form = SpellCheckEdit(self.project.lang)
                form.setFont(QFont(font))
                form.setText(msgstr)
                form.textChanged.connect(self.modify)
                self.msgstr.addTab(form, str(i))
                if i == 0:
                    focuser = form
                i=i+1
        elif len(data.msgstrs) > 1:
            self.msgid = QTabWidget()
            self.msgstr = QTabWidget()
            i = 0
            for msgid in data.msgids:
                edit = TagClickEdit()
                edit.setFont(QFont(font))
                edit.setReadOnly(True)
                edit.setText(msgid)
                edit.createLinks()
                edit.anchorClicked.connect(self.copyTag)
                self.msgid.addTab(edit, str(i))
                i=i+1
            i = 0
            for msgstr in data.msgstrs:
                form = SpellCheckEdit(self.project.lang)
                form.setFont(QFont(font))
                form.setText(msgstr)
                form.textChanged.connect(self.modify)
                self.msgstr.addTab(form, str(i))
                if i == 0:
                    focuser = form
                i=i+1
        else:
            self.msgid = TagClickEdit()
            self.msgid.setFont(QFont(font))
            self.msgid.setReadOnly(True)
            self.msgid.setText(data.msgids[0])
            self.msgid.createLinks()
            self.msgid.anchorClicked.connect(self.copyTag)
            self.msgstr = SpellCheckEdit(self.project.lang)
            self.msgstr.setFont(QFont(font))
            self.msgstr.setText(data.msgstrs[0])
            self.msgstr.textChanged.connect(self.modify)
            focuser = self.msgstr
        self.hbox.addWidget(self.msgid)
        self.hbox.addLayout(self.buttons)
        self.hbox.addWidget(self.msgstr)
        focuser.setFocus()

    def modify(self):
        item = self.treeWidget.currentItem()
        data = item.data(0, Qt.UserRole)
        if self.msgstr.__class__.__name__ == "SpellCheckEdit":
            msgstr = self.msgstr.toPlainText()
            data.update(0, msgstr)
            item.setText(1, msgstr.replace('\n', ' '))
        else:
            i = 0
            for msgstr in (data.msgstrs if isinstance(data.msgstrs, list) else \
                                    list(data.msgstrs.keys())):
                data.update(i if isinstance(data.msgstrs, list) else msgstr,
                        self.msgstr.widget(i).toPlainText())
                i=i+1
            item.setText(1, data.get(0).replace('\n', ' '))
        item.setForeground(1, QBrush())
        if data.isTranslated():
            item.setBackground(1, QBrush())
        else:
            item.setBackground(1, self.emptyColor)
        self.translationModified.emit()


    def save(self):
        self.project.save()

    def send(self):
        self.project.save()
        self.project.send(Interface())

    def askmerge(self, msgid, oldstr, newstr):
        # TODO: Actually do something more intelligent
        return newstr

    def update(self, callback=None):
        self.project.save()
        self.project.update(self.askmerge, callback)
        self.content = self.project.content()
        self.updateContent()

    def filter(self, showTranslated, showUntranslated, showFuzzy):
        self.showTranslated = showTranslated
        self.showUntranslated = showUntranslated
        self.showFuzzy = showFuzzy
        self.updateContent()

    def setFont(self, monospace):
        self.monospace = monospace
        current = self.treeWidget.currentItem()
        self.selectItem(current, current)

class EditorWindow(QMainWindow):
    def __init__(self, projectManagerWindow, manager):
        super().__init__()
        self.manager = manager
        self.projectManagerWindow = projectManagerWindow
        self.threadpool = QThreadPool()
        self.initUI()

    def initOpenProjects(self, menu):
        l = self.manager.listProjects()
        for p in l:
            name = p['name']
            act = QAction(name, self) 
            act.triggered.connect((lambda name: (lambda : self.open(name)))(name))
            menu.addAction(act)

    def open(self, name):
        try:
            project = self.manager.getProject(name)
        except Exception:
            self.qd = QErrorMessage()
            self.qd.showMessage(self.tr("Unsupported / Unknown project"))
            self.qd.exec_()
            return
        tab = ProjectView(project,
            showTranslated = self.showTranslatedAct.isChecked(),
            showUntranslated = self.showUntranslatedAct.isChecked(),
            showFuzzy = self.showFuzzyAct.isChecked(),
            monospace = self.monospaceAct.isChecked())
        tab.translationModified.connect(self.count)
        self.tabs.addTab(tab, name)
        self.count()

    def count(self, item = -1):
        widget = self.tabs.currentWidget()
        content = widget.content[widget.currentContent]
        total = 0
        translated = 0
        for d in content:
            total += 1
            if d.isTranslated() and not d.isFuzzy():
                translated += 1
        percent = 100 if total == 0 else math.floor(1000 * translated / total)/10
        self.countLabel.setText(self.tr("{} translated on {} total ({}%).", "", translated).format(translated, total, percent))

    def save(self):
        self.tabs.currentWidget().save()

    def manage(self):
        self.projectManagerWindow.show()

    def new(self):
        self.projectManagerWindow.new()

    def send(self):
        self.setLabels(self.tr("Uploading {}...").format(self.tabs.currentWidget().project.name))
        worker = UploadRunnable(self.tabs.currentWidget())
        worker.signals.finished.connect(self.sent)
        self.threadpool.start(worker)

    def sent(self, name):
        self.setLabels(self.tr("Finished uploading {}!").format(name))

    def update(self):
        self.setLabels(self.tr("Updating {}...").format(self.tabs.currentWidget().project.name))
        self.setProgresses(0)
        worker = UpdateRunnable(self.tabs.currentWidget())
        worker.signals.finished.connect(self.updated)
        worker.signals.progress.connect(self.reportProgress)
        self.threadpool.start(worker)

    def updated(self, name):
        self.manager.update()
        self.manager.writeProjects()
        self.setProgresses(0, False)
        self.setLabels(self.tr("Finished updating {}!").format(name))

    def reportProgress(self, name, progress):
        self.setProgresses(progress)

    def setLabels(self, value):
        self.actionLabel.setText(value)
        self.projectManagerWindow.projectManagerWidget.actionLabel.setText(value)

    def setProgresses(self, progress, enable=True):
        self.actionProgress.setEnabled(enable)
        self.actionProgress.setValue(progress)
        self.projectManagerWindow.projectManagerWidget.actionProgress.setEnabled(enable)
        self.projectManagerWindow.projectManagerWidget.actionProgress.setValue(progress)

    def closeProject(self):
        self.tabs.removeTab(self.tabs.currentIndex())

    def settings(self):
        self.projectManagerWindow.settings()

    def filter(self):
        for i in range(0, self.tabs.count()):
            self.tabs.widget(i).filter(
                self.showTranslatedAct.isChecked(),
                self.showUntranslatedAct.isChecked(),
                self.showFuzzyAct.isChecked())

    def setFont(self):
        for i in range(0, self.tabs.count()):
            self.tabs.widget(i).setFont(self.monospaceAct.isChecked())

    def previousItem(self):
        self.tabs.currentWidget().previousItem()

    def nextItem(self):
        self.tabs.currentWidget().nextItem()

    def initUI(self):
        # Build menu
        exitAct = QAction(QIcon('exit.png'), self.tr('Exit'), self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip(self.tr('Exit application'))
        exitAct.triggered.connect(qApp.quit)

        saveAct = QAction(QIcon('save.png'), self.tr('Save'), self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip(self.tr('Save current project'))
        saveAct.triggered.connect(self.save)

        newAct = QAction(QIcon('new.png'), self.tr('New'), self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip(self.tr('New project'))
        newAct.triggered.connect(self.new)

        manageAct = QAction(QIcon('settings.png'),
                self.tr('Manage Projects'), self)
        manageAct.setShortcut('Ctrl+M')
        manageAct.setStatusTip(self.tr('Open project manager'))
        manageAct.triggered.connect(self.manage)

        updateAct = QAction(QIcon('download.png'), self.tr('Update'), self)
        updateAct.setShortcut('Ctrl+U')
        updateAct.setStatusTip(self.tr('Get modifications from upstream'))
        updateAct.triggered.connect(self.update)

        closeAct = QAction(QIcon('close.png'), self.tr('Close'), self)
        closeAct.setStatusTip(self.tr('Close current project'))
        closeAct.triggered.connect(self.closeProject)

        sendAct = QAction(QIcon('upload.png'), self.tr('Send'), self)
        sendAct.setShortcut('Ctrl+E')
        sendAct.setStatusTip(self.tr('Send modifications upstream'))
        sendAct.triggered.connect(self.send)

        settingsAct = QAction(QIcon('settings.png'), self.tr('Settings'), self)
        settingsAct.setShortcut('Ctrl+P')
        settingsAct.setStatusTip(self.tr('Set parameters'))
        settingsAct.triggered.connect(self.settings)

        self.showTranslatedAct = QAction(self.tr('Show Translated'), self, checkable=True)
        self.showTranslatedAct.setChecked(True)
        self.showTranslatedAct.triggered.connect(self.filter)
        self.showFuzzyAct = QAction(self.tr('Show Fuzzy'), self, checkable=True)
        self.showFuzzyAct.setChecked(True)
        self.showFuzzyAct.triggered.connect(self.filter)
        self.showUntranslatedAct = QAction(self.tr('Show Empty Translation'), self, checkable=True)
        self.showUntranslatedAct.setChecked(True)
        self.showUntranslatedAct.triggered.connect(self.filter)
        self.monospaceAct = QAction(self.tr('Use a monospace font'), self, checkable=True)
        self.monospaceAct.setChecked(False)
        self.monospaceAct.triggered.connect(self.setFont)

        self.previousShortcut = QShortcut(QKeySequence("Ctrl+Up"), self)
        self.previousShortcut.activated.connect(self.previousItem)

        self.previous2Shortcut = QShortcut(QKeySequence("Ctrl+Shift+Return"), self)
        self.previous2Shortcut.activated.connect(self.previousItem)

        self.nextShortcut = QShortcut(QKeySequence("Ctrl+Down"), self)
        self.nextShortcut.activated.connect(self.nextItem)

        self.next2Shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        self.next2Shortcut.activated.connect(self.nextItem)

        self.countLabel = QLabel()
        self.actionLabel = QLabel()
        self.actionProgress = QProgressBar()
        self.actionProgress.setEnabled(False)
        self.statusBar()
        self.statusBar().addWidget(self.countLabel)
        self.statusBar().addWidget(self.actionLabel)
        self.statusBar().addWidget(self.actionProgress)

        openMenu = QMenu(self.tr('Open'), self)
        self.initOpenProjects(openMenu)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu(self.tr('&File'))
        fileMenu.addAction(newAct)
        fileMenu.addMenu(openMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(manageAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        projectMenu = menubar.addMenu(self.tr('&Project'))
        projectMenu.addAction(updateAct)
        projectMenu.addAction(saveAct)
        projectMenu.addAction(sendAct)
        projectMenu.addSeparator()
        projectMenu.addAction(closeAct)

        editMenu = menubar.addMenu(self.tr('&Edit'))
        editMenu.addAction(settingsAct)

        viewMenu = menubar.addMenu(self.tr('&View'))
        viewMenu.addAction(self.showTranslatedAct)
        viewMenu.addAction(self.showUntranslatedAct)
        viewMenu.addAction(self.showFuzzyAct)
        viewMenu.addSeparator()
        viewMenu.addAction(self.monospaceAct)

        self.tabs = ProjectTab()
        self.tabs.currentChanged.connect(self.count)

        self.setCentralWidget(self.tabs)

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Offlate')

class UploadRunnable(QRunnable, RunnableCallback):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.signals = RunnableSignals()
        self.oldamount = -1
        self.error = None
        self.name = self.widget.project.name
    
    def run(self):
        self.widget.send()
        self.signals.finished.emit(self.name)

class UpdateRunnable(QRunnable, RunnableCallback):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.signals = RunnableSignals()
        self.oldamount = -1
        self.error = None
        self.name = self.widget.project.name
    
    def run(self):
        self.widget.update(self)
        self.signals.finished.emit(self.name)

class ExternalRunnable(QRunnable, RunnableCallback):
    def __init__(self, mfile):
        super().__init__()
        self.mfile = mfile
        self.signals = RunnableSignals()
        self.oldamount = -1
        self.error = None
        self.name = ""
    
    def run(self):
        # Try to open file with the default application
        try:
            if platform.system() == 'Darwin':
                subprocess.run(['open', self.mfile])
            elif platform.system() == 'Windows':
                subprocess.run(['start', self.mfile])
            else:
                subprocess.run(['xdg-open', self.mfile])
        except:
            print(sys.exc_info())
            pass
        self.signals.finished.emit("")

class MyHandler(FileSystemEventHandler):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def on_modified(self, event):
        self.parent.signals.progress.emit("", 0)

class WatchRunnable(QRunnable, RunnableCallback):
    def __init__(self, project, size):
        super().__init__()
        self.project = project
        self.signals = RunnableSignals()
        self.oldamount = -1
        self.error = None
        self.name = self.project.name
        self.size = size
        self.observer = Observer()
        event_handler = MyHandler(self)
        mfiles = self.project.getExternalFiles()
        files = []
        for f in mfiles:
            files.extend(f)
        for f in files:
            self.observer.schedule(event_handler, str(Path(f).parent), recursive=True)
    
    def run(self):
        self.observer.start()
        while self.size > 0:
            sleep(0.2)
        self.observer.stop()
        self.observer.join()
        self.signals.finished.emit("")

    def stop(self, name):
        self.size -= 1
