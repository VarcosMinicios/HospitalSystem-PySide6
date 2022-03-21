from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PySide6.QtGui import QPalette, QColor
import sys

from ui_functions import *
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # Setup the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init functions
        self.set_connections()

        self.ui.stackedWidget.setCurrentIndex(1)

        # Show window
        self.show()

    def set_connections(self):
        for button in self.ui.pageMap.findChildren(QPushButton):
            if button.objectName()[0] == "a":
                suffix = button.objectName().replace('a', '')
                button.clicked.connect(self.init_discharge)

        palette = self.ui.firstLinePatientName.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 110))

        self.ui.firstLinePatientName.setPalette(palette)

        for line in self.ui.stackedWidget.findChildren(QLineEdit):
            line.setPalette(palette)

        palette2 = self.ui.menuBtnAtendimento.palette()
        

    def init_discharge(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
