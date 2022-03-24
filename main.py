from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
import sys

from ui_functions import *
from mainwindow import Ui_MainWindow
from Objects.DataBase import DataBase


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # Setup the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create Variables
        self.previousBtn = self.ui.menuBtnMap
        self.db = DataBase()

        # Init functions
        self.set_widget_connections()

        self.ui.stackedWidget.setCurrentIndex(1)

        # Show window
        self.show()

    # The btn Passed is the "new" self.previousBtn
    def unselect_button(self, btn):
        self.previousBtn.unselect()
        self.previousBtn = btn

    def set_widget_connections(self):

        # Connect the Buttons to discharge
        for button in self.ui.pageMap.findChildren(QPushButton):
            if button.objectName()[0] == "a":
                suffix = button.objectName().replace('a', '')
                button.clicked.connect(self.init_discharge)

        # Connect the Lines to the UpperFunction and the styleSheet function to all LineEdits
        for lineEdit in self.ui.stackedWidget.findChildren(QLineEdit):
            lineEdit.textChanged.connect(lineEdit.updateStyleSheet)
            lineEdit.textChanged.connect(lineEdit.toUpper)

        # Connect the Menu Btns to respective functions
        for menuBtn in self.ui.frame.findChildren(QPushButton):
            menuBtn.stacked = self.ui.stackedWidget
            menuBtn.clicked.connect(menuBtn.navigate)

        self.ui.menuBtnMap.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnMap))

        self.ui.menuBtnAtendimento.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnAtendimento))

        self.ui.menuBtnExport.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnExport))
        
        self.ui.menuBtnHistoric.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnHistoric))

        self.ui.menuBtnPatient.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnPatient))

        self.ui.menuBtnRecibo.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnRecibo))

        self.ui.menuBtnRegister.clicked.connect(lambda: self.unselect_button(self.ui.menuBtnRegister))
        # # # # #

        self.ui.fifthLineCpf.textEdited.connect(self.ui.fifthLineCpf.maskCpf)

        self.ui.firstLineCpf.textEdited.connect(self.ui.firstLineCpf.maskCpf)

        self.ui.sixthLineCpf.textEdited.connect(self.ui.sixthLineCpf.maskCpf)

        self.ui.thirdLineCpf.textEdited.connect(self.ui.thirdLineCpf.maskCpf)

        self.ui.secondLineCpf.textEdited.connect(self.ui.secondLineCpf.maskCpf)

        self.ui.seventhLineCpf.textEdited.connect(self.ui.seventhLineCpf.maskCpf)

        self.ui.sixthLineBornDate.textEdited.connect(self.ui.sixthLineBornDate.maskDate)

        self.ui.thirdLineInitDate.textEdited.connect(self.ui.thirdLineInitDate.maskDate)

        self.ui.thirdLineFinalDate.textEdited.connect(self.ui.thirdLineFinalDate.maskDate)

        self.ui.firstLinePhoneOne.textEdited.connect(self.ui.firstLinePhoneOne.maskPhone)
        
        self.ui.firstLinePhoneTwo.textEdited.connect(self.ui.firstLinePhoneTwo.maskPhone)

        self.ui.fourthLineCrm.textEdited.connect(self.ui.fourthLineCrm.maskCRM)

        self.ui.firstLineSusCard.textEdited.connect(self.ui.firstLineSusCard.maskSusCard)

        self.ui.firstLineCep.textEdited.connect(self.ui.firstLineCep.maskCep)

        # Connect Other functions

        self.ui.firstBtnConfirm.clicked.connect(lambda: UiFunctions.registerAndHospitalize(self))

        self.ui.firstBtnRegister.clicked.connect(lambda: UiFunctions.register(self))

    def init_discharge(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
