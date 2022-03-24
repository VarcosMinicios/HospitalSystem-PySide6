from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import QSize


class LineEdit(QLineEdit):

    def __init__(self, parent, name, font):
        super().__init__(parent)
        self.setMaximumSize(QSize(16777215, 30))
        self.setObjectName(name)
        self.setFont(font)
        self.setStyleSheet(
                """
                        QLineEdit {
                                border: 1px solid rgb(144, 144, 144);
                                border-radius: 5px;
                                color: gray;
                                padding: 3px;
                                padding-left: 8px;
                                background-color: rgb(85, 85, 85);
                        }     

                        QLineEdit:hover {
                                border: 1px solid rgb(180, 180, 180);
                        }

                        QLineEdit:focus {
                                border: 1px solid rgb(180, 180, 180);
                        }

                        QLineEdit:disabled {
                                background-color: rgb(144, 144, 144);
                        }
                """
        )

    def updateStyleSheet(self):

        if self.text() == "":

            self.setStyleSheet(
            """
            QLineEdit {
                    border: 1px solid rgb(144, 144, 144);
                    border-radius: 5px;
                    color: gray;
                    padding: 3px;
                    padding-left: 8px;
                    background-color: rgb(85, 85, 85);
            }     

            QLineEdit:hover {
                    border: 1px solid rgb(180, 180, 180);
            }

            QLineEdit:focus {
                    border: 1px solid rgb(180, 180, 180);
            }

            QLineEdit:disabled {
                background-color: rgb(144, 144, 144);
            }
            """)
        
        else:

            self.setStyleSheet(
            """
            QLineEdit {
                    border: 1px solid rgb(144, 144, 144);
                    border-radius: 5px;
                    color: #FFF;
                    padding: 3px;
                    padding-left: 8px;
                    background-color: rgb(85, 85, 85);
            }     

            QLineEdit:hover {
                    border: 1px solid rgb(180, 180, 180);
            }

            QLineEdit:focus {
                    border: 1px solid rgb(180, 180, 180);
            }
            
            QLineEdit:disabled {
                background-color: rgb(144, 144, 144);
            }
            """)

    def toUpper(self):
        cursor_pos = self.cursorPosition()
        self.setText(self.text().upper())
        self.setCursorPosition(cursor_pos)
        
    def maskCpf(self):

        if len(self.text()) == 1:
            prev_text = self.text()
            self.setInputMask("000.000.000-00")
            self.setText(prev_text)
            self.setCursorPosition(1)
        
        if len(self.text()) == 3:
            self.setInputMask("")

    def maskPhone(self):
        if len(self.text()) == 1:
            prev_text = self.text()
            self.setInputMask("(00) 00000-0000")
            self.setText(prev_text)
            self.setCursorPosition(2)
        
        if len(self.text()) == 4:
            self.setInputMask("")

    def maskDate(self):
        if len(self.text()) == 1:
            prev_text = self.text()
            self.setInputMask("00/00/0000")
            self.setText(prev_text)
            self.setCursorPosition(1)
        
        if len(self.text()) == 2:
            self.setInputMask("")

    def maskCRM(self):
        if len(self.text()) == 1:
            prev_text = self.text()
            self.setInputMask("CRM nnnnnnnnnnnnnnnnnnn")
            self.setText(prev_text)
            self.setCursorPosition(5)
        
        if len(self.text()) == 4:
            self.setInputMask("")

    def maskCep(self):
        if len(self.text()) == 1:
            prev_text = self.text()
            self.setInputMask("00.000-000")
            self.setText(prev_text)
            self.setCursorPosition(1)
        
        if len(self.text()) == 2:
            self.setInputMask("")

    def maskSusCard(self):
        if len(self.text()) == 1:
            prev_text = self.text()
            self.setInputMask("0000.0000.0000.0000")
            self.setText(prev_text)
            self.setCursorPosition(1)
        
        if len(self.text()) == 3:
            self.setInputMask("")
            