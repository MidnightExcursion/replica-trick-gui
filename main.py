# Native Package | sys
import sys

# External Packages | PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.windows.main_window import MainWindow

def main():

    # (1): Initialize the Application:
    app = QApplication([])

    # (2): Initialize the Main Window:
    main_window = MainWindow()

    # (3); Show the Main Window:
    main_window.show()

    # (4): Close the application:
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()