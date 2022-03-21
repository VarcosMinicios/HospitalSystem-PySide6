from main import MainWindow
from mainwindow import Ui_MainWindow


class UiFunctions(Ui_MainWindow):
    def __init__(self):
        pass

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

    