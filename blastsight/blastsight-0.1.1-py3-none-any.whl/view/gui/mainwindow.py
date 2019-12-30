#!/usr/bin/env python

#  Copyright (c) 2019 Gabriel Sanhueza.
#
#  Distributed under the MIT License.
#  See LICENSE for more info.

from qtpy.QtCore import Qt
from qtpy.QtCore import QFileInfo
from qtpy.QtCore import QSettings
from qtpy.QtCore import QThreadPool
from qtpy.QtWidgets import QFileDialog
from qtpy.QtWidgets import QMainWindow
from qtpy.QtWidgets import QHBoxLayout
from qtpy.QtWidgets import QVBoxLayout
from qtpy.QtWidgets import QWidget
from qtpy.QtWidgets import QMenu
from qtpy.QtWidgets import QMenuBar
from qtpy.QtWidgets import QStatusBar
from qtpy.QtWidgets import QDockWidget

from .helpdialog import HelpDialog
from .aboutdialog import AboutDialog
from .threadworker import ThreadWorker

from ..integrableviewer import IntegrableViewer
from .toolbar import ToolBar
from .treewidget import TreeWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(1000, 500)

        # Widget definition
        self.centralWidget = QWidget(self)
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.viewer = IntegrableViewer(self.centralWidget)
        self.horizontalLayout.addWidget(self.viewer)
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(self)
        self.menu_File = QMenu('&File', self.menuBar)
        self.menu_Help = QMenu('&Help', self.menuBar)
        self.menu_View = QMenu('&View', self.menuBar)
        self.menu_Tools = QMenu('&Tools', self.menuBar)
        self.setMenuBar(self.menuBar)
        self.toolbar = ToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.dockWidget = QDockWidget(self)
        self.dockWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.treeWidget = TreeWidget(self.dockWidgetContents, enable_export=True)
        self.verticalLayout.addWidget(self.treeWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.addDockWidget(Qt.DockWidgetArea(1), self.dockWidget)

        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_View.menuAction())
        self.menuBar.addAction(self.menu_Tools.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.setWindowTitle('BlastSight')
        self.toolbar.setWindowTitle('Toolbar')
        self.dockWidget.setWindowTitle('Element tree')
        self.treeWidget.headerItem().setText(0, 'Elements')

        self.setFocusPolicy(Qt.StrongFocus)
        self.setAcceptDrops(True)
        self.statusBar.showMessage('Ready')

        # Attributes
        self.settings = QSettings('BlastSight', application='blastsight', parent=self)
        self.filters_dict = {
            'mesh': 'Mesh Files (*.dxf *.off *.h5m);;'
                    'DXF Files (*.dxf);;'
                    'OFF Files (*.off);;'
                    'H5M Files (*.h5m);;'
                    'All Files (*.*)',
            'blocks': 'Data Files (*.csv *.h5p *.out);;'
                      'CSV Files (*.csv);;'
                      'H5P Files (*.h5p);;'
                      'GSLib Files (*.out);;'
                      'All Files (*.*)',
            'points': 'Data Files (*.csv *.h5p *.out);;'
                      'CSV Files (*.csv);;'
                      'H5P Files (*.h5p);;'
                      'GSLib Files (*.out);;'
                      'All Files (*.*)',
            'lines': 'CSV Files (*.csv);;'
                     'All Files (*.*)',
            'tubes': 'CSV Files (*.csv);;'
                     'All Files (*.*)',
        }

        # Extra actions
        self.toolbar.insertAction(self.toolbar.action_collection.action_plan_view, self.toolbar.action_collection.action_camera_properties)
        self.toolbar.addAction(self.toolbar.action_collection.action_quit)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.generate_menubar()
        self.connect_actions()

        # self.title = self.windowTitle()
        # self.viewer.signal_fps_updated.connect(lambda x: self.setWindowTitle(f'{self.title} (FPS: {x:.1f})'))

    def generate_menubar(self):
        self.menu_File.addAction(self.toolbar.action_collection.action_load_mesh)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_blocks)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_points)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_lines)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_tubes)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.toolbar.action_collection.action_load_mesh_folder)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_blocks_folder)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_points_folder)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_lines_folder)
        self.menu_File.addAction(self.toolbar.action_collection.action_load_tubes_folder)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.toolbar.action_collection.action_quit)

        self.menu_View.addAction(self.toolbar.action_collection.action_camera_properties)
        self.menu_View.addAction(self.toolbar.action_collection.action_plan_view)
        self.menu_View.addAction(self.toolbar.action_collection.action_north_view)
        self.menu_View.addAction(self.toolbar.action_collection.action_east_view)
        self.menu_View.addAction(self.toolbar.action_collection.action_fit_to_screen)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.toolbar.action_collection.action_autofit_to_screen)
        self.menu_View.addAction(self.toolbar.action_collection.action_turbo_rendering)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.toolbar.action_collection.action_perspective_projection)
        self.menu_View.addAction(self.toolbar.action_collection.action_orthographic_projection)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.toolbar.action_collection.action_take_screenshot)

        self.menu_Tools.addAction(self.toolbar.action_collection.action_slice_mode)
        self.menu_Tools.addAction(self.toolbar.action_collection.action_detection_mode)
        self.menu_Tools.addAction(self.toolbar.action_collection.action_measurement_mode)
        self.menu_Tools.addSeparator()
        self.menu_Tools.addAction(self.toolbar.action_collection.action_normal_mode)

        self.menu_Help.addAction(self.toolbar.action_collection.action_help)
        self.menu_Help.addAction(self.toolbar.action_collection.action_about)

    def connect_actions(self):
        # Auto-connections
        self.toolbar.connect_tree(self.treeWidget)  # Handles tree.show()
        self.toolbar.connect_viewer(self.viewer)  # Handles Plan/North/East/Fit/Camera/Turbo/Screenshot
        self.toolbar.connect_main_widget(self)  # Handles Exit
        self.treeWidget.connect_viewer(self.viewer)  # Handles signals from viewer

        # File
        self.toolbar.action_collection.action_load_mesh.triggered.connect(self.dialog_load_mesh)
        self.toolbar.action_collection.action_load_blocks.triggered.connect(self.dialog_load_blocks)
        self.toolbar.action_collection.action_load_points.triggered.connect(self.dialog_load_points)
        self.toolbar.action_collection.action_load_lines.triggered.connect(self.dialog_load_lines)
        self.toolbar.action_collection.action_load_tubes.triggered.connect(self.dialog_load_tubes)

        self.toolbar.action_collection.action_load_mesh_folder.triggered.connect(self.dialog_load_mesh_folder)
        self.toolbar.action_collection.action_load_blocks_folder.triggered.connect(self.dialog_load_blocks_folder)
        self.toolbar.action_collection.action_load_points_folder.triggered.connect(self.dialog_load_points_folder)
        self.toolbar.action_collection.action_load_lines_folder.triggered.connect(self.dialog_load_lines_folder)
        self.toolbar.action_collection.action_load_tubes_folder.triggered.connect(self.dialog_load_tubes_folder)

        # View
        self.toolbar.action_collection.action_show_tree.triggered.connect(self.dockWidget.show)
        self.toolbar.action_collection.action_perspective_projection.triggered.connect(self.viewer.perspective_projection)
        self.toolbar.action_collection.action_orthographic_projection.triggered.connect(self.viewer.orthographic_projection)

        # Tools
        self.toolbar.action_collection.action_detection_mode.triggered.connect(self.slot_detection_mode)
        self.toolbar.action_collection.action_slice_mode.triggered.connect(self.slot_slice_mode)
        self.toolbar.action_collection.action_measurement_mode.triggered.connect(self.slot_measurement_mode)
        self.toolbar.action_collection.action_normal_mode.triggered.connect(self.slot_normal_mode)

        # Help
        self.toolbar.action_collection.action_help.triggered.connect(self.slot_help)
        self.toolbar.action_collection.action_about.triggered.connect(self.slot_about)

        # Viewer signals
        self.viewer.signal_fps_updated.connect(self.print_fps)
        self.viewer.signal_mode_updated.connect(self.slot_mode_updated)
        self.viewer.signal_mesh_clicked.connect(self.slot_mesh_clicked)
        self.viewer.signal_mesh_distances.connect(self.slot_mesh_distances)
        self.viewer.signal_mesh_sliced.connect(self.slot_mesh_sliced)
        self.viewer.signal_blocks_sliced.connect(self.slot_blocks_sliced)

        self.viewer.signal_load_success.connect(self.slot_element_load_success)
        self.viewer.signal_load_failure.connect(self.slot_element_load_failure)
        self.viewer.signal_export_success.connect(self.slot_element_export_success)
        self.viewer.signal_export_failure.connect(self.slot_element_export_failure)

        # TreeWidget actions
        self.treeWidget.signal_export_mesh.connect(self.dialog_export_mesh)
        self.treeWidget.signal_export_blocks.connect(self.dialog_export_blocks)
        self.treeWidget.signal_export_points.connect(self.dialog_export_points)
        self.treeWidget.signal_export_lines.connect(self.dialog_export_lines)
        self.treeWidget.signal_export_tubes.connect(self.dialog_export_tubes)

    @property
    def last_dir(self) -> str:
        return self.settings.value('last_directory', '.')

    @last_dir.setter
    def last_dir(self, _last_dir: str) -> None:
        self.settings.setValue('last_directory', _last_dir)

    @staticmethod
    def print_fps(fps) -> None:
        print(f'               \r', end='')
        print(f'FPS: {fps:.1f} \r', end='')

    """
    Status bar updates
    """
    def slot_element_load_success(self, _id: int):
        self.statusBar.showMessage(f'Load successful (id: {_id}).')

    def slot_element_load_failure(self):
        self.statusBar.showMessage(f'Failed to load.')

    def slot_element_export_success(self, _id: int):
        self.statusBar.showMessage(f'Export successful (id: {_id}).')

    def slot_element_export_failure(self):
        self.statusBar.showMessage(f'Failed to export.')

    def slot_mode_updated(self, mode: str):
        self.statusBar.showMessage(f'Mode: {mode}')

    def slot_mesh_distances(self, distance_dict: dict):
        self.statusBar.showMessage(f'Distance: {distance_dict.get("distance")}')

    def slot_mesh_clicked(self, mesh_attributes: list):
        id_list = [attr.get('id', -1) for attr in mesh_attributes]
        self.statusBar.showMessage(f'Detected meshes: {id_list}')

    def slot_mesh_sliced(self, slice_dict: dict):
        slice_list = slice_dict.get('slices', [])

        for sliced_meshes in slice_list:
            slices = sliced_meshes.get('vertices')
            origin_id = sliced_meshes.get('origin_id')
            mesh = self.viewer.get_drawable(origin_id)

            if 'SLICE' in str(mesh.name):
                continue

            for i, vert_slice in enumerate(slices):
                self.viewer.lines(vertices=vert_slice,
                                  color=mesh.color,
                                  name=f'MESHSLICE_{i}_{mesh.name}',
                                  extension=mesh.extension,
                                  loop=True)

    def slot_blocks_sliced(self, slice_dict: dict):
        slice_list = slice_dict.get('slices', [])

        for sliced_blocks in slice_list:
            indices = sliced_blocks.get('indices')
            origin_id = sliced_blocks.get('origin_id')
            block = self.viewer.get_drawable(origin_id)

            if 'SLICE' in str(block.name):
                continue

            self.viewer.blocks(vertices=block.vertices[indices],
                               values=block.values[indices],
                               color=block.color[indices],
                               vmin=block.vmin,
                               vmax=block.vmax,
                               colormap=block.colormap,
                               name=f'BLOCKSLICE_{block.name}',
                               extension=block.extension,
                               block_size=block.block_size,
                               alpha=1.0,
                               )

    """
    Common functionality for loading/exporting
    """
    def _threaded_load(self, method: classmethod, path: str, *args, **kwargs) -> None:
        self.statusBar.showMessage('Loading...')

        worker = ThreadWorker(method, path, *args, **kwargs)
        QThreadPool.globalInstance().start(worker)

    def _threaded_export(self, method: classmethod, path: str, _id: int) -> None:
        self.statusBar.showMessage('Exporting...')

        worker = ThreadWorker(method, path, _id)
        QThreadPool.globalInstance().start(worker)

    def _dialog_load_element(self, method: classmethod, hint: str, *args, **kwargs) -> None:
        (paths, selected_filter) = QFileDialog.getOpenFileNames(
            parent=self,
            directory=self.last_dir,
            filter=self.filters_dict.get(hint))

        path_list = [p for p in paths if p != '']
        for path in sorted(path_list):
            self._threaded_load(method, path, hint=hint, *args, **kwargs)
            self.last_dir = QFileInfo(path).absoluteDir().absolutePath()

    def _dialog_load_folder(self, method: classmethod, hint: str, *args, **kwargs) -> None:
        path = QFileDialog.getExistingDirectory(
            parent=self,
            directory=self.last_dir,
            options=QFileDialog.ShowDirsOnly)

        # Execute method
        self._threaded_load(method, path, hint=hint, *args, **kwargs)
        self.last_dir = path

    def _dialog_export_element(self, _id: int, filters: str, method: classmethod) -> None:
        (path, selected_filter) = QFileDialog.getSaveFileName(
            parent=self,
            directory=self.viewer.get_drawable(_id).element.name,
            filter=filters)

        if path != '':
            # Execute method
            self._threaded_export(method, path, _id)

    """
    Slots for loading files
    """
    def dialog_load_mesh(self) -> None:
        self._dialog_load_element(method=self.viewer.mesh_by_path, hint='mesh')

    def dialog_load_blocks(self) -> None:
        self._dialog_load_element(method=self.viewer.blocks_by_path, hint='blocks')

    def dialog_load_points(self) -> None:
        self._dialog_load_element(method=self.viewer.points_by_path, hint='points')

    def dialog_load_lines(self) -> None:
        self._dialog_load_element(method=self.viewer.lines_by_path, hint='lines')

    def dialog_load_tubes(self) -> None:
        self._dialog_load_element(method=self.viewer.tubes_by_path, hint='tubes')

    def dialog_load_mesh_folder(self) -> None:
        self._dialog_load_folder(method=self.viewer.meshes_by_folder_path, hint='mesh')

    def dialog_load_blocks_folder(self) -> None:
        self._dialog_load_folder(method=self.viewer.blocks_by_folder_path, hint='blocks')

    def dialog_load_points_folder(self) -> None:
        self._dialog_load_folder(method=self.viewer.points_by_folder_path, hint='points')

    def dialog_load_lines_folder(self) -> None:
        self._dialog_load_folder(method=self.viewer.lines_by_folder_path, hint='lines')

    def dialog_load_tubes_folder(self) -> None:
        self._dialog_load_folder(method=self.viewer.tubes_by_folder_path, hint='tubes')

    """
    Slots for exporting files
    """
    def dialog_export_mesh(self, _id: int) -> None:
        self._dialog_export_element(_id=_id,
                                    filters='BlastSight mesh (*.h5m);;',
                                    method=self.viewer.export_mesh)

    def dialog_export_blocks(self, _id: int) -> None:
        self._dialog_export_element(_id=_id,
                                    filters='BlastSight blocks (*.h5p);;',
                                    method=self.viewer.export_blocks)

    def dialog_export_points(self, _id: int) -> None:
        self._dialog_export_element(_id=_id,
                                    filters='BlastSight points (*.h5p);;',
                                    method=self.viewer.export_points)

    def dialog_export_lines(self, _id: int) -> None:
        self._dialog_export_element(_id=_id,
                                    filters='BlastSight lines (*.csv);;',
                                    method=self.viewer.export_lines)

    def dialog_export_tubes(self, _id: int) -> None:
        self._dialog_export_element(_id=_id,
                                    filters='BlastSight tubes (*.csv);;',
                                    method=self.viewer.export_tubes)

    """
    Slots for modifying controller modes
    """
    def slot_normal_mode(self) -> None:
        self.viewer.set_normal_mode()

    def slot_detection_mode(self) -> None:
        self.viewer.set_detection_mode()

    def slot_slice_mode(self) -> None:
        self.viewer.set_slice_mode()

    def slot_measurement_mode(self) -> None:
        self.viewer.set_measurement_mode()

    """
    Slots for showing help/about dialogs
    """
    def slot_help(self) -> None:
        HelpDialog(self).exec_()

    def slot_about(self) -> None:
        AboutDialog(self).exec_()

    """
    Events pass-through
    """
    def dragEnterEvent(self, event, *args, **kwargs) -> None:
        self.viewer.dragEnterEvent(event, *args, **kwargs)

    def dropEvent(self, event, *args, **kwargs) -> None:
        self.viewer.dropEvent(event, *args, **kwargs)
