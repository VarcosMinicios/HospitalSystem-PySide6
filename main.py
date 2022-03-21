from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
import sys

from ui_functions import *
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # Setup the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.previousBtn = self.ui.menuBtnMap

        # Init functions
        self.set_connections()

        self.ui.stackedWidget.setCurrentIndex(1)

        # Show window
        self.show()

    def unselectButton(self, btn):
        print(self.previousBtn.objectName(), "prev")
        print(btn.objectName(), "actual")
        self.previousBtn.unselect()
        self.previousBtn = btn

    def set_connections(self):

        # Connect the Buttons to discharge
        for button in self.ui.pageMap.findChildren(QPushButton):
            if button.objectName()[0] == "a":
                suffix = button.objectName().replace('a', '')
                button.clicked.connect(self.init_discharge)

        # Connect the style function to all LineEdits
        for lineEdit in self.ui.stackedWidget.findChildren(QLineEdit):
            lineEdit.textChanged.connect(lineEdit.updateStyleSheet)

        # Connect the Menu Btns to respective functions
        for menuBtn in self.ui.frame.findChildren(QPushButton):
            menuBtn.stacked = self.ui.stackedWidget
            menuBtn.clicked.connect(menuBtn.navigate)

        self.ui.menuBtnMap.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnMap))

        self.ui.menuBtnAtendimento.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnAtendimento))

        self.ui.menuBtnExport.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnExport))

        self.ui.menuBtnHistoric.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnHistoric))

        self.ui.menuBtnPatient.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnPatient))

        self.ui.menuBtnRecibo.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnRecibo))

        self.ui.menuBtnRegister.clicked.connect(lambda: self.unselectButton(self.ui.menuBtnRegister))
        
    def init_discharge(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
