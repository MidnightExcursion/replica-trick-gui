# External Packages | PyQt5
from PyQt5.QtWidgets import QMainWindow, QWidget

from gui.tabs.central_tab import CentralTab

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

        

        # # (3): Initialize the central widget's tabs:
        # self.central_tab = CentralTab()

        # # (4): Add the central tab to the actual central widget:
        # self.central_tab.addTab(self.central_tab, "Main Display")