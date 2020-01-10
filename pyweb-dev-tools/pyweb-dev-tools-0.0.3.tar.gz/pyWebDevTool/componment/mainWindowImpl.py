# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtCore import QUrl, Qt, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QWidget, QMenuBar, QMenu, QVBoxLayout, QApplication, QTabBar, QAction

from pyWebDevTool.componment.PluginBuildDelegate import PluginBuildDelegate
from pyWebDevTool.componment.aboutDialog import AboutDialog
from pyWebDevTool.componment.channelBridge import ChannelBridge
from pyWebDevTool.componment.icon import AppIcon
from pyWebDevTool.componment.mainWindow import Ui_Form
from pyWebDevTool.componment.pluginInstallDialog import PluginInstallDialog
from pyWebDevTool.componment.webView import MyQWebEngineView, MyQWebEnginePage
from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.util import pluginStoreUtil, packageInfoUtil, qResourceUtil, webPageUtil, argumentUtil
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


class MainWindowImpl(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.aboutDialog = None
        self.plugin_install_dialog = None
        self.setupUi(self)
        self.tab_info = []

        self.bPressFlag = False
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.setWindowTitle("python工具包")
        self.setWindowIconText("python工具包")
        self.label.setText("pyweb-dev-tools")
        self.icon = AppIcon()
        self.setWindowIcon(self.icon)

        _desktop = QApplication.desktop()
        self._main_screen_geometry = _desktop.screenGeometry(0)
        self.init_height = self.height()
        self.init_width = self.width()
        self.move((self._main_screen_geometry.width() - self.width()) / 2,
                  (self._main_screen_geometry.height() - self.height()) / 2)
        self.init_geo = self.geometry()

        self.__init_menu()

        self.tabWidget.removeTab(1)
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.__init_view()

        self.__init_size()

        self.__init_title_bar_event()

        self.show()

    def __init_title_bar_event(self):
        self.pushButton_min.clicked.connect(lambda: self.hide())
        self.pushButton_restore.clicked.connect(self.__init_size)
        self.pushButton_max.clicked.connect(self.__set_max)
        self.pushButton_close.clicked.connect(self.hide)

    def __init_view(self):
        self.view = self.new_web_view()
        # 加载默认页面的初始化页面
        self.load_default_tab_loading()
        self.append_tab_info("index_tab", 0, "工作台", self.view)

    def load_default_tab(self):
        self.tabWidget.setCurrentIndex(0)
        self.load_url(webPageUtil.get_page_path_index(), self.view)

    def load_default_tab_loading(self):
        self.tabWidget.setCurrentIndex(0)
        self.load_url(webPageUtil.get_page_path_loading(), self.view)

    def show_readme(self):
        Context().trayIcon.showMessage("提示", "说明文档已显示在首页", self.icon, msecs=500)
        self.load_default_tab()

    def __init_menu(self):
        self.menu_bar = QMenuBar(self.menu_widget)
        self.myQMenuBarCss = qResourceUtil.get_qss("myQMenuBar.qss")
        self.menu_bar.setStyleSheet(self.myQMenuBarCss)

        self.init_plugin_menu()

    def init_plugin_menu(self):
        self.myQMenuCss = qResourceUtil.get_qss("myQMenu.qss")
        self.menu1 = QMenu("开始")
        menu_action21 = QAction("安装插件", self, triggered=self.open_plugin_install_dialog)
        self.pluginBuildDelegate = PluginBuildDelegate(self)
        menu_action22 = QAction("构建插件", self, triggered=self.pluginBuildDelegate.build_plugin)
        menu_action23 = QAction("插件管理", self, triggered=self.plugin_manage)
        self.menu1.addAction(menu_action21)
        self.menu1.addAction(menu_action22)
        self.menu1.addAction(menu_action23)
        if argumentUtil.is_dev():
            menu_action24 = QAction("打开调试页面", self, triggered=self.open_debug_page)
            self.menu1.addAction(menu_action24)
        self.menu1.setStyleSheet(self.myQMenuCss)

        self.menu_bar.addMenu(self.menu1)

        self.menu2 = QMenu("我的插件")
        self.menu2.setStyleSheet(self.myQMenuCss)
        class_json = pluginStoreUtil.read_class_json()
        for c in class_json:
            menu = QMenu()
            menu.setStyleSheet(self.myQMenuCss)
            a = QAction(c, self)
            for p in class_json[c]:
                web_page_path = pluginStoreUtil.get_plugin_index_path(p)
                menu_action = QAction(p['name'], self,
                                      triggered=partial(self.add_tab, p['name'], packageInfoUtil.get_package_info_id(p),
                                                        web_page_path))
                menu.addAction(menu_action)
            a.setMenu(menu)
            self.menu2.addAction(a)
        self.menu_bar.addMenu(self.menu2)

        self.menu3 = QMenu("帮助")
        menu_action31 = QAction("关于", self, triggered=self.about)
        menu_action32 = QAction("说明文档", self, triggered=self.show_readme)
        self.menu3.addAction(menu_action31)
        self.menu3.addAction(menu_action32)
        self.menu3.setStyleSheet(self.myQMenuCss)
        self.menu_bar.addMenu(self.menu3)

        self.menu_widget_verticalLayout = QVBoxLayout(self.menu_widget)
        self.menu_widget_verticalLayout.setObjectName("menu_widget_verticalLayout")
        self.menu_widget_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_widget_verticalLayout.setSpacing(0)
        self.menu_widget_verticalLayout.addWidget(self.menu_bar)

    def reload_plugin_menu(self):
        self.menu2.deleteLater()
        self.menu1.deleteLater()
        self.menu3.deleteLater()
        for tab in self.tab_info:
            if tab['tab_index'] > 0:
                self.close_tab(tab['tab_index'])
        self.init_plugin_menu()

    def reload_all(self):
        url = self.view.page().url()
        self.load_url(url.toDisplayString(), self.view)
        self.reload_plugin_menu()

    def __init_size(self):
        self.pushButton_restore.setHidden(True)
        self.pushButton_max.setHidden(False)
        self.setGeometry(self.init_geo)
        for tab in self.tab_info:
            self.__resize_view(tab['view'])

    def get_view_act_height(self):
        return self.init_geo.height() - self.title.height() - self.menu_bar.height() - self.tabWidget.tabBar().height() + 15

    def __set_max(self):
        self.pushButton_restore.setHidden(False)
        self.pushButton_max.setHidden(True)
        for tab in self.tab_info:
            tab['view'].setGeometry(self._main_screen_geometry)
        self.setGeometry(self._main_screen_geometry)

    def mousePressEvent(self, event):
        """在Qt程序中，当隐藏掉窗体的标题栏之后，如果不重写鼠标移动事件，我们是无法通过鼠标任意拖拽窗体的。 """
        self.bPressFlag = True
        self.beginDrag = event.pos()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.bPressFlag = False
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.beginDrag:
            qPoint = QPoint(QCursor.pos() - self.beginDrag)
            self.move(qPoint)
        super().mouseMoveEvent(event)

    def add_tab(self, tab_name, tab_id, url):
        # 增加一个标签
        # 如果该tab已经存在，则打开存在的
        tab_length = len(self.tab_info)
        for _tab in self.tab_info:
            if _tab['tab_id'] == tab_id:
                tab_index = _tab['tab_index']
                self.tabWidget.setCurrentIndex(tab_index)
                return
        view = self.new_web_view()
        self.load_url(url, view)
        self.tabWidget.addTab(view, tab_name)
        tab_index = tab_length
        self.tabWidget.setCurrentIndex(tab_index)
        self.append_tab_info(tab_id, tab_index, tab_name, view)

    def new_web_view(self):
        view = MyQWebEngineView(self.tab)
        page = MyQWebEnginePage(view)
        view.setPage(page)
        return view

    def load_url(self, url, view):
        if url.startswith("http"):
            q_url = QUrl(url)
        elif url.startswith("file:///"):
            q_url = QUrl.fromLocalFile(url)
        else:
            q_url = QUrl("file:///" + url.replace("\\", "/"))
        view.page().load(q_url)

    def append_tab_info(self, tab_id, tab_index, tab_name, view):
        web_channel = self.init_view_web_channel(view)
        self.init_view_right_menu(view)
        self.__resize_view(view)
        self.tab_info.append({
            "tab_id": tab_id,
            "tab_name": tab_name,
            "tab_index": tab_index,
            "web_channel": web_channel,
            "view": view
        })

    def __resize_view(self, view):
        view.setGeometry(0, 0, self.init_geo.width(), self.get_view_act_height())

    def close_tab(self, index):
        self.tabWidget.removeTab(index)
        self.tab_info[index]['view'].close()
        self.tab_info.pop(index)

    def init_view_right_menu(self, view):
        view.setContextMenuPolicy(Qt.NoContextMenu)

    def init_view_web_channel(self, view):
        q_web_channel = QWebChannel(view)
        channel_bridge = ChannelBridge(view)
        q_web_channel.registerObject('pyqtChannel', channel_bridge)
        view.page().setWebChannel(q_web_channel)
        web_channel = {
            "channel": q_web_channel,
            "bridge": channel_bridge
        }
        return web_channel

    def about(self):
        self.aboutDialog = AboutDialog(self)

    def open_plugin_install_dialog(self):
        self.plugin_install_dialog = PluginInstallDialog(self)
        self.plugin_install_dialog.show()

    def plugin_manage(self):
        self.add_tab("插件管理", "pywebtool_pluginManage", webPageUtil.get_page_path("/pluginManage"))

    def open_debug_page(self):
        self.add_tab("调试页面", "pywebtool_debugPage", webPageUtil.get_page_path_debug())
