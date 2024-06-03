# External Packages | NumPy
import numpy as np

# External Packages | PyQTt5
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QVBoxLayout, QLabel, QPushButton

# External Packages | pyqtgraph
import pyqtgraph as pg

class CentralInterface(QWidget):

    def __init__(self):

        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        
        layout = QVBoxLayout()

# class CentralInterface(QWidget):

#     def __init__(self):

#         super().__init__()

#         self.initializeUI()

#     def initializeUI(self):
        
#         layout = QGridLayout()

#         # Section 1
#         section1 = QFrame()
#         section1_layout = QVBoxLayout()
#         section1_layout.addWidget(QLabel("Section 1"))
#         section1_layout.addWidget(QPushButton("Button 1"))
#         section1.setLayout(section1_layout)

#         # Section 2
#         section2 = QFrame()
#         section2_layout = QVBoxLayout()
#         section2_layout.addWidget(QLabel("Section 2"))
#         section2_layout.addWidget(QPushButton("Button 2"))
#         section2.setLayout(section2_layout)

#         # Section 3
#         section3 = QFrame()
#         section3_layout = QVBoxLayout()
#         section3_layout.addWidget(QLabel("Section 3"))
#         section3_layout.addWidget(QPushButton("Button 3"))
#         section3.setLayout(section3_layout)

#         # Section 4
#         section4 = QFrame()
#         section4_layout = QVBoxLayout()
#         section4_layout.addWidget(QLabel("Section 4"))
#         section4_layout.addWidget(QPushButton("Button 4"))
#         section4.setLayout(section4_layout)

#         # Section 5
#         section5 = QFrame()
#         section5_layout = QVBoxLayout()
#         section5_layout.addWidget(QLabel("Section 5"))
#         section5_layout.addWidget(QPushButton("Button 5"))
#         section5.setLayout(section5_layout)

#         # Section 6
#         section6 = QFrame()
#         section6_layout = QVBoxLayout()
#         section6_layout.addWidget(QLabel("Section 6"))
#         section6_layout.addWidget(QPushButton("Button 6"))
#         section6.setLayout(section6_layout)

#         # Adding sections to the grid layout
#         layout.addWidget(section1, 0, 0)  # Row 0, Column 0
#         layout.addWidget(section2, 0, 1)  # Row 0, Column 1
#         layout.addWidget(section3, 0, 2)  # Row 0, Column 2
#         layout.addWidget(section4, 1, 0)  # Row 1, Column 0
#         layout.addWidget(section5, 1, 1)  # Row 1, Column 1
#         layout.addWidget(section6, 1, 2)  # Row 1, Column 2

#         self.setLayout(layout)
