# External Packages | PyQt5
from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget ,QVBoxLayout

from gui.interfaces.central_interface import CentralInterface
from gui.tabs.main_tab import MainTab
from gui.tabs.logging_tab import LoggingTab

from gui.static.constants import _APPLICATION_NAME, _WINDOW_MAIN_APP_WIDTH, _WINDOW_MAIN_APP_HEIGHT

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # (1): Set the name of the application:
        self.title = _APPLICATION_NAME
        self.setWindowTitle(self.title)

        # (2): Configure the geometry of the application window:
        self.window_left = 100
        self.window_top = 100
        self.window_width = _WINDOW_MAIN_APP_WIDTH
        self.window_height = _WINDOW_MAIN_APP_HEIGHT
        self.setGeometry(self.window_left, self.window_top, self.window_width, self.window_height)

        # (3): Initalize additional UI:
        self.initializeUI()

    def initializeUI(self):

        # (1): Initialize PyQT's "central widget"
        self.central_widget = QWidget()
        
        # (2): Set the central widget to be the central widget...
        self.setCentralWidget(self.central_widget)

        # (3): Initialize the central tab:
        self.central_tab = QTabWidget()

        # (4): Initialize the first main tab
        self.main_tab = MainTab()
        self.logging_tab = LoggingTab()

        # (4): Add the central tab to the actual central widget:
        self.central_tab.addTab(self.main_tab, "Main Display")
        self.central_tab.addTab(self.logging_tab, "Logging")

        # (): Initalize the MainWindow's layout:
        layout = QVBoxLayout()

        # (): Add the central tab (widget) to the layout so it will actually show up:
        layout.addWidget(self.central_tab)

        # (): Finally, update the central widget's layout with setLayout():
        self.central_widget.setLayout(layout)