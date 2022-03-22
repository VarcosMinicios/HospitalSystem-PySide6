from main import MainWindow
from Objects.DataBase import PatientRegister, HospitalizationInfo
from mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QLineEdit


class UiFunctions(Ui_MainWindow):
    def __init__(self, parent):
        self.parent = parent

    @staticmethod
    def upperFunc(line):
        position = line.cursorPosition()
        line.setText(line.text().upper())
        line.setCursorPosition(position)

    @staticmethod
    def maskCpf(line):
        if len(line.text()) == 1:
            prev_text = line.text()
            line.setInputMask("000.000.000-00")
            line.setText(prev_text)
            line.setCursorPosition(1)
        
        if len(line.text()) == 3:
            line.setInputMask("")

    @staticmethod
    def maskPhone(line):
        if len(line.text()) == 1:
            prev_text = line.text()
            line.setInputMask("(00) 00000-0000")
            line.setText(prev_text)
            line.setCursorPosition(2)
        
        if len(line.text()) == 4:
            line.setInputMask("")

    @staticmethod
    def maskDate(line):
        if len(line.text()) == 1:
            prev_text = line.text()
            line.setInputMask("00/00/0000")
            line.setText(prev_text)
            line.setCursorPosition(1)
        
        if len(line.text()) == 2:
            line.setInputMask("")

    @staticmethod
    def maskCRM(line):
        if len(line.text()) == 1:
            prev_text = line.text()
            line.setInputMask("CRM nnnnnnnnnnnnnnnnnnn")
            line.setText(prev_text)
            line.setCursorPosition(5)
        
        if len(line.text()) == 4:
            line.setInputMask("")

    @staticmethod
    def maskCep(line):
        if len(line.text()) == 1:
            prev_text = line.text()
            line.setInputMask("00.000-000")
            line.setText(prev_text)
            line.setCursorPosition(1)
        
        if len(line.text()) == 2:
            line.setInputMask("")

    @staticmethod
    def maskSusCard(line):
        if len(line.text()) == 1:
            prev_text = line.text()
            line.setInputMask("0000.0000.0000.0000")
            line.setText(prev_text)
            line.setCursorPosition(1)
        
        if len(line.text()) == 3:
            line.setInputMask("")

    def hospitalization(self):
        pass
        # self.parent.db.insertHospitalizations('hospitalizations', HospitalizationInfo(patient_id, card_code, cpf, patient, hospitalize_date, 
        #                                                                               admission, doctor, crm, clinic, bed, dependency,
        #                                                                               hospitalize_hour, responsible))
