from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize, Qt


class MenuBtn(QPushButton):
    def __init__(self, parent, name, image, font, padding_bottom, target):
        super().__init__(parent)

        self.image = image
        self.padding_bottom = padding_bottom

        self.focus = False

        self.stacked = 'self.ui.stackedWidget'
        self.target = target

        self.setObjectName(name)
        self.setMinimumSize(QSize(100, 100))
        self.setMaximumSize(QSize(100, 100))
        self.setFont(font)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
        QPushButton {
            padding-top: 10px;
        """

            f"background-image: url(:/logo/images/{self.image});"
            f"padding-bottom: {self.padding_bottom}; "

        """ 
            background-repeat: no-repeat;
            background-position: center top;
            text-align: bottom;
            color:#ffffff;
            border: 2px solid #009800;
        }
        QPushButton::hover {
            background-color: rgb(68, 69, 71);
        } 
        """)

    def navigate(self):

        self.stacked.setCurrentIndex(self.target)
        
        self.setStyleSheet("""
        QPushButton {
            padding-top: 10px;
        """

            f"background-image: url(:/logo/images/{self.image});"
            f"padding-bottom: {self.padding_bottom}; "

        """ 
            background-repeat: no-repeat;
            background-position: center top;
            text-align: bottom;
            color:#ffffff;
            border: 2px solid #009800;
            background-color: #4d4e50;
        }
        QPushButton::hover {
            background-color: rgb(68, 69, 71);
        } 
        """)

    def unselect(self):

        self.setStyleSheet("""
        QPushButton {
            padding-top: 10px;
        """

            f"background-image: url(:/logo/images/{self.image});"
            f"padding-bottom: {self.padding_bottom}; "

        """ 
            background-repeat: no-repeat;
            background-position: center top;
            text-align: bottom;
            color:#ffffff;
            border: 2px solid #009800;
        }
        QPushButton::hover {
            background-color: rgb(68, 69, 71);
        } 
        """)