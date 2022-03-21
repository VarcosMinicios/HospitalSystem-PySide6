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
        """)

    def setMask(self):
        
        print(self.text())

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
