# External Packages | PyQTt5
from PyQt5.QtWidgets import QTabWidget, QGridLayout, QFrame, QVBoxLayout

class LoggingTab(QTabWidget):

    def __init__(self):

        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        
        layout = QGridLayout()

        # Section 1
        section1 = QFrame()
        section1_layout = QVBoxLayout()
        section1.setLayout(section1_layout)

        # Adding sections to the grid layout
        layout.addWidget(section1, 0, 0)  # Row 0, Column 0

        self.setLayout(layout)
