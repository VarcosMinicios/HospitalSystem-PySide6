from signal import signal
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

    # The btn Passed is the "new" self.previousBtn
    def unselectButton(self, btn):
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
            lineEdit.textEdited.connect(lineEdit.setMask)

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
        # # # # #


        # Connect the Lines to the UpperFunction
        self.ui.firstLinePatientName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLinePatientName))

        self.ui.firstLineAdress.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineAdress))

        self.ui.firstLineCity.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineCity))

        self.ui.firstLineDistrict.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineDistrict))

        self.ui.firstLineFatherName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineFatherName))

        self.ui.firstLineMotherName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineMotherName))

        self.ui.firstLineProfession.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineProfession))

        self.ui.firstLineRG.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineRG))

        self.ui.firstLineResponsible.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineResponsible))

        self.ui.secondLineMotherName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.secondLineMotherName))

        self.ui.secondLinePatientName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.secondLinePatientName))

        self.ui.firstLineUf.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.firstLineUf))

        self.ui.fourthLineName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.fourthLineName))

        self.ui.fourthLineAdress.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.fourthLineAdress))

        self.ui.thirdLineMotherName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.thirdLineMotherName))

        self.ui.thirdLinePatient.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.thirdLinePatient))

        self.ui.fifthLinePayer.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.fifthLinePayer))

        self.ui.sixthLineMotherName.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.sixthLineMotherName))

        self.ui.fifthLinePatient.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.fifthLinePatient))

        self.ui.sixthLinePatient.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.sixthLinePatient))

        self.ui.fourthLineCrm.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.fourthLineCrm))
        # # # # #


        self.ui.fifthLineObs.textEdited.connect(lambda: UiFunctions.upperFunc(self.ui.fifthLineObs))

        self.ui.fifthLineCpf.textEdited.connect(lambda: UiFunctions.maskCpf(self.ui.fifthLineCpf))

        self.ui.firstLineCpf.textEdited.connect(lambda: UiFunctions.maskCpf(self.ui.firstLineCpf))

        self.ui.sixthLineCpf.textEdited.connect(lambda: UiFunctions.maskCpf(self.ui.sixthLineCpf))

        self.ui.thirdLineCpf.textEdited.connect(lambda: UiFunctions.maskCpf(self.ui.thirdLineCpf))

        self.ui.secondLineCpf.textEdited.connect(lambda: UiFunctions.maskCpf(self.ui.secondLineCpf))

        self.ui.seventhLineCpf.textEdited.connect(lambda: UiFunctions.maskCpf(self.ui.seventhLineCpf))

        self.ui.sixthLineBornDate.textEdited.connect(lambda: UiFunctions.maskDate(self.ui.sixthLineBornDate))

        self.ui.thirdLineInitDate.textEdited.connect(lambda: UiFunctions.maskDate(self.ui.thirdLineInitDate))

        self.ui.thirdLineFinalDate.textEdited.connect(lambda: UiFunctions.maskDate(self.ui.thirdLineFinalDate))

        self.ui.firstLinePhoneOne.textEdited.connect(lambda: UiFunctions.maskPhone(self.ui.firstLinePhoneOne))
        
        self.ui.firstLinePhoneTwo.textEdited.connect(lambda: UiFunctions.maskPhone(self.ui.firstLinePhoneTwo))

        self.ui.fourthLineCrm.textEdited.connect(lambda: UiFunctions.maskCRM(self.ui.fourthLineCrm))

        self.ui.firstLineSusCard.textEdited.connect(lambda: UiFunctions.maskSusCard(self.ui.firstLineSusCard))

        self.ui.firstLineCep.textEdited.connect(lambda: UiFunctions.maskCep(self.ui.firstLineCep))

    def init_discharge(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
