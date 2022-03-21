from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

import files


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 653)
        MainWindow.setMinimumSize(QSize(720, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.menuBtnMap = QPushButton(self.frame)
        self.menuBtnMap.setObjectName(u"menuBtnMap")
        self.menuBtnMap.setMinimumSize(QSize(100, 100))
        self.menuBtnMap.setMaximumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(11)
        self.menuBtnMap.setFont(font)
        self.menuBtnMap.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnMap.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 2px;\n"
"	background-image: url(:/logo/images/fi-rr-map.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnMap)

        self.menuBtnAtendimento = QPushButton(self.frame)
        self.menuBtnAtendimento.setObjectName(u"menuBtnAtendimento")
        self.menuBtnAtendimento.setMinimumSize(QSize(100, 100))
        self.menuBtnAtendimento.setMaximumSize(QSize(100, 100))
        self.menuBtnAtendimento.setFont(font)
        self.menuBtnAtendimento.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnAtendimento.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 10px;\n"
"	background-image: url(:/logo/images/fi-rr-file-add.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnAtendimento)

        self.menuBtnHistoric = QPushButton(self.frame)
        self.menuBtnHistoric.setObjectName(u"menuBtnHistoric")
        self.menuBtnHistoric.setMinimumSize(QSize(100, 100))
        self.menuBtnHistoric.setMaximumSize(QSize(100, 100))
        self.menuBtnHistoric.setFont(font)
        self.menuBtnHistoric.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnHistoric.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 2px;\n"
"	background-image: url(:/logo/images/fi-rr-database.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnHistoric)

        self.menuBtnPatient = QPushButton(self.frame)
        self.menuBtnPatient.setObjectName(u"menuBtnPatient")
        self.menuBtnPatient.setMinimumSize(QSize(100, 100))
        self.menuBtnPatient.setMaximumSize(QSize(100, 100))
        self.menuBtnPatient.setFont(font)
        self.menuBtnPatient.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnPatient.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 2px;\n"
"	background-image: url(:/logo/images/fi-rr-user.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnPatient)

        self.menuBtnExport = QPushButton(self.frame)
        self.menuBtnExport.setObjectName(u"menuBtnExport")
        self.menuBtnExport.setMinimumSize(QSize(100, 100))
        self.menuBtnExport.setMaximumSize(QSize(100, 100))
        self.menuBtnExport.setFont(font)
        self.menuBtnExport.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnExport.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 10px;\n"
"	background-image: url(:/logo/images/fi-rr-data-transfer.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnExport)

        self.menuBtnRegister = QPushButton(self.frame)
        self.menuBtnRegister.setObjectName(u"menuBtnRegister")
        self.menuBtnRegister.setMinimumSize(QSize(100, 100))
        self.menuBtnRegister.setMaximumSize(QSize(100, 100))
        self.menuBtnRegister.setFont(font)
        self.menuBtnRegister.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnRegister.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 2px;\n"
"	background-image: url(:/logo/images/fi-rr-user-add.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnRegister)

        self.menuBtnRecibo = QPushButton(self.frame)
        self.menuBtnRecibo.setObjectName(u"menuBtnRecibo")
        self.menuBtnRecibo.setMinimumSize(QSize(100, 100))
        self.menuBtnRecibo.setMaximumSize(QSize(100, 100))
        self.menuBtnRecibo.setFont(font)
        self.menuBtnRecibo.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtnRecibo.setStyleSheet(u"QPushButton {\n"
"	padding-top: 10px;	\n"
"	padding-bottom: 10px;\n"
"	background-image: url(:/logo/images/fi-rr-document.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center top;\n"
"	text-align: bottom;\n"
"	color:#ffffff;\n"
"	border: 2px solid #009800;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(68, 69, 71);\n"
"}")

        self.horizontalLayout.addWidget(self.menuBtnRecibo)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pageMap = QWidget()
        self.pageMap.setObjectName(u"pageMap")
        self.pageMap.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        self.verticalLayout_2 = QVBoxLayout(self.pageMap)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pageMap)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 516, 982))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.grid_11 = QGridLayout()
        self.grid_11.setSpacing(5)
        self.grid_11.setObjectName(u"grid_11")
        self.p_26 = QPushButton(self.scrollAreaWidgetContents)
        self.p_26.setObjectName(u"p_26")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.p_26.sizePolicy().hasHeightForWidth())
        self.p_26.setSizePolicy(sizePolicy1)
        self.p_26.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(14)
        self.p_26.setFont(font1)
        self.p_26.setCursor(QCursor(Qt.ArrowCursor))
        self.p_26.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_11.addWidget(self.p_26, 1, 0, 1, 1)

        self.p_27 = QPushButton(self.scrollAreaWidgetContents)
        self.p_27.setObjectName(u"p_27")
        sizePolicy1.setHeightForWidth(self.p_27.sizePolicy().hasHeightForWidth())
        self.p_27.setSizePolicy(sizePolicy1)
        self.p_27.setMaximumSize(QSize(16777215, 30))
        self.p_27.setFont(font1)
        self.p_27.setCursor(QCursor(Qt.ArrowCursor))
        self.p_27.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_11.addWidget(self.p_27, 2, 0, 1, 1)

        self.p_28 = QPushButton(self.scrollAreaWidgetContents)
        self.p_28.setObjectName(u"p_28")
        sizePolicy1.setHeightForWidth(self.p_28.sizePolicy().hasHeightForWidth())
        self.p_28.setSizePolicy(sizePolicy1)
        self.p_28.setMaximumSize(QSize(16777215, 30))
        self.p_28.setFont(font1)
        self.p_28.setCursor(QCursor(Qt.ArrowCursor))
        self.p_28.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_11.addWidget(self.p_28, 3, 0, 1, 1)

        self.b_30 = QPushButton(self.scrollAreaWidgetContents)
        self.b_30.setObjectName(u"b_30")
        sizePolicy1.setHeightForWidth(self.b_30.sizePolicy().hasHeightForWidth())
        self.b_30.setSizePolicy(sizePolicy1)
        self.b_30.setMaximumSize(QSize(30, 30))
        self.b_30.setStyleSheet(u"background-color: none;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/logo/images/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_30.setIcon(icon)

        self.grid_11.addWidget(self.b_30, 5, 3, 1, 1)

        self.a_28 = QPushButton(self.scrollAreaWidgetContents)
        self.a_28.setObjectName(u"a_28")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.a_28.sizePolicy().hasHeightForWidth())
        self.a_28.setSizePolicy(sizePolicy2)
        self.a_28.setMaximumSize(QSize(40, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.a_28.setFont(font2)
        self.a_28.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_11.addWidget(self.a_28, 3, 1, 1, 1)

        self.p_30 = QPushButton(self.scrollAreaWidgetContents)
        self.p_30.setObjectName(u"p_30")
        sizePolicy1.setHeightForWidth(self.p_30.sizePolicy().hasHeightForWidth())
        self.p_30.setSizePolicy(sizePolicy1)
        self.p_30.setMaximumSize(QSize(16777215, 30))
        self.p_30.setFont(font1)
        self.p_30.setCursor(QCursor(Qt.ArrowCursor))
        self.p_30.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_11.addWidget(self.p_30, 5, 0, 1, 1)

        self.b_26 = QPushButton(self.scrollAreaWidgetContents)
        self.b_26.setObjectName(u"b_26")
        sizePolicy1.setHeightForWidth(self.b_26.sizePolicy().hasHeightForWidth())
        self.b_26.setSizePolicy(sizePolicy1)
        self.b_26.setMaximumSize(QSize(30, 30))
        self.b_26.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_26.setIcon(icon)

        self.grid_11.addWidget(self.b_26, 1, 3, 1, 1)

        self.b_29 = QPushButton(self.scrollAreaWidgetContents)
        self.b_29.setObjectName(u"b_29")
        sizePolicy1.setHeightForWidth(self.b_29.sizePolicy().hasHeightForWidth())
        self.b_29.setSizePolicy(sizePolicy1)
        self.b_29.setMaximumSize(QSize(30, 30))
        self.b_29.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_29.setIcon(icon)

        self.grid_11.addWidget(self.b_29, 4, 3, 1, 1)

        self.a_26 = QPushButton(self.scrollAreaWidgetContents)
        self.a_26.setObjectName(u"a_26")
        sizePolicy2.setHeightForWidth(self.a_26.sizePolicy().hasHeightForWidth())
        self.a_26.setSizePolicy(sizePolicy2)
        self.a_26.setMaximumSize(QSize(40, 30))
        self.a_26.setFont(font2)
        self.a_26.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_11.addWidget(self.a_26, 1, 1, 1, 1)

        self.b_28 = QPushButton(self.scrollAreaWidgetContents)
        self.b_28.setObjectName(u"b_28")
        sizePolicy1.setHeightForWidth(self.b_28.sizePolicy().hasHeightForWidth())
        self.b_28.setSizePolicy(sizePolicy1)
        self.b_28.setMaximumSize(QSize(30, 30))
        self.b_28.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_28.setIcon(icon)

        self.grid_11.addWidget(self.b_28, 3, 3, 1, 1)

        self.a_27 = QPushButton(self.scrollAreaWidgetContents)
        self.a_27.setObjectName(u"a_27")
        sizePolicy2.setHeightForWidth(self.a_27.sizePolicy().hasHeightForWidth())
        self.a_27.setSizePolicy(sizePolicy2)
        self.a_27.setMaximumSize(QSize(40, 30))
        self.a_27.setFont(font2)
        self.a_27.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_11.addWidget(self.a_27, 2, 1, 1, 1)

        self.b_27 = QPushButton(self.scrollAreaWidgetContents)
        self.b_27.setObjectName(u"b_27")
        sizePolicy1.setHeightForWidth(self.b_27.sizePolicy().hasHeightForWidth())
        self.b_27.setSizePolicy(sizePolicy1)
        self.b_27.setMaximumSize(QSize(30, 30))
        self.b_27.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_27.setIcon(icon)

        self.grid_11.addWidget(self.b_27, 2, 3, 1, 1)

        self.a_29 = QPushButton(self.scrollAreaWidgetContents)
        self.a_29.setObjectName(u"a_29")
        sizePolicy2.setHeightForWidth(self.a_29.sizePolicy().hasHeightForWidth())
        self.a_29.setSizePolicy(sizePolicy2)
        self.a_29.setMaximumSize(QSize(40, 30))
        self.a_29.setFont(font2)
        self.a_29.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_11.addWidget(self.a_29, 4, 1, 1, 1)

        self.a_30 = QPushButton(self.scrollAreaWidgetContents)
        self.a_30.setObjectName(u"a_30")
        sizePolicy2.setHeightForWidth(self.a_30.sizePolicy().hasHeightForWidth())
        self.a_30.setSizePolicy(sizePolicy2)
        self.a_30.setMaximumSize(QSize(40, 30))
        self.a_30.setFont(font2)
        self.a_30.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_11.addWidget(self.a_30, 5, 1, 1, 1)

        self.p_29 = QPushButton(self.scrollAreaWidgetContents)
        self.p_29.setObjectName(u"p_29")
        sizePolicy1.setHeightForWidth(self.p_29.sizePolicy().hasHeightForWidth())
        self.p_29.setSizePolicy(sizePolicy1)
        self.p_29.setMaximumSize(QSize(16777215, 30))
        self.p_29.setFont(font1)
        self.p_29.setCursor(QCursor(Qt.ArrowCursor))
        self.p_29.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_11.addWidget(self.p_29, 4, 0, 1, 1)

        self.c_26 = QLabel(self.scrollAreaWidgetContents)
        self.c_26.setObjectName(u"c_26")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.c_26.sizePolicy().hasHeightForWidth())
        self.c_26.setSizePolicy(sizePolicy3)
        self.c_26.setMaximumSize(QSize(16777215, 30))
        self.c_26.setFont(font2)
        self.c_26.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_26.setAlignment(Qt.AlignCenter)
        self.c_26.setMargin(2)

        self.grid_11.addWidget(self.c_26, 1, 2, 1, 1)

        self.c_27 = QLabel(self.scrollAreaWidgetContents)
        self.c_27.setObjectName(u"c_27")
        sizePolicy3.setHeightForWidth(self.c_27.sizePolicy().hasHeightForWidth())
        self.c_27.setSizePolicy(sizePolicy3)
        self.c_27.setMaximumSize(QSize(16777215, 30))
        self.c_27.setFont(font2)
        self.c_27.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_27.setAlignment(Qt.AlignCenter)
        self.c_27.setMargin(2)

        self.grid_11.addWidget(self.c_27, 2, 2, 1, 1)

        self.c_28 = QLabel(self.scrollAreaWidgetContents)
        self.c_28.setObjectName(u"c_28")
        sizePolicy3.setHeightForWidth(self.c_28.sizePolicy().hasHeightForWidth())
        self.c_28.setSizePolicy(sizePolicy3)
        self.c_28.setMaximumSize(QSize(16777215, 30))
        self.c_28.setFont(font2)
        self.c_28.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_28.setAlignment(Qt.AlignCenter)
        self.c_28.setMargin(2)

        self.grid_11.addWidget(self.c_28, 3, 2, 1, 1)

        self.c_29 = QLabel(self.scrollAreaWidgetContents)
        self.c_29.setObjectName(u"c_29")
        sizePolicy3.setHeightForWidth(self.c_29.sizePolicy().hasHeightForWidth())
        self.c_29.setSizePolicy(sizePolicy3)
        self.c_29.setMaximumSize(QSize(16777215, 30))
        self.c_29.setFont(font2)
        self.c_29.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_29.setAlignment(Qt.AlignCenter)
        self.c_29.setMargin(2)

        self.grid_11.addWidget(self.c_29, 4, 2, 1, 1)

        self.c_30 = QLabel(self.scrollAreaWidgetContents)
        self.c_30.setObjectName(u"c_30")
        sizePolicy3.setHeightForWidth(self.c_30.sizePolicy().hasHeightForWidth())
        self.c_30.setSizePolicy(sizePolicy3)
        self.c_30.setMaximumSize(QSize(16777215, 30))
        self.c_30.setFont(font2)
        self.c_30.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_30.setAlignment(Qt.AlignCenter)
        self.c_30.setMargin(2)

        self.grid_11.addWidget(self.c_30, 5, 2, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(16)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.grid_11.addWidget(self.label_11, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_11, 0, 2, 1, 1)

        self.grid_2 = QGridLayout()
        self.grid_2.setSpacing(5)
        self.grid_2.setObjectName(u"grid_2")
        self.p_2 = QPushButton(self.scrollAreaWidgetContents)
        self.p_2.setObjectName(u"p_2")
        sizePolicy1.setHeightForWidth(self.p_2.sizePolicy().hasHeightForWidth())
        self.p_2.setSizePolicy(sizePolicy1)
        self.p_2.setMaximumSize(QSize(16777215, 30))
        self.p_2.setFont(font1)
        self.p_2.setCursor(QCursor(Qt.ArrowCursor))
        self.p_2.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_2.addWidget(self.p_2, 1, 0, 1, 1)

        self.b_2 = QPushButton(self.scrollAreaWidgetContents)
        self.b_2.setObjectName(u"b_2")
        sizePolicy1.setHeightForWidth(self.b_2.sizePolicy().hasHeightForWidth())
        self.b_2.setSizePolicy(sizePolicy1)
        self.b_2.setMaximumSize(QSize(30, 30))
        self.b_2.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_2.setIcon(icon)

        self.grid_2.addWidget(self.b_2, 1, 3, 1, 1)

        self.a_2 = QPushButton(self.scrollAreaWidgetContents)
        self.a_2.setObjectName(u"a_2")
        sizePolicy2.setHeightForWidth(self.a_2.sizePolicy().hasHeightForWidth())
        self.a_2.setSizePolicy(sizePolicy2)
        self.a_2.setMaximumSize(QSize(40, 30))
        self.a_2.setFont(font2)
        self.a_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_2.addWidget(self.a_2, 1, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.grid_2.addWidget(self.label_2, 0, 0, 1, 4)

        self.c_2 = QLabel(self.scrollAreaWidgetContents)
        self.c_2.setObjectName(u"c_2")
        sizePolicy3.setHeightForWidth(self.c_2.sizePolicy().hasHeightForWidth())
        self.c_2.setSizePolicy(sizePolicy3)
        self.c_2.setMaximumSize(QSize(16777215, 30))
        self.c_2.setFont(font2)
        self.c_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_2.setAlignment(Qt.AlignCenter)
        self.c_2.setMargin(2)

        self.grid_2.addWidget(self.c_2, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.grid_2, 1, 0, 1, 1)

        self.grid_12 = QGridLayout()
        self.grid_12.setSpacing(5)
        self.grid_12.setObjectName(u"grid_12")
        self.b_33 = QPushButton(self.scrollAreaWidgetContents)
        self.b_33.setObjectName(u"b_33")
        sizePolicy1.setHeightForWidth(self.b_33.sizePolicy().hasHeightForWidth())
        self.b_33.setSizePolicy(sizePolicy1)
        self.b_33.setMaximumSize(QSize(30, 30))
        self.b_33.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_33.setIcon(icon)

        self.grid_12.addWidget(self.b_33, 3, 3, 1, 1)

        self.b_34 = QPushButton(self.scrollAreaWidgetContents)
        self.b_34.setObjectName(u"b_34")
        sizePolicy1.setHeightForWidth(self.b_34.sizePolicy().hasHeightForWidth())
        self.b_34.setSizePolicy(sizePolicy1)
        self.b_34.setMaximumSize(QSize(30, 30))
        self.b_34.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_34.setIcon(icon)

        self.grid_12.addWidget(self.b_34, 4, 3, 1, 1)

        self.a_33 = QPushButton(self.scrollAreaWidgetContents)
        self.a_33.setObjectName(u"a_33")
        sizePolicy2.setHeightForWidth(self.a_33.sizePolicy().hasHeightForWidth())
        self.a_33.setSizePolicy(sizePolicy2)
        self.a_33.setMaximumSize(QSize(40, 30))
        self.a_33.setFont(font2)
        self.a_33.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_33, 3, 1, 1, 1)

        self.a_36 = QPushButton(self.scrollAreaWidgetContents)
        self.a_36.setObjectName(u"a_36")
        sizePolicy2.setHeightForWidth(self.a_36.sizePolicy().hasHeightForWidth())
        self.a_36.setSizePolicy(sizePolicy2)
        self.a_36.setMaximumSize(QSize(40, 30))
        self.a_36.setFont(font2)
        self.a_36.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_36, 6, 1, 1, 1)

        self.a_32 = QPushButton(self.scrollAreaWidgetContents)
        self.a_32.setObjectName(u"a_32")
        sizePolicy2.setHeightForWidth(self.a_32.sizePolicy().hasHeightForWidth())
        self.a_32.setSizePolicy(sizePolicy2)
        self.a_32.setMaximumSize(QSize(40, 30))
        self.a_32.setFont(font2)
        self.a_32.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_32, 2, 1, 1, 1)

        self.b_36 = QPushButton(self.scrollAreaWidgetContents)
        self.b_36.setObjectName(u"b_36")
        sizePolicy1.setHeightForWidth(self.b_36.sizePolicy().hasHeightForWidth())
        self.b_36.setSizePolicy(sizePolicy1)
        self.b_36.setMaximumSize(QSize(30, 30))
        self.b_36.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_36.setIcon(icon)

        self.grid_12.addWidget(self.b_36, 6, 3, 1, 1)

        self.p_33 = QPushButton(self.scrollAreaWidgetContents)
        self.p_33.setObjectName(u"p_33")
        sizePolicy1.setHeightForWidth(self.p_33.sizePolicy().hasHeightForWidth())
        self.p_33.setSizePolicy(sizePolicy1)
        self.p_33.setMaximumSize(QSize(16777215, 30))
        self.p_33.setFont(font1)
        self.p_33.setCursor(QCursor(Qt.ArrowCursor))
        self.p_33.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_33, 3, 0, 1, 1)

        self.p_31 = QPushButton(self.scrollAreaWidgetContents)
        self.p_31.setObjectName(u"p_31")
        sizePolicy1.setHeightForWidth(self.p_31.sizePolicy().hasHeightForWidth())
        self.p_31.setSizePolicy(sizePolicy1)
        self.p_31.setMaximumSize(QSize(16777215, 30))
        self.p_31.setFont(font1)
        self.p_31.setCursor(QCursor(Qt.ArrowCursor))
        self.p_31.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_31, 1, 0, 1, 1)

        self.a_35 = QPushButton(self.scrollAreaWidgetContents)
        self.a_35.setObjectName(u"a_35")
        sizePolicy2.setHeightForWidth(self.a_35.sizePolicy().hasHeightForWidth())
        self.a_35.setSizePolicy(sizePolicy2)
        self.a_35.setMaximumSize(QSize(40, 30))
        self.a_35.setFont(font2)
        self.a_35.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_35, 5, 1, 1, 1)

        self.b_37 = QPushButton(self.scrollAreaWidgetContents)
        self.b_37.setObjectName(u"b_37")
        sizePolicy1.setHeightForWidth(self.b_37.sizePolicy().hasHeightForWidth())
        self.b_37.setSizePolicy(sizePolicy1)
        self.b_37.setMaximumSize(QSize(30, 30))
        self.b_37.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_37.setIcon(icon)

        self.grid_12.addWidget(self.b_37, 7, 3, 1, 1)

        self.b_31 = QPushButton(self.scrollAreaWidgetContents)
        self.b_31.setObjectName(u"b_31")
        sizePolicy1.setHeightForWidth(self.b_31.sizePolicy().hasHeightForWidth())
        self.b_31.setSizePolicy(sizePolicy1)
        self.b_31.setMaximumSize(QSize(30, 30))
        self.b_31.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_31.setIcon(icon)

        self.grid_12.addWidget(self.b_31, 1, 3, 1, 1)

        self.p_32 = QPushButton(self.scrollAreaWidgetContents)
        self.p_32.setObjectName(u"p_32")
        sizePolicy1.setHeightForWidth(self.p_32.sizePolicy().hasHeightForWidth())
        self.p_32.setSizePolicy(sizePolicy1)
        self.p_32.setMaximumSize(QSize(16777215, 30))
        self.p_32.setFont(font1)
        self.p_32.setCursor(QCursor(Qt.ArrowCursor))
        self.p_32.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_32, 2, 0, 1, 1)

        self.p_34 = QPushButton(self.scrollAreaWidgetContents)
        self.p_34.setObjectName(u"p_34")
        sizePolicy1.setHeightForWidth(self.p_34.sizePolicy().hasHeightForWidth())
        self.p_34.setSizePolicy(sizePolicy1)
        self.p_34.setMaximumSize(QSize(16777215, 30))
        self.p_34.setFont(font1)
        self.p_34.setCursor(QCursor(Qt.ArrowCursor))
        self.p_34.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_34, 4, 0, 1, 1)

        self.p_35 = QPushButton(self.scrollAreaWidgetContents)
        self.p_35.setObjectName(u"p_35")
        sizePolicy1.setHeightForWidth(self.p_35.sizePolicy().hasHeightForWidth())
        self.p_35.setSizePolicy(sizePolicy1)
        self.p_35.setMaximumSize(QSize(16777215, 30))
        self.p_35.setFont(font1)
        self.p_35.setCursor(QCursor(Qt.ArrowCursor))
        self.p_35.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_35, 5, 0, 1, 1)

        self.p_37 = QPushButton(self.scrollAreaWidgetContents)
        self.p_37.setObjectName(u"p_37")
        sizePolicy1.setHeightForWidth(self.p_37.sizePolicy().hasHeightForWidth())
        self.p_37.setSizePolicy(sizePolicy1)
        self.p_37.setMaximumSize(QSize(16777215, 30))
        self.p_37.setFont(font1)
        self.p_37.setCursor(QCursor(Qt.ArrowCursor))
        self.p_37.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_37, 7, 0, 1, 1)

        self.a_37 = QPushButton(self.scrollAreaWidgetContents)
        self.a_37.setObjectName(u"a_37")
        sizePolicy2.setHeightForWidth(self.a_37.sizePolicy().hasHeightForWidth())
        self.a_37.setSizePolicy(sizePolicy2)
        self.a_37.setMaximumSize(QSize(40, 30))
        self.a_37.setFont(font)
        self.a_37.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_37, 7, 1, 1, 1)

        self.a_34 = QPushButton(self.scrollAreaWidgetContents)
        self.a_34.setObjectName(u"a_34")
        sizePolicy2.setHeightForWidth(self.a_34.sizePolicy().hasHeightForWidth())
        self.a_34.setSizePolicy(sizePolicy2)
        self.a_34.setMaximumSize(QSize(40, 30))
        self.a_34.setFont(font2)
        self.a_34.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_34, 4, 1, 1, 1)

        self.a_31 = QPushButton(self.scrollAreaWidgetContents)
        self.a_31.setObjectName(u"a_31")
        sizePolicy2.setHeightForWidth(self.a_31.sizePolicy().hasHeightForWidth())
        self.a_31.setSizePolicy(sizePolicy2)
        self.a_31.setMaximumSize(QSize(40, 30))
        self.a_31.setFont(font2)
        self.a_31.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_12.addWidget(self.a_31, 1, 1, 1, 1)

        self.b_35 = QPushButton(self.scrollAreaWidgetContents)
        self.b_35.setObjectName(u"b_35")
        sizePolicy1.setHeightForWidth(self.b_35.sizePolicy().hasHeightForWidth())
        self.b_35.setSizePolicy(sizePolicy1)
        self.b_35.setMaximumSize(QSize(30, 30))
        self.b_35.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_35.setIcon(icon)

        self.grid_12.addWidget(self.b_35, 5, 3, 1, 1)

        self.p_36 = QPushButton(self.scrollAreaWidgetContents)
        self.p_36.setObjectName(u"p_36")
        sizePolicy1.setHeightForWidth(self.p_36.sizePolicy().hasHeightForWidth())
        self.p_36.setSizePolicy(sizePolicy1)
        self.p_36.setMaximumSize(QSize(16777215, 30))
        self.p_36.setFont(font1)
        self.p_36.setCursor(QCursor(Qt.ArrowCursor))
        self.p_36.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_12.addWidget(self.p_36, 6, 0, 1, 1)

        self.b_32 = QPushButton(self.scrollAreaWidgetContents)
        self.b_32.setObjectName(u"b_32")
        sizePolicy1.setHeightForWidth(self.b_32.sizePolicy().hasHeightForWidth())
        self.b_32.setSizePolicy(sizePolicy1)
        self.b_32.setMaximumSize(QSize(30, 30))
        self.b_32.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_32.setIcon(icon)

        self.grid_12.addWidget(self.b_32, 2, 3, 1, 1)

        self.c_31 = QLabel(self.scrollAreaWidgetContents)
        self.c_31.setObjectName(u"c_31")
        sizePolicy3.setHeightForWidth(self.c_31.sizePolicy().hasHeightForWidth())
        self.c_31.setSizePolicy(sizePolicy3)
        self.c_31.setMaximumSize(QSize(16777215, 30))
        self.c_31.setFont(font2)
        self.c_31.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_31.setAlignment(Qt.AlignCenter)
        self.c_31.setMargin(2)

        self.grid_12.addWidget(self.c_31, 1, 2, 1, 1)

        self.c_32 = QLabel(self.scrollAreaWidgetContents)
        self.c_32.setObjectName(u"c_32")
        sizePolicy3.setHeightForWidth(self.c_32.sizePolicy().hasHeightForWidth())
        self.c_32.setSizePolicy(sizePolicy3)
        self.c_32.setMaximumSize(QSize(16777215, 30))
        self.c_32.setFont(font2)
        self.c_32.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_32.setAlignment(Qt.AlignCenter)
        self.c_32.setMargin(2)

        self.grid_12.addWidget(self.c_32, 2, 2, 1, 1)

        self.c_33 = QLabel(self.scrollAreaWidgetContents)
        self.c_33.setObjectName(u"c_33")
        sizePolicy3.setHeightForWidth(self.c_33.sizePolicy().hasHeightForWidth())
        self.c_33.setSizePolicy(sizePolicy3)
        self.c_33.setMaximumSize(QSize(16777215, 30))
        self.c_33.setFont(font2)
        self.c_33.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_33.setAlignment(Qt.AlignCenter)
        self.c_33.setMargin(2)

        self.grid_12.addWidget(self.c_33, 3, 2, 1, 1)

        self.c_34 = QLabel(self.scrollAreaWidgetContents)
        self.c_34.setObjectName(u"c_34")
        sizePolicy3.setHeightForWidth(self.c_34.sizePolicy().hasHeightForWidth())
        self.c_34.setSizePolicy(sizePolicy3)
        self.c_34.setMaximumSize(QSize(16777215, 30))
        self.c_34.setFont(font2)
        self.c_34.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_34.setAlignment(Qt.AlignCenter)
        self.c_34.setMargin(2)

        self.grid_12.addWidget(self.c_34, 4, 2, 1, 1)

        self.c_35 = QLabel(self.scrollAreaWidgetContents)
        self.c_35.setObjectName(u"c_35")
        sizePolicy3.setHeightForWidth(self.c_35.sizePolicy().hasHeightForWidth())
        self.c_35.setSizePolicy(sizePolicy3)
        self.c_35.setMaximumSize(QSize(16777215, 30))
        self.c_35.setFont(font2)
        self.c_35.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_35.setAlignment(Qt.AlignCenter)
        self.c_35.setMargin(2)

        self.grid_12.addWidget(self.c_35, 5, 2, 1, 1)

        self.c_36 = QLabel(self.scrollAreaWidgetContents)
        self.c_36.setObjectName(u"c_36")
        sizePolicy3.setHeightForWidth(self.c_36.sizePolicy().hasHeightForWidth())
        self.c_36.setSizePolicy(sizePolicy3)
        self.c_36.setMaximumSize(QSize(16777215, 30))
        self.c_36.setFont(font2)
        self.c_36.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_36.setAlignment(Qt.AlignCenter)
        self.c_36.setMargin(2)

        self.grid_12.addWidget(self.c_36, 6, 2, 1, 1)

        self.c_37 = QLabel(self.scrollAreaWidgetContents)
        self.c_37.setObjectName(u"c_37")
        sizePolicy3.setHeightForWidth(self.c_37.sizePolicy().hasHeightForWidth())
        self.c_37.setSizePolicy(sizePolicy3)
        self.c_37.setMaximumSize(QSize(16777215, 30))
        self.c_37.setFont(font2)
        self.c_37.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_37.setAlignment(Qt.AlignCenter)
        self.c_37.setMargin(2)

        self.grid_12.addWidget(self.c_37, 7, 2, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.grid_12.addWidget(self.label_12, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_12, 1, 2, 1, 1)

        self.grid_9 = QGridLayout()
        self.grid_9.setSpacing(5)
        self.grid_9.setObjectName(u"grid_9")
        self.p_20 = QPushButton(self.scrollAreaWidgetContents)
        self.p_20.setObjectName(u"p_20")
        sizePolicy1.setHeightForWidth(self.p_20.sizePolicy().hasHeightForWidth())
        self.p_20.setSizePolicy(sizePolicy1)
        self.p_20.setMaximumSize(QSize(16777215, 30))
        self.p_20.setFont(font1)
        self.p_20.setCursor(QCursor(Qt.ArrowCursor))
        self.p_20.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_9.addWidget(self.p_20, 3, 0, 1, 1)

        self.b_21 = QPushButton(self.scrollAreaWidgetContents)
        self.b_21.setObjectName(u"b_21")
        sizePolicy1.setHeightForWidth(self.b_21.sizePolicy().hasHeightForWidth())
        self.b_21.setSizePolicy(sizePolicy1)
        self.b_21.setMaximumSize(QSize(30, 30))
        self.b_21.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_21.setIcon(icon)

        self.grid_9.addWidget(self.b_21, 4, 3, 1, 1)

        self.b_19 = QPushButton(self.scrollAreaWidgetContents)
        self.b_19.setObjectName(u"b_19")
        sizePolicy1.setHeightForWidth(self.b_19.sizePolicy().hasHeightForWidth())
        self.b_19.setSizePolicy(sizePolicy1)
        self.b_19.setMaximumSize(QSize(30, 30))
        self.b_19.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_19.setIcon(icon)

        self.grid_9.addWidget(self.b_19, 2, 3, 1, 1)

        self.a_18 = QPushButton(self.scrollAreaWidgetContents)
        self.a_18.setObjectName(u"a_18")
        sizePolicy2.setHeightForWidth(self.a_18.sizePolicy().hasHeightForWidth())
        self.a_18.setSizePolicy(sizePolicy2)
        self.a_18.setMaximumSize(QSize(40, 30))
        self.a_18.setFont(font2)
        self.a_18.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_9.addWidget(self.a_18, 1, 1, 1, 1)

        self.a_21 = QPushButton(self.scrollAreaWidgetContents)
        self.a_21.setObjectName(u"a_21")
        sizePolicy2.setHeightForWidth(self.a_21.sizePolicy().hasHeightForWidth())
        self.a_21.setSizePolicy(sizePolicy2)
        self.a_21.setMaximumSize(QSize(40, 30))
        self.a_21.setFont(font2)
        self.a_21.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_9.addWidget(self.a_21, 4, 1, 1, 1)

        self.a_20 = QPushButton(self.scrollAreaWidgetContents)
        self.a_20.setObjectName(u"a_20")
        sizePolicy2.setHeightForWidth(self.a_20.sizePolicy().hasHeightForWidth())
        self.a_20.setSizePolicy(sizePolicy2)
        self.a_20.setMaximumSize(QSize(40, 30))
        self.a_20.setFont(font2)
        self.a_20.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_9.addWidget(self.a_20, 3, 1, 1, 1)

        self.p_18 = QPushButton(self.scrollAreaWidgetContents)
        self.p_18.setObjectName(u"p_18")
        sizePolicy1.setHeightForWidth(self.p_18.sizePolicy().hasHeightForWidth())
        self.p_18.setSizePolicy(sizePolicy1)
        self.p_18.setMaximumSize(QSize(16777215, 30))
        self.p_18.setFont(font1)
        self.p_18.setCursor(QCursor(Qt.ArrowCursor))
        self.p_18.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_9.addWidget(self.p_18, 1, 0, 1, 1)

        self.b_18 = QPushButton(self.scrollAreaWidgetContents)
        self.b_18.setObjectName(u"b_18")
        sizePolicy1.setHeightForWidth(self.b_18.sizePolicy().hasHeightForWidth())
        self.b_18.setSizePolicy(sizePolicy1)
        self.b_18.setMaximumSize(QSize(30, 30))
        self.b_18.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_18.setIcon(icon)

        self.grid_9.addWidget(self.b_18, 1, 3, 1, 1)

        self.p_21 = QPushButton(self.scrollAreaWidgetContents)
        self.p_21.setObjectName(u"p_21")
        sizePolicy1.setHeightForWidth(self.p_21.sizePolicy().hasHeightForWidth())
        self.p_21.setSizePolicy(sizePolicy1)
        self.p_21.setMaximumSize(QSize(16777215, 30))
        self.p_21.setFont(font1)
        self.p_21.setCursor(QCursor(Qt.ArrowCursor))
        self.p_21.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_9.addWidget(self.p_21, 4, 0, 1, 1)

        self.c_19 = QLabel(self.scrollAreaWidgetContents)
        self.c_19.setObjectName(u"c_19")
        sizePolicy3.setHeightForWidth(self.c_19.sizePolicy().hasHeightForWidth())
        self.c_19.setSizePolicy(sizePolicy3)
        self.c_19.setMaximumSize(QSize(16777215, 30))
        self.c_19.setFont(font2)
        self.c_19.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_19.setAlignment(Qt.AlignCenter)
        self.c_19.setMargin(2)

        self.grid_9.addWidget(self.c_19, 2, 2, 1, 1)

        self.c_20 = QLabel(self.scrollAreaWidgetContents)
        self.c_20.setObjectName(u"c_20")
        sizePolicy3.setHeightForWidth(self.c_20.sizePolicy().hasHeightForWidth())
        self.c_20.setSizePolicy(sizePolicy3)
        self.c_20.setMaximumSize(QSize(16777215, 30))
        self.c_20.setFont(font2)
        self.c_20.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_20.setAlignment(Qt.AlignCenter)
        self.c_20.setMargin(2)

        self.grid_9.addWidget(self.c_20, 3, 2, 1, 1)

        self.p_19 = QPushButton(self.scrollAreaWidgetContents)
        self.p_19.setObjectName(u"p_19")
        sizePolicy1.setHeightForWidth(self.p_19.sizePolicy().hasHeightForWidth())
        self.p_19.setSizePolicy(sizePolicy1)
        self.p_19.setMaximumSize(QSize(16777215, 30))
        self.p_19.setFont(font1)
        self.p_19.setCursor(QCursor(Qt.ArrowCursor))
        self.p_19.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_9.addWidget(self.p_19, 2, 0, 1, 1)

        self.a_19 = QPushButton(self.scrollAreaWidgetContents)
        self.a_19.setObjectName(u"a_19")
        sizePolicy2.setHeightForWidth(self.a_19.sizePolicy().hasHeightForWidth())
        self.a_19.setSizePolicy(sizePolicy2)
        self.a_19.setMaximumSize(QSize(40, 30))
        self.a_19.setFont(font2)
        self.a_19.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_9.addWidget(self.a_19, 2, 1, 1, 1)

        self.b_20 = QPushButton(self.scrollAreaWidgetContents)
        self.b_20.setObjectName(u"b_20")
        sizePolicy1.setHeightForWidth(self.b_20.sizePolicy().hasHeightForWidth())
        self.b_20.setSizePolicy(sizePolicy1)
        self.b_20.setMaximumSize(QSize(30, 30))
        self.b_20.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_20.setIcon(icon)

        self.grid_9.addWidget(self.b_20, 3, 3, 1, 1)

        self.c_21 = QLabel(self.scrollAreaWidgetContents)
        self.c_21.setObjectName(u"c_21")
        sizePolicy3.setHeightForWidth(self.c_21.sizePolicy().hasHeightForWidth())
        self.c_21.setSizePolicy(sizePolicy3)
        self.c_21.setMaximumSize(QSize(16777215, 30))
        self.c_21.setFont(font2)
        self.c_21.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_21.setAlignment(Qt.AlignCenter)
        self.c_21.setMargin(2)

        self.grid_9.addWidget(self.c_21, 4, 2, 1, 1)

        self.c_18 = QLabel(self.scrollAreaWidgetContents)
        self.c_18.setObjectName(u"c_18")
        sizePolicy3.setHeightForWidth(self.c_18.sizePolicy().hasHeightForWidth())
        self.c_18.setSizePolicy(sizePolicy3)
        self.c_18.setMaximumSize(QSize(16777215, 30))
        self.c_18.setFont(font2)
        self.c_18.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_18.setAlignment(Qt.AlignCenter)
        self.c_18.setMargin(2)

        self.grid_9.addWidget(self.c_18, 1, 2, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.grid_9.addWidget(self.label_9, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_9, 3, 1, 1, 1)

        self.grid_13 = QGridLayout()
        self.grid_13.setSpacing(5)
        self.grid_13.setObjectName(u"grid_13")
        self.p_38 = QPushButton(self.scrollAreaWidgetContents)
        self.p_38.setObjectName(u"p_38")
        sizePolicy1.setHeightForWidth(self.p_38.sizePolicy().hasHeightForWidth())
        self.p_38.setSizePolicy(sizePolicy1)
        self.p_38.setMaximumSize(QSize(16777215, 30))
        self.p_38.setFont(font1)
        self.p_38.setCursor(QCursor(Qt.ArrowCursor))
        self.p_38.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_13.addWidget(self.p_38, 1, 0, 1, 1)

        self.c_38 = QLabel(self.scrollAreaWidgetContents)
        self.c_38.setObjectName(u"c_38")
        sizePolicy3.setHeightForWidth(self.c_38.sizePolicy().hasHeightForWidth())
        self.c_38.setSizePolicy(sizePolicy3)
        self.c_38.setMaximumSize(QSize(16777215, 30))
        self.c_38.setFont(font2)
        self.c_38.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_38.setAlignment(Qt.AlignCenter)
        self.c_38.setMargin(2)

        self.grid_13.addWidget(self.c_38, 1, 2, 1, 1)

        self.c_39 = QLabel(self.scrollAreaWidgetContents)
        self.c_39.setObjectName(u"c_39")
        sizePolicy3.setHeightForWidth(self.c_39.sizePolicy().hasHeightForWidth())
        self.c_39.setSizePolicy(sizePolicy3)
        self.c_39.setMaximumSize(QSize(16777215, 30))
        self.c_39.setFont(font2)
        self.c_39.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_39.setAlignment(Qt.AlignCenter)
        self.c_39.setMargin(2)

        self.grid_13.addWidget(self.c_39, 2, 2, 1, 1)

        self.a_39 = QPushButton(self.scrollAreaWidgetContents)
        self.a_39.setObjectName(u"a_39")
        sizePolicy2.setHeightForWidth(self.a_39.sizePolicy().hasHeightForWidth())
        self.a_39.setSizePolicy(sizePolicy2)
        self.a_39.setMaximumSize(QSize(40, 30))
        self.a_39.setFont(font2)
        self.a_39.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_13.addWidget(self.a_39, 2, 1, 1, 1)

        self.c_40 = QLabel(self.scrollAreaWidgetContents)
        self.c_40.setObjectName(u"c_40")
        sizePolicy3.setHeightForWidth(self.c_40.sizePolicy().hasHeightForWidth())
        self.c_40.setSizePolicy(sizePolicy3)
        self.c_40.setMaximumSize(QSize(16777215, 30))
        self.c_40.setFont(font2)
        self.c_40.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_40.setAlignment(Qt.AlignCenter)
        self.c_40.setMargin(2)

        self.grid_13.addWidget(self.c_40, 3, 2, 1, 1)

        self.p_39 = QPushButton(self.scrollAreaWidgetContents)
        self.p_39.setObjectName(u"p_39")
        sizePolicy1.setHeightForWidth(self.p_39.sizePolicy().hasHeightForWidth())
        self.p_39.setSizePolicy(sizePolicy1)
        self.p_39.setMaximumSize(QSize(16777215, 30))
        self.p_39.setFont(font1)
        self.p_39.setCursor(QCursor(Qt.ArrowCursor))
        self.p_39.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_13.addWidget(self.p_39, 2, 0, 1, 1)

        self.b_38 = QPushButton(self.scrollAreaWidgetContents)
        self.b_38.setObjectName(u"b_38")
        sizePolicy1.setHeightForWidth(self.b_38.sizePolicy().hasHeightForWidth())
        self.b_38.setSizePolicy(sizePolicy1)
        self.b_38.setMaximumSize(QSize(30, 30))
        self.b_38.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_38.setIcon(icon)

        self.grid_13.addWidget(self.b_38, 1, 3, 1, 1)

        self.a_38 = QPushButton(self.scrollAreaWidgetContents)
        self.a_38.setObjectName(u"a_38")
        sizePolicy2.setHeightForWidth(self.a_38.sizePolicy().hasHeightForWidth())
        self.a_38.setSizePolicy(sizePolicy2)
        self.a_38.setMaximumSize(QSize(40, 30))
        self.a_38.setFont(font2)
        self.a_38.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_13.addWidget(self.a_38, 1, 1, 1, 1)

        self.p_40 = QPushButton(self.scrollAreaWidgetContents)
        self.p_40.setObjectName(u"p_40")
        sizePolicy1.setHeightForWidth(self.p_40.sizePolicy().hasHeightForWidth())
        self.p_40.setSizePolicy(sizePolicy1)
        self.p_40.setMaximumSize(QSize(16777215, 30))
        self.p_40.setFont(font1)
        self.p_40.setCursor(QCursor(Qt.ArrowCursor))
        self.p_40.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_13.addWidget(self.p_40, 3, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.grid_13.addWidget(self.label_13, 0, 0, 1, 4)

        self.b_39 = QPushButton(self.scrollAreaWidgetContents)
        self.b_39.setObjectName(u"b_39")
        sizePolicy1.setHeightForWidth(self.b_39.sizePolicy().hasHeightForWidth())
        self.b_39.setSizePolicy(sizePolicy1)
        self.b_39.setMaximumSize(QSize(30, 30))
        self.b_39.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_39.setIcon(icon)

        self.grid_13.addWidget(self.b_39, 2, 3, 1, 1)

        self.a_40 = QPushButton(self.scrollAreaWidgetContents)
        self.a_40.setObjectName(u"a_40")
        sizePolicy2.setHeightForWidth(self.a_40.sizePolicy().hasHeightForWidth())
        self.a_40.setSizePolicy(sizePolicy2)
        self.a_40.setMaximumSize(QSize(40, 30))
        self.a_40.setFont(font2)
        self.a_40.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_13.addWidget(self.a_40, 3, 1, 1, 1)

        self.b_40 = QPushButton(self.scrollAreaWidgetContents)
        self.b_40.setObjectName(u"b_40")
        sizePolicy1.setHeightForWidth(self.b_40.sizePolicy().hasHeightForWidth())
        self.b_40.setSizePolicy(sizePolicy1)
        self.b_40.setMaximumSize(QSize(30, 30))
        self.b_40.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_40.setIcon(icon)

        self.grid_13.addWidget(self.b_40, 3, 3, 1, 1)


        self.gridLayout_5.addLayout(self.grid_13, 2, 2, 1, 1)

        self.grid_1 = QGridLayout()
        self.grid_1.setSpacing(5)
        self.grid_1.setObjectName(u"grid_1")
        self.a_1 = QPushButton(self.scrollAreaWidgetContents)
        self.a_1.setObjectName(u"a_1")
        sizePolicy2.setHeightForWidth(self.a_1.sizePolicy().hasHeightForWidth())
        self.a_1.setSizePolicy(sizePolicy2)
        self.a_1.setMaximumSize(QSize(40, 30))
        self.a_1.setFont(font2)
        self.a_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_1.addWidget(self.a_1, 1, 1, 1, 1)

        self.b_1 = QPushButton(self.scrollAreaWidgetContents)
        self.b_1.setObjectName(u"b_1")
        sizePolicy1.setHeightForWidth(self.b_1.sizePolicy().hasHeightForWidth())
        self.b_1.setSizePolicy(sizePolicy1)
        self.b_1.setMaximumSize(QSize(30, 30))
        self.b_1.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_1.setIcon(icon)

        self.grid_1.addWidget(self.b_1, 1, 3, 1, 1)

        self.p_1 = QPushButton(self.scrollAreaWidgetContents)
        self.p_1.setObjectName(u"p_1")
        sizePolicy1.setHeightForWidth(self.p_1.sizePolicy().hasHeightForWidth())
        self.p_1.setSizePolicy(sizePolicy1)
        self.p_1.setMaximumSize(QSize(16777215, 30))
        self.p_1.setFont(font1)
        self.p_1.setCursor(QCursor(Qt.ArrowCursor))
        self.p_1.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_1.addWidget(self.p_1, 1, 0, 1, 1)

        self.c_1 = QLabel(self.scrollAreaWidgetContents)
        self.c_1.setObjectName(u"c_1")
        sizePolicy3.setHeightForWidth(self.c_1.sizePolicy().hasHeightForWidth())
        self.c_1.setSizePolicy(sizePolicy3)
        self.c_1.setMaximumSize(QSize(16777215, 30))
        self.c_1.setFont(font2)
        self.c_1.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_1.setAlignment(Qt.AlignCenter)
        self.c_1.setMargin(2)

        self.grid_1.addWidget(self.c_1, 1, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.grid_1.addWidget(self.label, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_1, 0, 0, 1, 1)

        self.grid_10 = QGridLayout()
        self.grid_10.setSpacing(5)
        self.grid_10.setObjectName(u"grid_10")
        self.p_24 = QPushButton(self.scrollAreaWidgetContents)
        self.p_24.setObjectName(u"p_24")
        sizePolicy1.setHeightForWidth(self.p_24.sizePolicy().hasHeightForWidth())
        self.p_24.setSizePolicy(sizePolicy1)
        self.p_24.setMaximumSize(QSize(16777215, 30))
        self.p_24.setFont(font1)
        self.p_24.setCursor(QCursor(Qt.ArrowCursor))
        self.p_24.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_10.addWidget(self.p_24, 3, 0, 1, 1)

        self.p_25 = QPushButton(self.scrollAreaWidgetContents)
        self.p_25.setObjectName(u"p_25")
        sizePolicy1.setHeightForWidth(self.p_25.sizePolicy().hasHeightForWidth())
        self.p_25.setSizePolicy(sizePolicy1)
        self.p_25.setMaximumSize(QSize(16777215, 30))
        self.p_25.setFont(font1)
        self.p_25.setCursor(QCursor(Qt.ArrowCursor))
        self.p_25.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_10.addWidget(self.p_25, 4, 0, 1, 1)

        self.b_22 = QPushButton(self.scrollAreaWidgetContents)
        self.b_22.setObjectName(u"b_22")
        sizePolicy1.setHeightForWidth(self.b_22.sizePolicy().hasHeightForWidth())
        self.b_22.setSizePolicy(sizePolicy1)
        self.b_22.setMaximumSize(QSize(30, 30))
        self.b_22.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_22.setIcon(icon)

        self.grid_10.addWidget(self.b_22, 1, 3, 1, 1)

        self.a_22 = QPushButton(self.scrollAreaWidgetContents)
        self.a_22.setObjectName(u"a_22")
        sizePolicy2.setHeightForWidth(self.a_22.sizePolicy().hasHeightForWidth())
        self.a_22.setSizePolicy(sizePolicy2)
        self.a_22.setMaximumSize(QSize(40, 30))
        self.a_22.setFont(font2)
        self.a_22.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_10.addWidget(self.a_22, 1, 1, 1, 1)

        self.p_22 = QPushButton(self.scrollAreaWidgetContents)
        self.p_22.setObjectName(u"p_22")
        sizePolicy1.setHeightForWidth(self.p_22.sizePolicy().hasHeightForWidth())
        self.p_22.setSizePolicy(sizePolicy1)
        self.p_22.setMaximumSize(QSize(16777215, 30))
        self.p_22.setFont(font1)
        self.p_22.setCursor(QCursor(Qt.ArrowCursor))
        self.p_22.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_10.addWidget(self.p_22, 1, 0, 1, 1)

        self.a_23 = QPushButton(self.scrollAreaWidgetContents)
        self.a_23.setObjectName(u"a_23")
        sizePolicy2.setHeightForWidth(self.a_23.sizePolicy().hasHeightForWidth())
        self.a_23.setSizePolicy(sizePolicy2)
        self.a_23.setMaximumSize(QSize(40, 30))
        self.a_23.setFont(font2)
        self.a_23.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_10.addWidget(self.a_23, 2, 1, 1, 1)

        self.p_23 = QPushButton(self.scrollAreaWidgetContents)
        self.p_23.setObjectName(u"p_23")
        sizePolicy1.setHeightForWidth(self.p_23.sizePolicy().hasHeightForWidth())
        self.p_23.setSizePolicy(sizePolicy1)
        self.p_23.setMaximumSize(QSize(16777215, 30))
        self.p_23.setFont(font1)
        self.p_23.setCursor(QCursor(Qt.ArrowCursor))
        self.p_23.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_10.addWidget(self.p_23, 2, 0, 1, 1)

        self.b_24 = QPushButton(self.scrollAreaWidgetContents)
        self.b_24.setObjectName(u"b_24")
        sizePolicy1.setHeightForWidth(self.b_24.sizePolicy().hasHeightForWidth())
        self.b_24.setSizePolicy(sizePolicy1)
        self.b_24.setMaximumSize(QSize(30, 30))
        self.b_24.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_24.setIcon(icon)

        self.grid_10.addWidget(self.b_24, 3, 3, 1, 1)

        self.b_23 = QPushButton(self.scrollAreaWidgetContents)
        self.b_23.setObjectName(u"b_23")
        sizePolicy1.setHeightForWidth(self.b_23.sizePolicy().hasHeightForWidth())
        self.b_23.setSizePolicy(sizePolicy1)
        self.b_23.setMaximumSize(QSize(30, 30))
        self.b_23.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_23.setIcon(icon)

        self.grid_10.addWidget(self.b_23, 2, 3, 1, 1)

        self.a_25 = QPushButton(self.scrollAreaWidgetContents)
        self.a_25.setObjectName(u"a_25")
        sizePolicy2.setHeightForWidth(self.a_25.sizePolicy().hasHeightForWidth())
        self.a_25.setSizePolicy(sizePolicy2)
        self.a_25.setMaximumSize(QSize(40, 30))
        self.a_25.setFont(font2)
        self.a_25.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_10.addWidget(self.a_25, 4, 1, 1, 1)

        self.b_25 = QPushButton(self.scrollAreaWidgetContents)
        self.b_25.setObjectName(u"b_25")
        sizePolicy1.setHeightForWidth(self.b_25.sizePolicy().hasHeightForWidth())
        self.b_25.setSizePolicy(sizePolicy1)
        self.b_25.setMaximumSize(QSize(30, 30))
        self.b_25.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_25.setIcon(icon)

        self.grid_10.addWidget(self.b_25, 4, 3, 1, 1)

        self.a_24 = QPushButton(self.scrollAreaWidgetContents)
        self.a_24.setObjectName(u"a_24")
        sizePolicy2.setHeightForWidth(self.a_24.sizePolicy().hasHeightForWidth())
        self.a_24.setSizePolicy(sizePolicy2)
        self.a_24.setMaximumSize(QSize(40, 30))
        self.a_24.setFont(font2)
        self.a_24.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_10.addWidget(self.a_24, 3, 1, 1, 1)

        self.c_22 = QLabel(self.scrollAreaWidgetContents)
        self.c_22.setObjectName(u"c_22")
        sizePolicy3.setHeightForWidth(self.c_22.sizePolicy().hasHeightForWidth())
        self.c_22.setSizePolicy(sizePolicy3)
        self.c_22.setMaximumSize(QSize(16777215, 30))
        self.c_22.setFont(font2)
        self.c_22.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_22.setAlignment(Qt.AlignCenter)
        self.c_22.setMargin(2)

        self.grid_10.addWidget(self.c_22, 1, 2, 1, 1)

        self.c_23 = QLabel(self.scrollAreaWidgetContents)
        self.c_23.setObjectName(u"c_23")
        sizePolicy3.setHeightForWidth(self.c_23.sizePolicy().hasHeightForWidth())
        self.c_23.setSizePolicy(sizePolicy3)
        self.c_23.setMaximumSize(QSize(16777215, 30))
        self.c_23.setFont(font2)
        self.c_23.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_23.setAlignment(Qt.AlignCenter)
        self.c_23.setMargin(2)

        self.grid_10.addWidget(self.c_23, 2, 2, 1, 1)

        self.c_24 = QLabel(self.scrollAreaWidgetContents)
        self.c_24.setObjectName(u"c_24")
        sizePolicy3.setHeightForWidth(self.c_24.sizePolicy().hasHeightForWidth())
        self.c_24.setSizePolicy(sizePolicy3)
        self.c_24.setMaximumSize(QSize(16777215, 30))
        self.c_24.setFont(font2)
        self.c_24.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_24.setAlignment(Qt.AlignCenter)
        self.c_24.setMargin(2)

        self.grid_10.addWidget(self.c_24, 3, 2, 1, 1)

        self.c_25 = QLabel(self.scrollAreaWidgetContents)
        self.c_25.setObjectName(u"c_25")
        sizePolicy3.setHeightForWidth(self.c_25.sizePolicy().hasHeightForWidth())
        self.c_25.setSizePolicy(sizePolicy3)
        self.c_25.setMaximumSize(QSize(16777215, 30))
        self.c_25.setFont(font2)
        self.c_25.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_25.setAlignment(Qt.AlignCenter)
        self.c_25.setMargin(2)

        self.grid_10.addWidget(self.c_25, 4, 2, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.grid_10.addWidget(self.label_10, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_10, 4, 1, 1, 1)

        self.grid_6 = QGridLayout()
        self.grid_6.setSpacing(5)
        self.grid_6.setObjectName(u"grid_6")
        self.a_7 = QPushButton(self.scrollAreaWidgetContents)
        self.a_7.setObjectName(u"a_7")
        sizePolicy2.setHeightForWidth(self.a_7.sizePolicy().hasHeightForWidth())
        self.a_7.setSizePolicy(sizePolicy2)
        self.a_7.setMaximumSize(QSize(40, 30))
        self.a_7.setFont(font2)
        self.a_7.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_6.addWidget(self.a_7, 2, 1, 1, 1)

        self.p_6 = QPushButton(self.scrollAreaWidgetContents)
        self.p_6.setObjectName(u"p_6")
        sizePolicy1.setHeightForWidth(self.p_6.sizePolicy().hasHeightForWidth())
        self.p_6.setSizePolicy(sizePolicy1)
        self.p_6.setMaximumSize(QSize(16777215, 30))
        self.p_6.setFont(font1)
        self.p_6.setCursor(QCursor(Qt.ArrowCursor))
        self.p_6.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_6.addWidget(self.p_6, 1, 0, 1, 1)

        self.b_7 = QPushButton(self.scrollAreaWidgetContents)
        self.b_7.setObjectName(u"b_7")
        sizePolicy1.setHeightForWidth(self.b_7.sizePolicy().hasHeightForWidth())
        self.b_7.setSizePolicy(sizePolicy1)
        self.b_7.setMaximumSize(QSize(30, 30))
        self.b_7.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_7.setIcon(icon)

        self.grid_6.addWidget(self.b_7, 2, 3, 1, 1)

        self.p_9 = QPushButton(self.scrollAreaWidgetContents)
        self.p_9.setObjectName(u"p_9")
        sizePolicy1.setHeightForWidth(self.p_9.sizePolicy().hasHeightForWidth())
        self.p_9.setSizePolicy(sizePolicy1)
        self.p_9.setMaximumSize(QSize(16777215, 30))
        self.p_9.setFont(font1)
        self.p_9.setCursor(QCursor(Qt.ArrowCursor))
        self.p_9.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_6.addWidget(self.p_9, 4, 0, 1, 1)

        self.b_9 = QPushButton(self.scrollAreaWidgetContents)
        self.b_9.setObjectName(u"b_9")
        sizePolicy1.setHeightForWidth(self.b_9.sizePolicy().hasHeightForWidth())
        self.b_9.setSizePolicy(sizePolicy1)
        self.b_9.setMaximumSize(QSize(30, 30))
        self.b_9.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_9.setIcon(icon)

        self.grid_6.addWidget(self.b_9, 4, 3, 1, 1)

        self.b_8 = QPushButton(self.scrollAreaWidgetContents)
        self.b_8.setObjectName(u"b_8")
        sizePolicy1.setHeightForWidth(self.b_8.sizePolicy().hasHeightForWidth())
        self.b_8.setSizePolicy(sizePolicy1)
        self.b_8.setMaximumSize(QSize(30, 30))
        self.b_8.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_8.setIcon(icon)

        self.grid_6.addWidget(self.b_8, 3, 3, 1, 1)

        self.a_8 = QPushButton(self.scrollAreaWidgetContents)
        self.a_8.setObjectName(u"a_8")
        sizePolicy2.setHeightForWidth(self.a_8.sizePolicy().hasHeightForWidth())
        self.a_8.setSizePolicy(sizePolicy2)
        self.a_8.setMaximumSize(QSize(40, 30))
        self.a_8.setFont(font2)
        self.a_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_6.addWidget(self.a_8, 3, 1, 1, 1)

        self.a_6 = QPushButton(self.scrollAreaWidgetContents)
        self.a_6.setObjectName(u"a_6")
        sizePolicy2.setHeightForWidth(self.a_6.sizePolicy().hasHeightForWidth())
        self.a_6.setSizePolicy(sizePolicy2)
        self.a_6.setMaximumSize(QSize(40, 30))
        self.a_6.setFont(font2)
        self.a_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_6.addWidget(self.a_6, 1, 1, 1, 1)

        self.b_6 = QPushButton(self.scrollAreaWidgetContents)
        self.b_6.setObjectName(u"b_6")
        sizePolicy1.setHeightForWidth(self.b_6.sizePolicy().hasHeightForWidth())
        self.b_6.setSizePolicy(sizePolicy1)
        self.b_6.setMaximumSize(QSize(30, 30))
        self.b_6.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_6.setIcon(icon)

        self.grid_6.addWidget(self.b_6, 1, 3, 1, 1)

        self.p_8 = QPushButton(self.scrollAreaWidgetContents)
        self.p_8.setObjectName(u"p_8")
        sizePolicy1.setHeightForWidth(self.p_8.sizePolicy().hasHeightForWidth())
        self.p_8.setSizePolicy(sizePolicy1)
        self.p_8.setMaximumSize(QSize(16777215, 30))
        self.p_8.setFont(font1)
        self.p_8.setCursor(QCursor(Qt.ArrowCursor))
        self.p_8.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_6.addWidget(self.p_8, 3, 0, 1, 1)

        self.p_7 = QPushButton(self.scrollAreaWidgetContents)
        self.p_7.setObjectName(u"p_7")
        sizePolicy1.setHeightForWidth(self.p_7.sizePolicy().hasHeightForWidth())
        self.p_7.setSizePolicy(sizePolicy1)
        self.p_7.setMaximumSize(QSize(16777215, 30))
        self.p_7.setFont(font1)
        self.p_7.setCursor(QCursor(Qt.ArrowCursor))
        self.p_7.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_6.addWidget(self.p_7, 2, 0, 1, 1)

        self.a_9 = QPushButton(self.scrollAreaWidgetContents)
        self.a_9.setObjectName(u"a_9")
        sizePolicy2.setHeightForWidth(self.a_9.sizePolicy().hasHeightForWidth())
        self.a_9.setSizePolicy(sizePolicy2)
        self.a_9.setMaximumSize(QSize(40, 30))
        self.a_9.setFont(font2)
        self.a_9.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_6.addWidget(self.a_9, 4, 1, 1, 1)

        self.c_6 = QLabel(self.scrollAreaWidgetContents)
        self.c_6.setObjectName(u"c_6")
        sizePolicy3.setHeightForWidth(self.c_6.sizePolicy().hasHeightForWidth())
        self.c_6.setSizePolicy(sizePolicy3)
        self.c_6.setMaximumSize(QSize(16777215, 30))
        self.c_6.setFont(font2)
        self.c_6.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_6.setAlignment(Qt.AlignCenter)
        self.c_6.setMargin(2)

        self.grid_6.addWidget(self.c_6, 1, 2, 1, 1)

        self.c_7 = QLabel(self.scrollAreaWidgetContents)
        self.c_7.setObjectName(u"c_7")
        sizePolicy3.setHeightForWidth(self.c_7.sizePolicy().hasHeightForWidth())
        self.c_7.setSizePolicy(sizePolicy3)
        self.c_7.setMaximumSize(QSize(16777215, 30))
        self.c_7.setFont(font2)
        self.c_7.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_7.setAlignment(Qt.AlignCenter)
        self.c_7.setMargin(2)

        self.grid_6.addWidget(self.c_7, 2, 2, 1, 1)

        self.c_8 = QLabel(self.scrollAreaWidgetContents)
        self.c_8.setObjectName(u"c_8")
        sizePolicy3.setHeightForWidth(self.c_8.sizePolicy().hasHeightForWidth())
        self.c_8.setSizePolicy(sizePolicy3)
        self.c_8.setMaximumSize(QSize(16777215, 30))
        self.c_8.setFont(font2)
        self.c_8.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_8.setAlignment(Qt.AlignCenter)
        self.c_8.setMargin(2)

        self.grid_6.addWidget(self.c_8, 3, 2, 1, 1)

        self.c_9 = QLabel(self.scrollAreaWidgetContents)
        self.c_9.setObjectName(u"c_9")
        sizePolicy3.setHeightForWidth(self.c_9.sizePolicy().hasHeightForWidth())
        self.c_9.setSizePolicy(sizePolicy3)
        self.c_9.setMaximumSize(QSize(16777215, 30))
        self.c_9.setFont(font2)
        self.c_9.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_9.setAlignment(Qt.AlignCenter)
        self.c_9.setMargin(2)

        self.grid_6.addWidget(self.c_9, 4, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.grid_6.addWidget(self.label_6, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_6, 0, 1, 1, 1)

        self.grid_5 = QGridLayout()
        self.grid_5.setSpacing(5)
        self.grid_5.setObjectName(u"grid_5")
        self.b_5 = QPushButton(self.scrollAreaWidgetContents)
        self.b_5.setObjectName(u"b_5")
        sizePolicy1.setHeightForWidth(self.b_5.sizePolicy().hasHeightForWidth())
        self.b_5.setSizePolicy(sizePolicy1)
        self.b_5.setMaximumSize(QSize(30, 30))
        self.b_5.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_5.setIcon(icon)

        self.grid_5.addWidget(self.b_5, 1, 3, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.grid_5.addWidget(self.label_4, 0, 0, 1, 4)

        self.p_5 = QPushButton(self.scrollAreaWidgetContents)
        self.p_5.setObjectName(u"p_5")
        sizePolicy1.setHeightForWidth(self.p_5.sizePolicy().hasHeightForWidth())
        self.p_5.setSizePolicy(sizePolicy1)
        self.p_5.setMaximumSize(QSize(16777215, 30))
        self.p_5.setFont(font1)
        self.p_5.setCursor(QCursor(Qt.ArrowCursor))
        self.p_5.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_5.addWidget(self.p_5, 1, 0, 1, 1)

        self.a_5 = QPushButton(self.scrollAreaWidgetContents)
        self.a_5.setObjectName(u"a_5")
        sizePolicy2.setHeightForWidth(self.a_5.sizePolicy().hasHeightForWidth())
        self.a_5.setSizePolicy(sizePolicy2)
        self.a_5.setMaximumSize(QSize(40, 30))
        self.a_5.setFont(font2)
        self.a_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_5.addWidget(self.a_5, 1, 1, 1, 1)

        self.c_5 = QLabel(self.scrollAreaWidgetContents)
        self.c_5.setObjectName(u"c_5")
        sizePolicy3.setHeightForWidth(self.c_5.sizePolicy().hasHeightForWidth())
        self.c_5.setSizePolicy(sizePolicy3)
        self.c_5.setMaximumSize(QSize(16777215, 30))
        self.c_5.setFont(font2)
        self.c_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_5.setAlignment(Qt.AlignCenter)
        self.c_5.setMargin(2)

        self.grid_5.addWidget(self.c_5, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.grid_5, 4, 0, 1, 1)

        self.grid_4 = QGridLayout()
        self.grid_4.setSpacing(5)
        self.grid_4.setObjectName(u"grid_4")
        self.a_4 = QPushButton(self.scrollAreaWidgetContents)
        self.a_4.setObjectName(u"a_4")
        sizePolicy2.setHeightForWidth(self.a_4.sizePolicy().hasHeightForWidth())
        self.a_4.setSizePolicy(sizePolicy2)
        self.a_4.setMaximumSize(QSize(40, 30))
        self.a_4.setFont(font2)
        self.a_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_4.addWidget(self.a_4, 1, 1, 1, 1)

        self.p_4 = QPushButton(self.scrollAreaWidgetContents)
        self.p_4.setObjectName(u"p_4")
        sizePolicy1.setHeightForWidth(self.p_4.sizePolicy().hasHeightForWidth())
        self.p_4.setSizePolicy(sizePolicy1)
        self.p_4.setMaximumSize(QSize(16777215, 30))
        self.p_4.setFont(font1)
        self.p_4.setCursor(QCursor(Qt.ArrowCursor))
        self.p_4.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_4.addWidget(self.p_4, 1, 0, 1, 1)

        self.b_4 = QPushButton(self.scrollAreaWidgetContents)
        self.b_4.setObjectName(u"b_4")
        sizePolicy1.setHeightForWidth(self.b_4.sizePolicy().hasHeightForWidth())
        self.b_4.setSizePolicy(sizePolicy1)
        self.b_4.setMaximumSize(QSize(30, 30))
        self.b_4.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_4.setIcon(icon)

        self.grid_4.addWidget(self.b_4, 1, 3, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.grid_4.addWidget(self.label_5, 0, 0, 1, 4)

        self.c_4 = QLabel(self.scrollAreaWidgetContents)
        self.c_4.setObjectName(u"c_4")
        sizePolicy3.setHeightForWidth(self.c_4.sizePolicy().hasHeightForWidth())
        self.c_4.setSizePolicy(sizePolicy3)
        self.c_4.setMaximumSize(QSize(16777215, 30))
        self.c_4.setFont(font2)
        self.c_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_4.setAlignment(Qt.AlignCenter)
        self.c_4.setMargin(2)

        self.grid_4.addWidget(self.c_4, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.grid_4, 3, 0, 1, 1)

        self.grid_7 = QGridLayout()
        self.grid_7.setSpacing(5)
        self.grid_7.setObjectName(u"grid_7")
        self.p_12 = QPushButton(self.scrollAreaWidgetContents)
        self.p_12.setObjectName(u"p_12")
        sizePolicy1.setHeightForWidth(self.p_12.sizePolicy().hasHeightForWidth())
        self.p_12.setSizePolicy(sizePolicy1)
        self.p_12.setMaximumSize(QSize(16777215, 30))
        self.p_12.setFont(font1)
        self.p_12.setCursor(QCursor(Qt.ArrowCursor))
        self.p_12.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_7.addWidget(self.p_12, 3, 0, 1, 1)

        self.a_13 = QPushButton(self.scrollAreaWidgetContents)
        self.a_13.setObjectName(u"a_13")
        sizePolicy2.setHeightForWidth(self.a_13.sizePolicy().hasHeightForWidth())
        self.a_13.setSizePolicy(sizePolicy2)
        self.a_13.setMaximumSize(QSize(40, 30))
        self.a_13.setFont(font2)
        self.a_13.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_7.addWidget(self.a_13, 4, 1, 1, 1)

        self.a_11 = QPushButton(self.scrollAreaWidgetContents)
        self.a_11.setObjectName(u"a_11")
        sizePolicy2.setHeightForWidth(self.a_11.sizePolicy().hasHeightForWidth())
        self.a_11.setSizePolicy(sizePolicy2)
        self.a_11.setMaximumSize(QSize(40, 30))
        self.a_11.setFont(font2)
        self.a_11.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_7.addWidget(self.a_11, 2, 1, 1, 1)

        self.p_11 = QPushButton(self.scrollAreaWidgetContents)
        self.p_11.setObjectName(u"p_11")
        sizePolicy1.setHeightForWidth(self.p_11.sizePolicy().hasHeightForWidth())
        self.p_11.setSizePolicy(sizePolicy1)
        self.p_11.setMaximumSize(QSize(16777215, 30))
        self.p_11.setFont(font1)
        self.p_11.setCursor(QCursor(Qt.ArrowCursor))
        self.p_11.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_7.addWidget(self.p_11, 2, 0, 1, 1)

        self.p_10 = QPushButton(self.scrollAreaWidgetContents)
        self.p_10.setObjectName(u"p_10")
        sizePolicy1.setHeightForWidth(self.p_10.sizePolicy().hasHeightForWidth())
        self.p_10.setSizePolicy(sizePolicy1)
        self.p_10.setMaximumSize(QSize(16777215, 30))
        self.p_10.setFont(font1)
        self.p_10.setCursor(QCursor(Qt.ArrowCursor))
        self.p_10.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_7.addWidget(self.p_10, 1, 0, 1, 1)

        self.b_12 = QPushButton(self.scrollAreaWidgetContents)
        self.b_12.setObjectName(u"b_12")
        sizePolicy1.setHeightForWidth(self.b_12.sizePolicy().hasHeightForWidth())
        self.b_12.setSizePolicy(sizePolicy1)
        self.b_12.setMaximumSize(QSize(30, 30))
        self.b_12.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_12.setIcon(icon)

        self.grid_7.addWidget(self.b_12, 3, 3, 1, 1)

        self.b_13 = QPushButton(self.scrollAreaWidgetContents)
        self.b_13.setObjectName(u"b_13")
        sizePolicy1.setHeightForWidth(self.b_13.sizePolicy().hasHeightForWidth())
        self.b_13.setSizePolicy(sizePolicy1)
        self.b_13.setMaximumSize(QSize(30, 30))
        self.b_13.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_13.setIcon(icon)

        self.grid_7.addWidget(self.b_13, 4, 3, 1, 1)

        self.b_10 = QPushButton(self.scrollAreaWidgetContents)
        self.b_10.setObjectName(u"b_10")
        sizePolicy1.setHeightForWidth(self.b_10.sizePolicy().hasHeightForWidth())
        self.b_10.setSizePolicy(sizePolicy1)
        self.b_10.setMaximumSize(QSize(30, 30))
        self.b_10.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_10.setIcon(icon)

        self.grid_7.addWidget(self.b_10, 1, 3, 1, 1)

        self.p_13 = QPushButton(self.scrollAreaWidgetContents)
        self.p_13.setObjectName(u"p_13")
        sizePolicy1.setHeightForWidth(self.p_13.sizePolicy().hasHeightForWidth())
        self.p_13.setSizePolicy(sizePolicy1)
        self.p_13.setMaximumSize(QSize(16777215, 30))
        self.p_13.setFont(font1)
        self.p_13.setCursor(QCursor(Qt.ArrowCursor))
        self.p_13.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_7.addWidget(self.p_13, 4, 0, 1, 1)

        self.a_10 = QPushButton(self.scrollAreaWidgetContents)
        self.a_10.setObjectName(u"a_10")
        sizePolicy2.setHeightForWidth(self.a_10.sizePolicy().hasHeightForWidth())
        self.a_10.setSizePolicy(sizePolicy2)
        self.a_10.setMaximumSize(QSize(40, 30))
        self.a_10.setFont(font2)
        self.a_10.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_7.addWidget(self.a_10, 1, 1, 1, 1)

        self.b_11 = QPushButton(self.scrollAreaWidgetContents)
        self.b_11.setObjectName(u"b_11")
        sizePolicy1.setHeightForWidth(self.b_11.sizePolicy().hasHeightForWidth())
        self.b_11.setSizePolicy(sizePolicy1)
        self.b_11.setMaximumSize(QSize(30, 30))
        self.b_11.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_11.setIcon(icon)

        self.grid_7.addWidget(self.b_11, 2, 3, 1, 1)

        self.a_12 = QPushButton(self.scrollAreaWidgetContents)
        self.a_12.setObjectName(u"a_12")
        sizePolicy2.setHeightForWidth(self.a_12.sizePolicy().hasHeightForWidth())
        self.a_12.setSizePolicy(sizePolicy2)
        self.a_12.setMaximumSize(QSize(40, 30))
        self.a_12.setFont(font2)
        self.a_12.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_7.addWidget(self.a_12, 3, 1, 1, 1)

        self.c_10 = QLabel(self.scrollAreaWidgetContents)
        self.c_10.setObjectName(u"c_10")
        sizePolicy3.setHeightForWidth(self.c_10.sizePolicy().hasHeightForWidth())
        self.c_10.setSizePolicy(sizePolicy3)
        self.c_10.setMaximumSize(QSize(16777215, 30))
        self.c_10.setFont(font2)
        self.c_10.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_10.setAlignment(Qt.AlignCenter)
        self.c_10.setMargin(2)

        self.grid_7.addWidget(self.c_10, 1, 2, 1, 1)

        self.c_11 = QLabel(self.scrollAreaWidgetContents)
        self.c_11.setObjectName(u"c_11")
        sizePolicy3.setHeightForWidth(self.c_11.sizePolicy().hasHeightForWidth())
        self.c_11.setSizePolicy(sizePolicy3)
        self.c_11.setMaximumSize(QSize(16777215, 30))
        self.c_11.setFont(font2)
        self.c_11.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_11.setAlignment(Qt.AlignCenter)
        self.c_11.setMargin(2)

        self.grid_7.addWidget(self.c_11, 2, 2, 1, 1)

        self.c_12 = QLabel(self.scrollAreaWidgetContents)
        self.c_12.setObjectName(u"c_12")
        sizePolicy3.setHeightForWidth(self.c_12.sizePolicy().hasHeightForWidth())
        self.c_12.setSizePolicy(sizePolicy3)
        self.c_12.setMaximumSize(QSize(16777215, 30))
        self.c_12.setFont(font2)
        self.c_12.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_12.setAlignment(Qt.AlignCenter)
        self.c_12.setMargin(2)

        self.grid_7.addWidget(self.c_12, 3, 2, 1, 1)

        self.c_13 = QLabel(self.scrollAreaWidgetContents)
        self.c_13.setObjectName(u"c_13")
        sizePolicy3.setHeightForWidth(self.c_13.sizePolicy().hasHeightForWidth())
        self.c_13.setSizePolicy(sizePolicy3)
        self.c_13.setMaximumSize(QSize(16777215, 30))
        self.c_13.setFont(font2)
        self.c_13.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_13.setAlignment(Qt.AlignCenter)
        self.c_13.setMargin(2)

        self.grid_7.addWidget(self.c_13, 4, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.grid_7.addWidget(self.label_7, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_7, 1, 1, 1, 1)

        self.grid_8 = QGridLayout()
        self.grid_8.setSpacing(5)
        self.grid_8.setObjectName(u"grid_8")
        self.p_17 = QPushButton(self.scrollAreaWidgetContents)
        self.p_17.setObjectName(u"p_17")
        sizePolicy1.setHeightForWidth(self.p_17.sizePolicy().hasHeightForWidth())
        self.p_17.setSizePolicy(sizePolicy1)
        self.p_17.setMaximumSize(QSize(16777215, 30))
        self.p_17.setFont(font1)
        self.p_17.setCursor(QCursor(Qt.ArrowCursor))
        self.p_17.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_8.addWidget(self.p_17, 4, 0, 1, 1)

        self.a_15 = QPushButton(self.scrollAreaWidgetContents)
        self.a_15.setObjectName(u"a_15")
        sizePolicy2.setHeightForWidth(self.a_15.sizePolicy().hasHeightForWidth())
        self.a_15.setSizePolicy(sizePolicy2)
        self.a_15.setMaximumSize(QSize(40, 30))
        self.a_15.setFont(font2)
        self.a_15.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_8.addWidget(self.a_15, 2, 1, 1, 1)

        self.p_16 = QPushButton(self.scrollAreaWidgetContents)
        self.p_16.setObjectName(u"p_16")
        sizePolicy1.setHeightForWidth(self.p_16.sizePolicy().hasHeightForWidth())
        self.p_16.setSizePolicy(sizePolicy1)
        self.p_16.setMaximumSize(QSize(16777215, 30))
        self.p_16.setFont(font1)
        self.p_16.setCursor(QCursor(Qt.ArrowCursor))
        self.p_16.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_8.addWidget(self.p_16, 3, 0, 1, 1)

        self.a_16 = QPushButton(self.scrollAreaWidgetContents)
        self.a_16.setObjectName(u"a_16")
        sizePolicy2.setHeightForWidth(self.a_16.sizePolicy().hasHeightForWidth())
        self.a_16.setSizePolicy(sizePolicy2)
        self.a_16.setMaximumSize(QSize(40, 30))
        self.a_16.setFont(font2)
        self.a_16.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_8.addWidget(self.a_16, 3, 1, 1, 1)

        self.a_14 = QPushButton(self.scrollAreaWidgetContents)
        self.a_14.setObjectName(u"a_14")
        sizePolicy2.setHeightForWidth(self.a_14.sizePolicy().hasHeightForWidth())
        self.a_14.setSizePolicy(sizePolicy2)
        self.a_14.setMaximumSize(QSize(40, 30))
        self.a_14.setFont(font2)
        self.a_14.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}\n"
"")

        self.grid_8.addWidget(self.a_14, 1, 1, 1, 1)

        self.b_15 = QPushButton(self.scrollAreaWidgetContents)
        self.b_15.setObjectName(u"b_15")
        sizePolicy1.setHeightForWidth(self.b_15.sizePolicy().hasHeightForWidth())
        self.b_15.setSizePolicy(sizePolicy1)
        self.b_15.setMaximumSize(QSize(30, 30))
        self.b_15.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_15.setIcon(icon)

        self.grid_8.addWidget(self.b_15, 2, 3, 1, 1)

        self.b_14 = QPushButton(self.scrollAreaWidgetContents)
        self.b_14.setObjectName(u"b_14")
        sizePolicy1.setHeightForWidth(self.b_14.sizePolicy().hasHeightForWidth())
        self.b_14.setSizePolicy(sizePolicy1)
        self.b_14.setMaximumSize(QSize(30, 30))
        self.b_14.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_14.setIcon(icon)

        self.grid_8.addWidget(self.b_14, 1, 3, 1, 1)

        self.b_16 = QPushButton(self.scrollAreaWidgetContents)
        self.b_16.setObjectName(u"b_16")
        sizePolicy1.setHeightForWidth(self.b_16.sizePolicy().hasHeightForWidth())
        self.b_16.setSizePolicy(sizePolicy1)
        self.b_16.setMaximumSize(QSize(30, 30))
        self.b_16.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_16.setIcon(icon)

        self.grid_8.addWidget(self.b_16, 3, 3, 1, 1)

        self.a_17 = QPushButton(self.scrollAreaWidgetContents)
        self.a_17.setObjectName(u"a_17")
        sizePolicy2.setHeightForWidth(self.a_17.sizePolicy().hasHeightForWidth())
        self.a_17.setSizePolicy(sizePolicy2)
        self.a_17.setMaximumSize(QSize(40, 30))
        self.a_17.setFont(font2)
        self.a_17.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_8.addWidget(self.a_17, 4, 1, 1, 1)

        self.p_15 = QPushButton(self.scrollAreaWidgetContents)
        self.p_15.setObjectName(u"p_15")
        sizePolicy1.setHeightForWidth(self.p_15.sizePolicy().hasHeightForWidth())
        self.p_15.setSizePolicy(sizePolicy1)
        self.p_15.setMaximumSize(QSize(16777215, 30))
        self.p_15.setFont(font1)
        self.p_15.setCursor(QCursor(Qt.ArrowCursor))
        self.p_15.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_8.addWidget(self.p_15, 2, 0, 1, 1)

        self.b_17 = QPushButton(self.scrollAreaWidgetContents)
        self.b_17.setObjectName(u"b_17")
        sizePolicy1.setHeightForWidth(self.b_17.sizePolicy().hasHeightForWidth())
        self.b_17.setSizePolicy(sizePolicy1)
        self.b_17.setMaximumSize(QSize(30, 30))
        self.b_17.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_17.setIcon(icon)

        self.grid_8.addWidget(self.b_17, 4, 3, 1, 1)

        self.p_14 = QPushButton(self.scrollAreaWidgetContents)
        self.p_14.setObjectName(u"p_14")
        sizePolicy1.setHeightForWidth(self.p_14.sizePolicy().hasHeightForWidth())
        self.p_14.setSizePolicy(sizePolicy1)
        self.p_14.setMaximumSize(QSize(16777215, 30))
        self.p_14.setFont(font1)
        self.p_14.setCursor(QCursor(Qt.ArrowCursor))
        self.p_14.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_8.addWidget(self.p_14, 1, 0, 1, 1)

        self.c_14 = QLabel(self.scrollAreaWidgetContents)
        self.c_14.setObjectName(u"c_14")
        sizePolicy3.setHeightForWidth(self.c_14.sizePolicy().hasHeightForWidth())
        self.c_14.setSizePolicy(sizePolicy3)
        self.c_14.setMaximumSize(QSize(16777215, 30))
        self.c_14.setFont(font2)
        self.c_14.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_14.setAlignment(Qt.AlignCenter)
        self.c_14.setMargin(2)

        self.grid_8.addWidget(self.c_14, 1, 2, 1, 1)

        self.c_15 = QLabel(self.scrollAreaWidgetContents)
        self.c_15.setObjectName(u"c_15")
        sizePolicy3.setHeightForWidth(self.c_15.sizePolicy().hasHeightForWidth())
        self.c_15.setSizePolicy(sizePolicy3)
        self.c_15.setMaximumSize(QSize(16777215, 30))
        self.c_15.setFont(font2)
        self.c_15.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_15.setAlignment(Qt.AlignCenter)
        self.c_15.setMargin(2)

        self.grid_8.addWidget(self.c_15, 2, 2, 1, 1)

        self.c_16 = QLabel(self.scrollAreaWidgetContents)
        self.c_16.setObjectName(u"c_16")
        sizePolicy3.setHeightForWidth(self.c_16.sizePolicy().hasHeightForWidth())
        self.c_16.setSizePolicy(sizePolicy3)
        self.c_16.setMaximumSize(QSize(16777215, 30))
        self.c_16.setFont(font2)
        self.c_16.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_16.setAlignment(Qt.AlignCenter)
        self.c_16.setMargin(2)

        self.grid_8.addWidget(self.c_16, 3, 2, 1, 1)

        self.c_17 = QLabel(self.scrollAreaWidgetContents)
        self.c_17.setObjectName(u"c_17")
        sizePolicy3.setHeightForWidth(self.c_17.sizePolicy().hasHeightForWidth())
        self.c_17.setSizePolicy(sizePolicy3)
        self.c_17.setMaximumSize(QSize(16777215, 30))
        self.c_17.setFont(font2)
        self.c_17.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_17.setAlignment(Qt.AlignCenter)
        self.c_17.setMargin(2)

        self.grid_8.addWidget(self.c_17, 4, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.grid_8.addWidget(self.label_8, 0, 0, 1, 4)


        self.gridLayout_5.addLayout(self.grid_8, 2, 1, 1, 1)

        self.grid_3 = QGridLayout()
        self.grid_3.setSpacing(5)
        self.grid_3.setObjectName(u"grid_3")
        self.b_3 = QPushButton(self.scrollAreaWidgetContents)
        self.b_3.setObjectName(u"b_3")
        sizePolicy1.setHeightForWidth(self.b_3.sizePolicy().hasHeightForWidth())
        self.b_3.setSizePolicy(sizePolicy1)
        self.b_3.setMaximumSize(QSize(30, 30))
        self.b_3.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.b_3.setIcon(icon)

        self.grid_3.addWidget(self.b_3, 1, 3, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.grid_3.addWidget(self.label_3, 0, 0, 1, 4)

        self.a_3 = QPushButton(self.scrollAreaWidgetContents)
        self.a_3.setObjectName(u"a_3")
        sizePolicy2.setHeightForWidth(self.a_3.sizePolicy().hasHeightForWidth())
        self.a_3.setSizePolicy(sizePolicy2)
        self.a_3.setMaximumSize(QSize(40, 30))
        self.a_3.setFont(font2)
        self.a_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(201, 22, 26);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(255, 100, 50);\n"
"}")

        self.grid_3.addWidget(self.a_3, 1, 1, 1, 1)

        self.p_3 = QPushButton(self.scrollAreaWidgetContents)
        self.p_3.setObjectName(u"p_3")
        sizePolicy1.setHeightForWidth(self.p_3.sizePolicy().hasHeightForWidth())
        self.p_3.setSizePolicy(sizePolicy1)
        self.p_3.setMaximumSize(QSize(16777215, 30))
        self.p_3.setFont(font1)
        self.p_3.setCursor(QCursor(Qt.ArrowCursor))
        self.p_3.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  rgb(83, 83, 83);\n"
"	border: 1px solid rgb(110, 111, 112);\n"
"}")

        self.grid_3.addWidget(self.p_3, 1, 0, 1, 1)

        self.c_3 = QLabel(self.scrollAreaWidgetContents)
        self.c_3.setObjectName(u"c_3")
        sizePolicy3.setHeightForWidth(self.c_3.sizePolicy().hasHeightForWidth())
        self.c_3.setSizePolicy(sizePolicy3)
        self.c_3.setMaximumSize(QSize(16777215, 30))
        self.c_3.setFont(font2)
        self.c_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"")
        self.c_3.setAlignment(Qt.AlignCenter)
        self.c_3.setMargin(2)

        self.grid_3.addWidget(self.c_3, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.grid_3, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.pageMap)
        self.pageTreatment = QWidget()
        self.pageTreatment.setObjectName(u"pageTreatment")
        self.pageTreatment.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        self.verticalLayout_3 = QVBoxLayout(self.pageTreatment)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameTreatment = QFrame(self.pageTreatment)
        self.frameTreatment.setObjectName(u"frameTreatment")
        font4 = QFont()
        self.frameTreatment.setFont(font4)
        self.frameTreatment.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/logo/images/logo.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.frameTreatment.setFrameShape(QFrame.StyledPanel)
        self.frameTreatment.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frameTreatment)
        self.gridLayout_18.setSpacing(5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(10, 10, 10, 10)
        self.firstLineProfession = QLineEdit(self.frameTreatment)
        self.firstLineProfession.setObjectName(u"firstLineProfession")
        sizePolicy1.setHeightForWidth(self.firstLineProfession.sizePolicy().hasHeightForWidth())
        self.firstLineProfession.setSizePolicy(sizePolicy1)
        self.firstLineProfession.setMaximumSize(QSize(16777215, 30))
        self.firstLineProfession.setFont(font2)
        self.firstLineProfession.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineProfession, 0, 8, 1, 1)

        self.firstLineAge = QLineEdit(self.frameTreatment)
        self.firstLineAge.setObjectName(u"firstLineAge")
        sizePolicy1.setHeightForWidth(self.firstLineAge.sizePolicy().hasHeightForWidth())
        self.firstLineAge.setSizePolicy(sizePolicy1)
        self.firstLineAge.setMaximumSize(QSize(16777215, 30))
        self.firstLineAge.setFont(font2)
        self.firstLineAge.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineAge, 0, 4, 1, 1)

        self.firstBoxDoctor = QComboBox(self.frameTreatment)
        self.firstBoxDoctor.setObjectName(u"firstBoxDoctor")
        sizePolicy1.setHeightForWidth(self.firstBoxDoctor.sizePolicy().hasHeightForWidth())
        self.firstBoxDoctor.setSizePolicy(sizePolicy1)
        self.firstBoxDoctor.setMaximumSize(QSize(16777215, 30))
        self.firstBoxDoctor.setFont(font2)
        self.firstBoxDoctor.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxDoctor, 4, 7, 1, 2)

        self.firstLineUf = QLineEdit(self.frameTreatment)
        self.firstLineUf.setObjectName(u"firstLineUf")
        sizePolicy1.setHeightForWidth(self.firstLineUf.sizePolicy().hasHeightForWidth())
        self.firstLineUf.setSizePolicy(sizePolicy1)
        self.firstLineUf.setMaximumSize(QSize(50, 30))
        self.firstLineUf.setFont(font2)
        self.firstLineUf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")
        self.firstLineUf.setMaxLength(2)

        self.gridLayout_18.addWidget(self.firstLineUf, 2, 5, 1, 1)

        self.firstLineTreatDate = QLineEdit(self.frameTreatment)
        self.firstLineTreatDate.setObjectName(u"firstLineTreatDate")
        sizePolicy1.setHeightForWidth(self.firstLineTreatDate.sizePolicy().hasHeightForWidth())
        self.firstLineTreatDate.setSizePolicy(sizePolicy1)
        self.firstLineTreatDate.setMaximumSize(QSize(16777215, 30))
        self.firstLineTreatDate.setFont(font2)
        self.firstLineTreatDate.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineTreatDate, 4, 0, 1, 1)

        self.firstLinePatientName = QLineEdit(self.frameTreatment)
        self.firstLinePatientName.setObjectName(u"firstLinePatientName")
        sizePolicy1.setHeightForWidth(self.firstLinePatientName.sizePolicy().hasHeightForWidth())
        self.firstLinePatientName.setSizePolicy(sizePolicy1)
        self.firstLinePatientName.setMaximumSize(QSize(16777215, 30))
        self.firstLinePatientName.setFont(font2)
        self.firstLinePatientName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLinePatientName, 0, 1, 1, 2)

        self.firstLineCpf = QLineEdit(self.frameTreatment)
        self.firstLineCpf.setObjectName(u"firstLineCpf")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(120)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.firstLineCpf.sizePolicy().hasHeightForWidth())
        self.firstLineCpf.setSizePolicy(sizePolicy5)
        self.firstLineCpf.setMaximumSize(QSize(16777215, 30))
        self.firstLineCpf.setFont(font2)
        self.firstLineCpf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineCpf, 0, 0, 1, 1)

        self.firstBoxClinic = QComboBox(self.frameTreatment)
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.addItem("")
        self.firstBoxClinic.setObjectName(u"firstBoxClinic")
        sizePolicy1.setHeightForWidth(self.firstBoxClinic.sizePolicy().hasHeightForWidth())
        self.firstBoxClinic.setSizePolicy(sizePolicy1)
        self.firstBoxClinic.setMaximumSize(QSize(16777215, 30))
        self.firstBoxClinic.setFont(font2)
        self.firstBoxClinic.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxClinic, 4, 2, 1, 1)

        self.firstLineCity = QLineEdit(self.frameTreatment)
        self.firstLineCity.setObjectName(u"firstLineCity")
        sizePolicy1.setHeightForWidth(self.firstLineCity.sizePolicy().hasHeightForWidth())
        self.firstLineCity.setSizePolicy(sizePolicy1)
        self.firstLineCity.setMaximumSize(QSize(16777215, 30))
        self.firstLineCity.setFont(font2)
        self.firstLineCity.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineCity, 2, 3, 1, 1)

        self.firstLineSusCard = QLineEdit(self.frameTreatment)
        self.firstLineSusCard.setObjectName(u"firstLineSusCard")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(120)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.firstLineSusCard.sizePolicy().hasHeightForWidth())
        self.firstLineSusCard.setSizePolicy(sizePolicy6)
        self.firstLineSusCard.setMaximumSize(QSize(16777215, 30))
        self.firstLineSusCard.setFont(font2)
        self.firstLineSusCard.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineSusCard, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frameTreatment)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(30, 30))
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_18.addWidget(self.frame_3, 3, 0, 1, 1)

        self.firstLineCep = QLineEdit(self.frameTreatment)
        self.firstLineCep.setObjectName(u"firstLineCep")
        sizePolicy1.setHeightForWidth(self.firstLineCep.sizePolicy().hasHeightForWidth())
        self.firstLineCep.setSizePolicy(sizePolicy1)
        self.firstLineCep.setMaximumSize(QSize(16777215, 30))
        self.firstLineCep.setFont(font2)
        self.firstLineCep.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineCep, 2, 4, 1, 1)

        self.firstLineBornDay = QLineEdit(self.frameTreatment)
        self.firstLineBornDay.setObjectName(u"firstLineBornDay")
        sizePolicy1.setHeightForWidth(self.firstLineBornDay.sizePolicy().hasHeightForWidth())
        self.firstLineBornDay.setSizePolicy(sizePolicy1)
        self.firstLineBornDay.setMaximumSize(QSize(16777215, 30))
        self.firstLineBornDay.setFont(font2)
        self.firstLineBornDay.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineBornDay, 0, 3, 1, 1)

        self.firstBoxAdmission = QComboBox(self.frameTreatment)
        self.firstBoxAdmission.setObjectName(u"firstBoxAdmission")
        sizePolicy1.setHeightForWidth(self.firstBoxAdmission.sizePolicy().hasHeightForWidth())
        self.firstBoxAdmission.setSizePolicy(sizePolicy1)
        self.firstBoxAdmission.setMaximumSize(QSize(16777215, 30))
        self.firstBoxAdmission.setFont(font2)
        self.firstBoxAdmission.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxAdmission, 4, 6, 1, 1)

        self.firstLineAdress = QLineEdit(self.frameTreatment)
        self.firstLineAdress.setObjectName(u"firstLineAdress")
        sizePolicy1.setHeightForWidth(self.firstLineAdress.sizePolicy().hasHeightForWidth())
        self.firstLineAdress.setSizePolicy(sizePolicy1)
        self.firstLineAdress.setMaximumSize(QSize(16777215, 30))
        self.firstLineAdress.setFont(font2)
        self.firstLineAdress.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineAdress, 2, 0, 1, 2)

        self.firstBtnClean = QPushButton(self.frameTreatment)
        self.firstBtnClean.setObjectName(u"firstBtnClean")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.firstBtnClean.sizePolicy().hasHeightForWidth())
        self.firstBtnClean.setSizePolicy(sizePolicy7)
        self.firstBtnClean.setMinimumSize(QSize(130, 30))
        self.firstBtnClean.setMaximumSize(QSize(130, 30))
        self.firstBtnClean.setFont(font2)
        self.firstBtnClean.setCursor(QCursor(Qt.PointingHandCursor))
        self.firstBtnClean.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBtnClean, 5, 7, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.firstLinePhoneTwo = QLineEdit(self.frameTreatment)
        self.firstLinePhoneTwo.setObjectName(u"firstLinePhoneTwo")
        sizePolicy1.setHeightForWidth(self.firstLinePhoneTwo.sizePolicy().hasHeightForWidth())
        self.firstLinePhoneTwo.setSizePolicy(sizePolicy1)
        self.firstLinePhoneTwo.setMaximumSize(QSize(16777215, 30))
        self.firstLinePhoneTwo.setFont(font2)
        self.firstLinePhoneTwo.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLinePhoneTwo, 1, 8, 1, 1)

        self.firstBoxBed = QComboBox(self.frameTreatment)
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.addItem("")
        self.firstBoxBed.setObjectName(u"firstBoxBed")
        sizePolicy3.setHeightForWidth(self.firstBoxBed.sizePolicy().hasHeightForWidth())
        self.firstBoxBed.setSizePolicy(sizePolicy3)
        self.firstBoxBed.setMaximumSize(QSize(16777215, 30))
        self.firstBoxBed.setFont(font2)
        self.firstBoxBed.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxBed, 4, 3, 1, 2)

        self.firstBoxDependency = QComboBox(self.frameTreatment)
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.addItem("")
        self.firstBoxDependency.setObjectName(u"firstBoxDependency")
        sizePolicy1.setHeightForWidth(self.firstBoxDependency.sizePolicy().hasHeightForWidth())
        self.firstBoxDependency.setSizePolicy(sizePolicy1)
        self.firstBoxDependency.setMaximumSize(QSize(16777215, 30))
        self.firstBoxDependency.setFont(font2)
        self.firstBoxDependency.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxDependency, 4, 5, 1, 1)

        self.firstLinePhoneOne = QLineEdit(self.frameTreatment)
        self.firstLinePhoneOne.setObjectName(u"firstLinePhoneOne")
        sizePolicy1.setHeightForWidth(self.firstLinePhoneOne.sizePolicy().hasHeightForWidth())
        self.firstLinePhoneOne.setSizePolicy(sizePolicy1)
        self.firstLinePhoneOne.setMaximumSize(QSize(16777215, 30))
        self.firstLinePhoneOne.setFont(font2)
        self.firstLinePhoneOne.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLinePhoneOne, 1, 7, 1, 1)

        self.firstLineFatherName = QLineEdit(self.frameTreatment)
        self.firstLineFatherName.setObjectName(u"firstLineFatherName")
        sizePolicy1.setHeightForWidth(self.firstLineFatherName.sizePolicy().hasHeightForWidth())
        self.firstLineFatherName.setSizePolicy(sizePolicy1)
        self.firstLineFatherName.setMaximumSize(QSize(16777215, 30))
        self.firstLineFatherName.setFont(font2)
        self.firstLineFatherName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineFatherName, 1, 2, 1, 3)

        self.firstLineRG = QLineEdit(self.frameTreatment)
        self.firstLineRG.setObjectName(u"firstLineRG")
        sizePolicy1.setHeightForWidth(self.firstLineRG.sizePolicy().hasHeightForWidth())
        self.firstLineRG.setSizePolicy(sizePolicy1)
        self.firstLineRG.setMaximumSize(QSize(16777215, 30))
        self.firstLineRG.setFont(font2)
        self.firstLineRG.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineRG, 1, 1, 1, 1)

        self.firstBtnConfirm = QPushButton(self.frameTreatment)
        self.firstBtnConfirm.setObjectName(u"firstBtnConfirm")
        sizePolicy7.setHeightForWidth(self.firstBtnConfirm.sizePolicy().hasHeightForWidth())
        self.firstBtnConfirm.setSizePolicy(sizePolicy7)
        self.firstBtnConfirm.setMinimumSize(QSize(130, 30))
        self.firstBtnConfirm.setMaximumSize(QSize(130, 30))
        self.firstBtnConfirm.setFont(font2)
        self.firstBtnConfirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.firstBtnConfirm.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBtnConfirm, 5, 8, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.firstLineDistrict = QLineEdit(self.frameTreatment)
        self.firstLineDistrict.setObjectName(u"firstLineDistrict")
        sizePolicy1.setHeightForWidth(self.firstLineDistrict.sizePolicy().hasHeightForWidth())
        self.firstLineDistrict.setSizePolicy(sizePolicy1)
        self.firstLineDistrict.setMaximumSize(QSize(16777215, 30))
        self.firstLineDistrict.setFont(font2)
        self.firstLineDistrict.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineDistrict, 2, 2, 1, 1)

        self.firstLineTreatHour = QLineEdit(self.frameTreatment)
        self.firstLineTreatHour.setObjectName(u"firstLineTreatHour")
        sizePolicy1.setHeightForWidth(self.firstLineTreatHour.sizePolicy().hasHeightForWidth())
        self.firstLineTreatHour.setSizePolicy(sizePolicy1)
        self.firstLineTreatHour.setMaximumSize(QSize(16777215, 30))
        self.firstLineTreatHour.setFont(font2)
        self.firstLineTreatHour.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineTreatHour, 4, 1, 1, 1)

        self.firstBtnRegister = QPushButton(self.frameTreatment)
        self.firstBtnRegister.setObjectName(u"firstBtnRegister")
        self.firstBtnRegister.setMinimumSize(QSize(130, 30))
        self.firstBtnRegister.setMaximumSize(QSize(130, 30))
        self.firstBtnRegister.setFont(font2)
        self.firstBtnRegister.setCursor(QCursor(Qt.PointingHandCursor))
        self.firstBtnRegister.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBtnRegister, 2, 8, 1, 1, Qt.AlignHCenter)

        self.firstBoxSkinColor = QComboBox(self.frameTreatment)
        self.firstBoxSkinColor.addItem("")
        self.firstBoxSkinColor.addItem("")
        self.firstBoxSkinColor.addItem("")
        self.firstBoxSkinColor.addItem("")
        self.firstBoxSkinColor.addItem("")
        self.firstBoxSkinColor.setObjectName(u"firstBoxSkinColor")
        sizePolicy1.setHeightForWidth(self.firstBoxSkinColor.sizePolicy().hasHeightForWidth())
        self.firstBoxSkinColor.setSizePolicy(sizePolicy1)
        self.firstBoxSkinColor.setMaximumSize(QSize(16777215, 30))
        self.firstBoxSkinColor.setFont(font2)
        self.firstBoxSkinColor.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxSkinColor, 0, 6, 1, 1)

        self.firstLineMotherName = QLineEdit(self.frameTreatment)
        self.firstLineMotherName.setObjectName(u"firstLineMotherName")
        sizePolicy1.setHeightForWidth(self.firstLineMotherName.sizePolicy().hasHeightForWidth())
        self.firstLineMotherName.setSizePolicy(sizePolicy1)
        self.firstLineMotherName.setMaximumSize(QSize(16777215, 30))
        self.firstLineMotherName.setFont(font2)
        self.firstLineMotherName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineMotherName, 1, 5, 1, 2)

        self.firstBoxUrbanZone = QComboBox(self.frameTreatment)
        self.firstBoxUrbanZone.addItem("")
        self.firstBoxUrbanZone.addItem("")
        self.firstBoxUrbanZone.setObjectName(u"firstBoxUrbanZone")
        sizePolicy1.setHeightForWidth(self.firstBoxUrbanZone.sizePolicy().hasHeightForWidth())
        self.firstBoxUrbanZone.setSizePolicy(sizePolicy1)
        self.firstBoxUrbanZone.setMaximumSize(QSize(16777215, 30))
        self.firstBoxUrbanZone.setFont(font2)
        self.firstBoxUrbanZone.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxUrbanZone, 2, 6, 1, 1)

        self.firstBoxSex = QComboBox(self.frameTreatment)
        self.firstBoxSex.addItem("")
        self.firstBoxSex.addItem("")
        self.firstBoxSex.setObjectName(u"firstBoxSex")
        sizePolicy1.setHeightForWidth(self.firstBoxSex.sizePolicy().hasHeightForWidth())
        self.firstBoxSex.setSizePolicy(sizePolicy1)
        self.firstBoxSex.setMaximumSize(QSize(16777215, 30))
        self.firstBoxSex.setFont(font2)
        self.firstBoxSex.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxSex, 0, 5, 1, 1)

        self.firstBoxCivilStats = QComboBox(self.frameTreatment)
        self.firstBoxCivilStats.addItem("")
        self.firstBoxCivilStats.addItem("")
        self.firstBoxCivilStats.addItem("")
        self.firstBoxCivilStats.addItem("")
        self.firstBoxCivilStats.setObjectName(u"firstBoxCivilStats")
        sizePolicy1.setHeightForWidth(self.firstBoxCivilStats.sizePolicy().hasHeightForWidth())
        self.firstBoxCivilStats.setSizePolicy(sizePolicy1)
        self.firstBoxCivilStats.setMaximumSize(QSize(16777215, 30))
        self.firstBoxCivilStats.setFont(font2)
        self.firstBoxCivilStats.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_18.addWidget(self.firstBoxCivilStats, 0, 7, 1, 1)

        self.firstLineResponsible = QLineEdit(self.frameTreatment)
        self.firstLineResponsible.setObjectName(u"firstLineResponsible")
        self.firstLineResponsible.setMaximumSize(QSize(16777215, 30))
        self.firstLineResponsible.setFont(font2)
        self.firstLineResponsible.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.firstLineResponsible, 5, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer, 6, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frameTreatment)

        self.stackedWidget.addWidget(self.pageTreatment)
        self.pageHistoric = QWidget()
        self.pageHistoric.setObjectName(u"pageHistoric")
        self.pageHistoric.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        self.verticalLayout_4 = QVBoxLayout(self.pageHistoric)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frameHistoric = QFrame(self.pageHistoric)
        self.frameHistoric.setObjectName(u"frameHistoric")
        self.frameHistoric.setFrameShape(QFrame.StyledPanel)
        self.frameHistoric.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frameHistoric)
        self.gridLayout_19.setSpacing(5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(10, 10, 10, 10)
        self.secondBtnClean = QPushButton(self.frameHistoric)
        self.secondBtnClean.setObjectName(u"secondBtnClean")
        self.secondBtnClean.setMinimumSize(QSize(130, 30))
        self.secondBtnClean.setMaximumSize(QSize(130, 30))
        self.secondBtnClean.setFont(font2)
        self.secondBtnClean.setCursor(QCursor(Qt.PointingHandCursor))
        self.secondBtnClean.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_19.addWidget(self.secondBtnClean, 1, 1, 1, 1, Qt.AlignRight)

        self.secondLineCpf = QLineEdit(self.frameHistoric)
        self.secondLineCpf.setObjectName(u"secondLineCpf")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.secondLineCpf.sizePolicy().hasHeightForWidth())
        self.secondLineCpf.setSizePolicy(sizePolicy8)
        self.secondLineCpf.setMaximumSize(QSize(16777215, 30))
        self.secondLineCpf.setFont(font2)
        self.secondLineCpf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.secondLineCpf, 0, 0, 1, 1)

        self.secondLinePatientName = QLineEdit(self.frameHistoric)
        self.secondLinePatientName.setObjectName(u"secondLinePatientName")
        self.secondLinePatientName.setMaximumSize(QSize(16777215, 30))
        self.secondLinePatientName.setFont(font2)
        self.secondLinePatientName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.secondLinePatientName, 0, 1, 1, 1)

        self.secondBtnConfirm = QPushButton(self.frameHistoric)
        self.secondBtnConfirm.setObjectName(u"secondBtnConfirm")
        self.secondBtnConfirm.setMinimumSize(QSize(130, 30))
        self.secondBtnConfirm.setMaximumSize(QSize(130, 30))
        self.secondBtnConfirm.setFont(font2)
        self.secondBtnConfirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.secondBtnConfirm.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_19.addWidget(self.secondBtnConfirm, 1, 2, 1, 1)

        self.secondLineMotherName = QLineEdit(self.frameHistoric)
        self.secondLineMotherName.setObjectName(u"secondLineMotherName")
        self.secondLineMotherName.setMaximumSize(QSize(16777215, 30))
        self.secondLineMotherName.setFont(font2)
        self.secondLineMotherName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.secondLineMotherName, 0, 2, 1, 1)

        self.secondTable = QTableWidget(self.frameHistoric)
        if (self.secondTable.columnCount() < 15):
            self.secondTable.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.secondTable.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.secondTable.setObjectName(u"secondTable")
        self.secondTable.setFont(font1)
        self.secondTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(46, 47, 48);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	/* background-color: rgb(207, 249, 226); */\n"
"	background-color: #009800;\n"
"	padding: 1px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	gridline-color: rgb(168, 168, 168);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color: rgb(207, 249, 226);\n"
"	border: 1px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.secondTable, 2, 0, 1, 3)


        self.verticalLayout_4.addWidget(self.frameHistoric)

        self.stackedWidget.addWidget(self.pageHistoric)
        self.pageExport = QWidget()
        self.pageExport.setObjectName(u"pageExport")
        self.pageExport.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        self.gridLayout = QGridLayout(self.pageExport)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.thirdBoxDependency = QComboBox(self.pageExport)
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.addItem("")
        self.thirdBoxDependency.setObjectName(u"thirdBoxDependency")
        self.thirdBoxDependency.setMaximumSize(QSize(16777215, 30))
        self.thirdBoxDependency.setFont(font2)
        self.thirdBoxDependency.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout.addWidget(self.thirdBoxDependency, 2, 1, 1, 1)

        self.thirdLineMotherName = QLineEdit(self.pageExport)
        self.thirdLineMotherName.setObjectName(u"thirdLineMotherName")
        self.thirdLineMotherName.setMaximumSize(QSize(16777215, 30))
        self.thirdLineMotherName.setFont(font2)
        self.thirdLineMotherName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.thirdLineMotherName, 1, 3, 1, 3)

        self.thirdLineFinalDate = QLineEdit(self.pageExport)
        self.thirdLineFinalDate.setObjectName(u"thirdLineFinalDate")
        self.thirdLineFinalDate.setMaximumSize(QSize(130, 30))
        self.thirdLineFinalDate.setFont(font2)
        self.thirdLineFinalDate.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.thirdLineFinalDate, 0, 1, 1, 1)

        self.thirdLineInitDate = QLineEdit(self.pageExport)
        self.thirdLineInitDate.setObjectName(u"thirdLineInitDate")
        self.thirdLineInitDate.setMaximumSize(QSize(130, 30))
        self.thirdLineInitDate.setFont(font2)
        self.thirdLineInitDate.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.thirdLineInitDate, 0, 0, 1, 1)

        self.thirdBtnExport = QPushButton(self.pageExport)
        self.thirdBtnExport.setObjectName(u"thirdBtnExport")
        self.thirdBtnExport.setMinimumSize(QSize(130, 30))
        self.thirdBtnExport.setMaximumSize(QSize(130, 30))
        self.thirdBtnExport.setFont(font2)
        self.thirdBtnExport.setCursor(QCursor(Qt.PointingHandCursor))
        self.thirdBtnExport.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.thirdBtnExport, 2, 4, 1, 1)

        self.thirdBoxClinic = QComboBox(self.pageExport)
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.addItem("")
        self.thirdBoxClinic.setObjectName(u"thirdBoxClinic")
        self.thirdBoxClinic.setMaximumSize(QSize(16777215, 30))
        self.thirdBoxClinic.setFont(font2)
        self.thirdBoxClinic.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout.addWidget(self.thirdBoxClinic, 2, 0, 1, 1)

        self.thirdLineCpf = QLineEdit(self.pageExport)
        self.thirdLineCpf.setObjectName(u"thirdLineCpf")
        self.thirdLineCpf.setMaximumSize(QSize(150, 30))
        self.thirdLineCpf.setFont(font2)
        self.thirdLineCpf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.thirdLineCpf, 1, 0, 1, 1)

        self.thirdBoxBed = QComboBox(self.pageExport)
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.addItem("")
        self.thirdBoxBed.setObjectName(u"thirdBoxBed")
        self.thirdBoxBed.setMaximumSize(QSize(16777215, 30))
        self.thirdBoxBed.setFont(font2)
        self.thirdBoxBed.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout.addWidget(self.thirdBoxBed, 2, 2, 1, 1)

        self.thirdLinePatient = QLineEdit(self.pageExport)
        self.thirdLinePatient.setObjectName(u"thirdLinePatient")
        self.thirdLinePatient.setMaximumSize(QSize(16777215, 30))
        self.thirdLinePatient.setFont(font2)
        self.thirdLinePatient.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.thirdLinePatient, 1, 1, 1, 2)

        self.thirdCheckData = QCheckBox(self.pageExport)
        self.thirdCheckData.setObjectName(u"thirdCheckData")
        self.thirdCheckData.setFont(font2)
        self.thirdCheckData.setCursor(QCursor(Qt.PointingHandCursor))
        self.thirdCheckData.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.thirdCheckData, 2, 3, 1, 1)

        self.thirdBtnSearch = QPushButton(self.pageExport)
        self.thirdBtnSearch.setObjectName(u"thirdBtnSearch")
        self.thirdBtnSearch.setMinimumSize(QSize(130, 30))
        self.thirdBtnSearch.setMaximumSize(QSize(130, 30))
        self.thirdBtnSearch.setFont(font2)
        self.thirdBtnSearch.setCursor(QCursor(Qt.PointingHandCursor))
        self.thirdBtnSearch.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.thirdBtnSearch, 2, 5, 1, 1)

        self.thirdTable = QTableWidget(self.pageExport)
        self.thirdTable.setObjectName(u"thirdTable")
        self.thirdTable.setFont(font1)
        self.thirdTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(46, 47, 48);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	/* background-color: rgb(207, 249, 226); */\n"
"	background-color: #009800;\n"
"	padding: 1px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	gridline-color: rgb(168, 168, 168);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color: rgb(207, 249, 226);\n"
"	border: 1px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.thirdTable, 3, 0, 1, 6)

        self.stackedWidget.addWidget(self.pageExport)
        self.pageRegister = QWidget()
        self.pageRegister.setObjectName(u"pageRegister")
        self.pageRegister.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.pageRegister)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frameRegister = QFrame(self.pageRegister)
        self.frameRegister.setObjectName(u"frameRegister")
        self.frameRegister.setMinimumSize(QSize(600, 0))
        self.frameRegister.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/logo/images/logo.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.frameRegister.setFrameShape(QFrame.NoFrame)
        self.frameRegister.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameRegister)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.fourthLineName = QLineEdit(self.frameRegister)
        self.fourthLineName.setObjectName(u"fourthLineName")
        self.fourthLineName.setMaximumSize(QSize(16777215, 30))
        self.fourthLineName.setFont(font2)
        self.fourthLineName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.fourthLineName, 0, 0, 1, 2)

        self.fourthBtnConfirm = QPushButton(self.frameRegister)
        self.fourthBtnConfirm.setObjectName(u"fourthBtnConfirm")
        self.fourthBtnConfirm.setMinimumSize(QSize(130, 30))
        self.fourthBtnConfirm.setMaximumSize(QSize(130, 30))
        self.fourthBtnConfirm.setFont(font2)
        self.fourthBtnConfirm.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.fourthBtnConfirm, 2, 0, 1, 1)

        self.fourthBoxProfessionType = QComboBox(self.frameRegister)
        self.fourthBoxProfessionType.addItem("")
        self.fourthBoxProfessionType.addItem("")
        self.fourthBoxProfessionType.setObjectName(u"fourthBoxProfessionType")
        self.fourthBoxProfessionType.setMaximumSize(QSize(16777215, 30))
        self.fourthBoxProfessionType.setFont(font2)
        self.fourthBoxProfessionType.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_2.addWidget(self.fourthBoxProfessionType, 1, 0, 1, 2)

        self.fourthLineClean = QPushButton(self.frameRegister)
        self.fourthLineClean.setObjectName(u"fourthLineClean")
        self.fourthLineClean.setMinimumSize(QSize(130, 30))
        self.fourthLineClean.setMaximumSize(QSize(130, 30))
        self.fourthLineClean.setFont(font2)
        self.fourthLineClean.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.fourthLineClean, 2, 1, 1, 1)

        self.fourthLineCrm = QLineEdit(self.frameRegister)
        self.fourthLineCrm.setObjectName(u"fourthLineCrm")
        self.fourthLineCrm.setMaximumSize(QSize(16777215, 30))
        self.fourthLineCrm.setFont(font2)
        self.fourthLineCrm.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"QLineEdit::disabled {\n"
"	background-color: rgb(114, 114, 114);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.fourthLineCrm, 1, 2, 1, 1)

        self.fourthLineAdress = QLineEdit(self.frameRegister)
        self.fourthLineAdress.setObjectName(u"fourthLineAdress")
        self.fourthLineAdress.setMaximumSize(QSize(16777215, 30))
        self.fourthLineAdress.setFont(font2)
        self.fourthLineAdress.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.fourthLineAdress, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frameRegister, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageRegister)
        self.pageRecibo = QWidget()
        self.pageRecibo.setObjectName(u"pageRecibo")
        self.gridLayout_3 = QGridLayout(self.pageRecibo)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.fifthBtnSearch = QPushButton(self.pageRecibo)
        self.fifthBtnSearch.setObjectName(u"fifthBtnSearch")
        self.fifthBtnSearch.setMinimumSize(QSize(130, 30))
        self.fifthBtnSearch.setMaximumSize(QSize(130, 30))
        self.fifthBtnSearch.setFont(font2)
        self.fifthBtnSearch.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifthBtnSearch.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.fifthBtnSearch, 4, 3, 1, 1)

        self.fifthLineCpf = QLineEdit(self.pageRecibo)
        self.fifthLineCpf.setObjectName(u"fifthLineCpf")
        sizePolicy8.setHeightForWidth(self.fifthLineCpf.sizePolicy().hasHeightForWidth())
        self.fifthLineCpf.setSizePolicy(sizePolicy8)
        self.fifthLineCpf.setMaximumSize(QSize(16777215, 30))
        self.fifthLineCpf.setFont(font2)
        self.fifthLineCpf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.fifthLineCpf, 1, 0, 1, 1)

        self.fifthLinePayer = QLineEdit(self.pageRecibo)
        self.fifthLinePayer.setObjectName(u"fifthLinePayer")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.fifthLinePayer.sizePolicy().hasHeightForWidth())
        self.fifthLinePayer.setSizePolicy(sizePolicy9)
        self.fifthLinePayer.setMaximumSize(QSize(16777215, 30))
        self.fifthLinePayer.setFont(font2)
        self.fifthLinePayer.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.fifthLinePayer, 3, 0, 1, 5)

        self.fifthBoxReciboType = QComboBox(self.pageRecibo)
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.addItem("")
        self.fifthBoxReciboType.setObjectName(u"fifthBoxReciboType")
        sizePolicy9.setHeightForWidth(self.fifthBoxReciboType.sizePolicy().hasHeightForWidth())
        self.fifthBoxReciboType.setSizePolicy(sizePolicy9)
        self.fifthBoxReciboType.setMaximumSize(QSize(16777215, 30))
        self.fifthBoxReciboType.setFont(font2)
        self.fifthBoxReciboType.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_3.addWidget(self.fifthBoxReciboType, 4, 0, 1, 2)

        self.fifthLineValue = QLineEdit(self.pageRecibo)
        self.fifthLineValue.setObjectName(u"fifthLineValue")
        sizePolicy8.setHeightForWidth(self.fifthLineValue.sizePolicy().hasHeightForWidth())
        self.fifthLineValue.setSizePolicy(sizePolicy8)
        self.fifthLineValue.setMaximumSize(QSize(16777215, 30))
        self.fifthLineValue.setFont(font2)
        self.fifthLineValue.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.fifthLineValue, 2, 0, 1, 1)

        self.fifthBtnTotalRecibo = QPushButton(self.pageRecibo)
        self.fifthBtnTotalRecibo.setObjectName(u"fifthBtnTotalRecibo")
        self.fifthBtnTotalRecibo.setMinimumSize(QSize(130, 30))
        self.fifthBtnTotalRecibo.setMaximumSize(QSize(130, 30))
        self.fifthBtnTotalRecibo.setFont(font2)
        self.fifthBtnTotalRecibo.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifthBtnTotalRecibo.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.fifthBtnTotalRecibo, 0, 4, 1, 1)

        self.fifthLineObs = QLineEdit(self.pageRecibo)
        self.fifthLineObs.setObjectName(u"fifthLineObs")
        self.fifthLineObs.setMaximumSize(QSize(16777215, 30))
        self.fifthLineObs.setFont(font2)
        self.fifthLineObs.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.fifthLineObs, 2, 1, 1, 4)

        self.fifthLinePatient = QLineEdit(self.pageRecibo)
        self.fifthLinePatient.setObjectName(u"fifthLinePatient")
        self.fifthLinePatient.setMaximumSize(QSize(16777215, 30))
        self.fifthLinePatient.setFont(font2)
        self.fifthLinePatient.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.fifthLinePatient, 1, 1, 1, 4)

        self.fifthBtnCancel = QPushButton(self.pageRecibo)
        self.fifthBtnCancel.setObjectName(u"fifthBtnCancel")
        self.fifthBtnCancel.setMinimumSize(QSize(130, 30))
        self.fifthBtnCancel.setMaximumSize(QSize(130, 30))
        self.fifthBtnCancel.setFont(font2)
        self.fifthBtnCancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifthBtnCancel.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.fifthBtnCancel, 4, 4, 1, 1)

        self.fifthBtnPrint = QPushButton(self.pageRecibo)
        self.fifthBtnPrint.setObjectName(u"fifthBtnPrint")
        self.fifthBtnPrint.setMinimumSize(QSize(130, 30))
        self.fifthBtnPrint.setMaximumSize(QSize(130, 30))
        self.fifthBtnPrint.setFont(font2)
        self.fifthBtnPrint.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifthBtnPrint.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.fifthBtnPrint, 4, 2, 1, 1)

        self.label_14 = QLabel(self.pageRecibo)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setPointSize(22)
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 4)

        self.fifthTable = QTableWidget(self.pageRecibo)
        if (self.fifthTable.columnCount() < 8):
            self.fifthTable.setColumnCount(8)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.fifthTable.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        self.fifthTable.setObjectName(u"fifthTable")
        self.fifthTable.setFont(font1)
        self.fifthTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(46, 47, 48);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	/* background-color: rgb(207, 249, 226); */\n"
"	background-color: #009800;\n"
"	padding: 1px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	gridline-color: rgb(168, 168, 168);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color: rgb(207, 249, 226);\n"
"	border: 1px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.fifthTable, 5, 0, 1, 5)

        self.stackedWidget.addWidget(self.pageRecibo)
        self.pagePatient = QWidget()
        self.pagePatient.setObjectName(u"pagePatient")
        self.gridLayout_4 = QGridLayout(self.pagePatient)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.sixthLinePatient = QLineEdit(self.pagePatient)
        self.sixthLinePatient.setObjectName(u"sixthLinePatient")
        self.sixthLinePatient.setMaximumSize(QSize(16777215, 30))
        self.sixthLinePatient.setFont(font2)
        self.sixthLinePatient.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.sixthLinePatient, 0, 1, 1, 1)

        self.sixthLineBornDate = QLineEdit(self.pagePatient)
        self.sixthLineBornDate.setObjectName(u"sixthLineBornDate")
        sizePolicy8.setHeightForWidth(self.sixthLineBornDate.sizePolicy().hasHeightForWidth())
        self.sixthLineBornDate.setSizePolicy(sizePolicy8)
        self.sixthLineBornDate.setMaximumSize(QSize(16777215, 30))
        self.sixthLineBornDate.setFont(font2)
        self.sixthLineBornDate.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.sixthLineBornDate, 1, 0, 1, 1)

        self.sixthBtnSearch = QPushButton(self.pagePatient)
        self.sixthBtnSearch.setObjectName(u"sixthBtnSearch")
        self.sixthBtnSearch.setMinimumSize(QSize(130, 30))
        self.sixthBtnSearch.setMaximumSize(QSize(130, 30))
        self.sixthBtnSearch.setFont(font2)
        self.sixthBtnSearch.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_4.addWidget(self.sixthBtnSearch, 1, 1, 1, 1, Qt.AlignRight)

        self.sixthLineMotherName = QLineEdit(self.pagePatient)
        self.sixthLineMotherName.setObjectName(u"sixthLineMotherName")
        self.sixthLineMotherName.setMaximumSize(QSize(16777215, 30))
        self.sixthLineMotherName.setFont(font2)
        self.sixthLineMotherName.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.sixthLineMotherName, 0, 2, 1, 1)

        self.sixthBtnExport = QPushButton(self.pagePatient)
        self.sixthBtnExport.setObjectName(u"sixthBtnExport")
        self.sixthBtnExport.setMinimumSize(QSize(130, 30))
        self.sixthBtnExport.setMaximumSize(QSize(130, 30))
        self.sixthBtnExport.setFont(font2)
        self.sixthBtnExport.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_4.addWidget(self.sixthBtnExport, 1, 2, 1, 1)

        self.sixthLineCpf = QLineEdit(self.pagePatient)
        self.sixthLineCpf.setObjectName(u"sixthLineCpf")
        sizePolicy8.setHeightForWidth(self.sixthLineCpf.sizePolicy().hasHeightForWidth())
        self.sixthLineCpf.setSizePolicy(sizePolicy8)
        self.sixthLineCpf.setMaximumSize(QSize(16777215, 30))
        self.sixthLineCpf.setFont(font2)
        self.sixthLineCpf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.sixthLineCpf, 0, 0, 1, 1)

        self.sixthTable = QTableWidget(self.pagePatient)
        if (self.sixthTable.columnCount() < 20):
            self.sixthTable.setColumnCount(20)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(8, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(9, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(10, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(11, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(12, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(13, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(14, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(15, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(16, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(17, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(18, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.sixthTable.setHorizontalHeaderItem(19, __qtablewidgetitem42)
        self.sixthTable.setObjectName(u"sixthTable")
        self.sixthTable.setFont(font1)
        self.sixthTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(46, 47, 48);\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	/* background-color: rgb(207, 249, 226); */\n"
"	background-color: #009800;\n"
"	padding: 1px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	gridline-color: rgb(168, 168, 168);\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color: rgb(207, 249, 226);\n"
"	border: 1px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.sixthTable, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.pagePatient)
        self.pageAlta = QWidget()
        self.pageAlta.setObjectName(u"pageAlta")
        self.verticalLayout_5 = QVBoxLayout(self.pageAlta)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frameAlta = QFrame(self.pageAlta)
        self.frameAlta.setObjectName(u"frameAlta")
        self.frameAlta.setMinimumSize(QSize(600, 0))
        self.frameAlta.setMaximumSize(QSize(700, 16777215))
        self.frameAlta.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/logo/images/logo.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"")
        self.frameAlta.setFrameShape(QFrame.StyledPanel)
        self.frameAlta.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frameAlta)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.seventhLinePatient = QLineEdit(self.frameAlta)
        self.seventhLinePatient.setObjectName(u"seventhLinePatient")
        self.seventhLinePatient.setMaximumSize(QSize(16777215, 30))
        self.seventhLinePatient.setFont(font2)
        self.seventhLinePatient.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.seventhLinePatient, 0, 0, 1, 2)

        self.seventhBoxDischargeType = QComboBox(self.frameAlta)
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.addItem("")
        self.seventhBoxDischargeType.setObjectName(u"seventhBoxDischargeType")
        self.seventhBoxDischargeType.setMaximumSize(QSize(16777215, 30))
        self.seventhBoxDischargeType.setFont(font2)
        self.seventhBoxDischargeType.setStyleSheet(u"QComboBox {\n"
"	color: #ffffff;\n"
"	border: 2px solid rgb(121, 121, 121);\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: none;\n"
"	background-color: rgb(85, 85, 85);\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 15px;\n"
"	color: #ffffff;\n"
"                                        \n"
"	border-left-width: 1px;\n"
"	border-left-color: darkgray;\n"
"	border-left-style: solid; \n"
"	border-top-right-radius: 3px; \n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	background-image: url(:/logo/images/arrow-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-image: url(:/images/fundoBox.png);\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: #ffffff;\n"
"}")

        self.gridLayout_7.addWidget(self.seventhBoxDischargeType, 2, 0, 1, 2)

        self.seventhLineDischargeDate = QLineEdit(self.frameAlta)
        self.seventhLineDischargeDate.setObjectName(u"seventhLineDischargeDate")
        sizePolicy8.setHeightForWidth(self.seventhLineDischargeDate.sizePolicy().hasHeightForWidth())
        self.seventhLineDischargeDate.setSizePolicy(sizePolicy8)
        self.seventhLineDischargeDate.setMaximumSize(QSize(16777215, 30))
        self.seventhLineDischargeDate.setFont(font2)
        self.seventhLineDischargeDate.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.seventhLineDischargeDate, 1, 0, 1, 1)

        self.seventhLineCpf = QLineEdit(self.frameAlta)
        self.seventhLineCpf.setObjectName(u"seventhLineCpf")
        self.seventhLineCpf.setMaximumSize(QSize(16777215, 30))
        self.seventhLineCpf.setFont(font2)
        self.seventhLineCpf.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.seventhLineCpf, 0, 2, 1, 1)

        self.seventhLineDischargeHour = QLineEdit(self.frameAlta)
        self.seventhLineDischargeHour.setObjectName(u"seventhLineDischargeHour")
        sizePolicy8.setHeightForWidth(self.seventhLineDischargeHour.sizePolicy().hasHeightForWidth())
        self.seventhLineDischargeHour.setSizePolicy(sizePolicy8)
        self.seventhLineDischargeHour.setMaximumSize(QSize(16777215, 30))
        self.seventhLineDischargeHour.setFont(font2)
        self.seventhLineDischargeHour.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(144, 144, 144);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	padding: 3px;\n"
"	color: #ffffff;\n"
"	padding-left: 8px;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.seventhLineDischargeHour, 1, 1, 1, 1)

        self.seventhBtnConfirm = QPushButton(self.frameAlta)
        self.seventhBtnConfirm.setObjectName(u"seventhBtnConfirm")
        self.seventhBtnConfirm.setMinimumSize(QSize(140, 30))
        self.seventhBtnConfirm.setMaximumSize(QSize(140, 30))
        self.seventhBtnConfirm.setFont(font2)
        self.seventhBtnConfirm.setStyleSheet(u"QPushButton::Hover {\n"
"	background-color: rgb(113, 113, 113);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(91, 91, 91);\n"
"	color: rgb(232, 232, 232);\n"
"	border: 2px solid rgb(100, 100, 100);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_7.addWidget(self.seventhBtnConfirm, 3, 2, 1, 1, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frameAlta, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pageAlta)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.firstLineCpf, self.firstLinePatientName)
        QWidget.setTabOrder(self.firstLinePatientName, self.firstLineBornDay)
        QWidget.setTabOrder(self.firstLineBornDay, self.firstLineAge)
        QWidget.setTabOrder(self.firstLineAge, self.firstBoxSex)
        QWidget.setTabOrder(self.firstBoxSex, self.firstBoxSkinColor)
        QWidget.setTabOrder(self.firstBoxSkinColor, self.firstBoxCivilStats)
        QWidget.setTabOrder(self.firstBoxCivilStats, self.firstLineProfession)
        QWidget.setTabOrder(self.firstLineProfession, self.firstLineSusCard)
        QWidget.setTabOrder(self.firstLineSusCard, self.firstLineRG)
        QWidget.setTabOrder(self.firstLineRG, self.firstLineFatherName)
        QWidget.setTabOrder(self.firstLineFatherName, self.firstLineMotherName)
        QWidget.setTabOrder(self.firstLineMotherName, self.firstLinePhoneOne)
        QWidget.setTabOrder(self.firstLinePhoneOne, self.firstLinePhoneTwo)
        QWidget.setTabOrder(self.firstLinePhoneTwo, self.firstLineAdress)
        QWidget.setTabOrder(self.firstLineAdress, self.firstLineDistrict)
        QWidget.setTabOrder(self.firstLineDistrict, self.firstLineCity)
        QWidget.setTabOrder(self.firstLineCity, self.firstLineCep)
        QWidget.setTabOrder(self.firstLineCep, self.firstLineUf)
        QWidget.setTabOrder(self.firstLineUf, self.firstBoxUrbanZone)
        QWidget.setTabOrder(self.firstBoxUrbanZone, self.firstLineResponsible)
        QWidget.setTabOrder(self.firstLineResponsible, self.firstBoxClinic)
        QWidget.setTabOrder(self.firstBoxClinic, self.firstBoxBed)
        QWidget.setTabOrder(self.firstBoxBed, self.firstBoxDependency)
        QWidget.setTabOrder(self.firstBoxDependency, self.firstBoxAdmission)
        QWidget.setTabOrder(self.firstBoxAdmission, self.firstBoxDoctor)
        QWidget.setTabOrder(self.firstBoxDoctor, self.firstBtnConfirm)
        QWidget.setTabOrder(self.firstBtnConfirm, self.firstBtnClean)
        QWidget.setTabOrder(self.firstBtnClean, self.firstLineTreatHour)
        QWidget.setTabOrder(self.firstLineTreatHour, self.firstLineTreatDate)
        QWidget.setTabOrder(self.firstLineTreatDate, self.firstBtnRegister)
        QWidget.setTabOrder(self.firstBtnRegister, self.secondLineCpf)
        QWidget.setTabOrder(self.secondLineCpf, self.secondLinePatientName)
        QWidget.setTabOrder(self.secondLinePatientName, self.secondLineMotherName)
        QWidget.setTabOrder(self.secondLineMotherName, self.secondBtnConfirm)
        QWidget.setTabOrder(self.secondBtnConfirm, self.secondBtnClean)
        QWidget.setTabOrder(self.secondBtnClean, self.thirdLineInitDate)
        QWidget.setTabOrder(self.thirdLineInitDate, self.thirdLineFinalDate)
        QWidget.setTabOrder(self.thirdLineFinalDate, self.thirdLineCpf)
        QWidget.setTabOrder(self.thirdLineCpf, self.thirdLinePatient)
        QWidget.setTabOrder(self.thirdLinePatient, self.thirdLineMotherName)
        QWidget.setTabOrder(self.thirdLineMotherName, self.thirdBoxClinic)
        QWidget.setTabOrder(self.thirdBoxClinic, self.thirdBoxDependency)
        QWidget.setTabOrder(self.thirdBoxDependency, self.thirdBoxBed)
        QWidget.setTabOrder(self.thirdBoxBed, self.thirdCheckData)
        QWidget.setTabOrder(self.thirdCheckData, self.thirdBtnSearch)
        QWidget.setTabOrder(self.thirdBtnSearch, self.thirdBtnExport)
        QWidget.setTabOrder(self.thirdBtnExport, self.fourthLineName)
        QWidget.setTabOrder(self.fourthLineName, self.fourthLineAdress)
        QWidget.setTabOrder(self.fourthLineAdress, self.fourthBoxProfessionType)
        QWidget.setTabOrder(self.fourthBoxProfessionType, self.fourthLineCrm)
        QWidget.setTabOrder(self.fourthLineCrm, self.fourthBtnConfirm)
        QWidget.setTabOrder(self.fourthBtnConfirm, self.fourthLineClean)
        QWidget.setTabOrder(self.fourthLineClean, self.fifthLineCpf)
        QWidget.setTabOrder(self.fifthLineCpf, self.fifthLinePatient)
        QWidget.setTabOrder(self.fifthLinePatient, self.fifthLineValue)
        QWidget.setTabOrder(self.fifthLineValue, self.fifthLineObs)
        QWidget.setTabOrder(self.fifthLineObs, self.fifthLinePayer)
        QWidget.setTabOrder(self.fifthLinePayer, self.fifthBoxReciboType)
        QWidget.setTabOrder(self.fifthBoxReciboType, self.fifthBtnPrint)
        QWidget.setTabOrder(self.fifthBtnPrint, self.fifthBtnSearch)
        QWidget.setTabOrder(self.fifthBtnSearch, self.fifthBtnCancel)
        QWidget.setTabOrder(self.fifthBtnCancel, self.fifthBtnTotalRecibo)
        QWidget.setTabOrder(self.fifthBtnTotalRecibo, self.sixthLineCpf)
        QWidget.setTabOrder(self.sixthLineCpf, self.sixthLinePatient)
        QWidget.setTabOrder(self.sixthLinePatient, self.sixthLineMotherName)
        QWidget.setTabOrder(self.sixthLineMotherName, self.sixthLineBornDate)
        QWidget.setTabOrder(self.sixthLineBornDate, self.sixthBtnSearch)
        QWidget.setTabOrder(self.sixthBtnSearch, self.sixthBtnExport)
        QWidget.setTabOrder(self.sixthBtnExport, self.seventhLinePatient)
        QWidget.setTabOrder(self.seventhLinePatient, self.seventhLineCpf)
        QWidget.setTabOrder(self.seventhLineCpf, self.a_24)
        QWidget.setTabOrder(self.a_24, self.seventhLineDischargeDate)
        QWidget.setTabOrder(self.seventhLineDischargeDate, self.seventhBoxDischargeType)
        QWidget.setTabOrder(self.seventhBoxDischargeType, self.seventhLineDischargeHour)
        QWidget.setTabOrder(self.seventhLineDischargeHour, self.seventhBtnConfirm)
        QWidget.setTabOrder(self.seventhBtnConfirm, self.p_26)
        QWidget.setTabOrder(self.p_26, self.p_27)
        QWidget.setTabOrder(self.p_27, self.p_28)
        QWidget.setTabOrder(self.p_28, self.p_29)
        QWidget.setTabOrder(self.p_29, self.p_30)
        QWidget.setTabOrder(self.p_30, self.a_26)
        QWidget.setTabOrder(self.a_26, self.b_26)
        QWidget.setTabOrder(self.b_26, self.a_27)
        QWidget.setTabOrder(self.a_27, self.b_27)
        QWidget.setTabOrder(self.b_27, self.a_28)
        QWidget.setTabOrder(self.a_28, self.b_28)
        QWidget.setTabOrder(self.b_28, self.a_29)
        QWidget.setTabOrder(self.a_29, self.b_29)
        QWidget.setTabOrder(self.b_29, self.a_30)
        QWidget.setTabOrder(self.a_30, self.b_30)
        QWidget.setTabOrder(self.b_30, self.p_31)
        QWidget.setTabOrder(self.p_31, self.p_32)
        QWidget.setTabOrder(self.p_32, self.p_33)
        QWidget.setTabOrder(self.p_33, self.p_34)
        QWidget.setTabOrder(self.p_34, self.p_35)
        QWidget.setTabOrder(self.p_35, self.p_36)
        QWidget.setTabOrder(self.p_36, self.a_31)
        QWidget.setTabOrder(self.a_31, self.b_31)
        QWidget.setTabOrder(self.b_31, self.a_32)
        QWidget.setTabOrder(self.a_32, self.b_32)
        QWidget.setTabOrder(self.b_32, self.a_33)
        QWidget.setTabOrder(self.a_33, self.b_33)
        QWidget.setTabOrder(self.b_33, self.a_34)
        QWidget.setTabOrder(self.a_34, self.b_34)
        QWidget.setTabOrder(self.b_34, self.a_35)
        QWidget.setTabOrder(self.a_35, self.b_35)
        QWidget.setTabOrder(self.b_35, self.a_36)
        QWidget.setTabOrder(self.a_36, self.b_36)
        QWidget.setTabOrder(self.b_36, self.p_37)
        QWidget.setTabOrder(self.p_37, self.a_37)
        QWidget.setTabOrder(self.a_37, self.b_37)
        QWidget.setTabOrder(self.b_37, self.p_38)
        QWidget.setTabOrder(self.p_38, self.p_39)
        QWidget.setTabOrder(self.p_39, self.p_40)
        QWidget.setTabOrder(self.p_40, self.a_38)
        QWidget.setTabOrder(self.a_38, self.b_38)
        QWidget.setTabOrder(self.b_38, self.a_39)
        QWidget.setTabOrder(self.a_39, self.b_39)
        QWidget.setTabOrder(self.b_39, self.a_40)
        QWidget.setTabOrder(self.a_40, self.b_40)
        QWidget.setTabOrder(self.b_40, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.p_1)
        QWidget.setTabOrder(self.p_1, self.p_2)
        QWidget.setTabOrder(self.p_2, self.a_1)
        QWidget.setTabOrder(self.a_1, self.b_1)
        QWidget.setTabOrder(self.b_1, self.a_2)
        QWidget.setTabOrder(self.a_2, self.b_2)
        QWidget.setTabOrder(self.b_2, self.p_3)
        QWidget.setTabOrder(self.p_3, self.a_3)
        QWidget.setTabOrder(self.a_3, self.b_3)
        QWidget.setTabOrder(self.b_3, self.p_4)
        QWidget.setTabOrder(self.p_4, self.a_4)
        QWidget.setTabOrder(self.a_4, self.b_4)
        QWidget.setTabOrder(self.b_4, self.p_5)
        QWidget.setTabOrder(self.p_5, self.a_5)
        QWidget.setTabOrder(self.a_5, self.b_5)
        QWidget.setTabOrder(self.b_5, self.p_6)
        QWidget.setTabOrder(self.p_6, self.p_7)
        QWidget.setTabOrder(self.p_7, self.p_8)
        QWidget.setTabOrder(self.p_8, self.p_9)
        QWidget.setTabOrder(self.p_9, self.a_7)
        QWidget.setTabOrder(self.a_7, self.a_8)
        QWidget.setTabOrder(self.a_8, self.a_9)
        QWidget.setTabOrder(self.a_9, self.b_6)
        QWidget.setTabOrder(self.b_6, self.b_7)
        QWidget.setTabOrder(self.b_7, self.b_8)
        QWidget.setTabOrder(self.b_8, self.b_9)
        QWidget.setTabOrder(self.b_9, self.p_10)
        QWidget.setTabOrder(self.p_10, self.a_10)
        QWidget.setTabOrder(self.a_10, self.a_6)
        QWidget.setTabOrder(self.a_6, self.b_11)
        QWidget.setTabOrder(self.b_11, self.p_11)
        QWidget.setTabOrder(self.p_11, self.p_12)
        QWidget.setTabOrder(self.p_12, self.a_11)
        QWidget.setTabOrder(self.a_11, self.p_13)
        QWidget.setTabOrder(self.p_13, self.secondTable)
        QWidget.setTabOrder(self.secondTable, self.a_14)
        QWidget.setTabOrder(self.a_14, self.p_14)
        QWidget.setTabOrder(self.p_14, self.b_12)
        QWidget.setTabOrder(self.b_12, self.a_12)
        QWidget.setTabOrder(self.a_12, self.a_15)
        QWidget.setTabOrder(self.a_15, self.p_15)
        QWidget.setTabOrder(self.p_15, self.a_13)
        QWidget.setTabOrder(self.a_13, self.b_14)
        QWidget.setTabOrder(self.b_14, self.b_13)
        QWidget.setTabOrder(self.b_13, self.p_16)
        QWidget.setTabOrder(self.p_16, self.p_17)
        QWidget.setTabOrder(self.p_17, self.thirdTable)
        QWidget.setTabOrder(self.thirdTable, self.menuBtnMap)
        QWidget.setTabOrder(self.menuBtnMap, self.menuBtnAtendimento)
        QWidget.setTabOrder(self.menuBtnAtendimento, self.menuBtnHistoric)
        QWidget.setTabOrder(self.menuBtnHistoric, self.menuBtnPatient)
        QWidget.setTabOrder(self.menuBtnPatient, self.menuBtnExport)
        QWidget.setTabOrder(self.menuBtnExport, self.menuBtnRegister)
        QWidget.setTabOrder(self.menuBtnRegister, self.menuBtnRecibo)
        QWidget.setTabOrder(self.menuBtnRecibo, self.b_10)
        QWidget.setTabOrder(self.b_10, self.b_15)
        QWidget.setTabOrder(self.b_15, self.b_17)
        QWidget.setTabOrder(self.b_17, self.b_16)
        QWidget.setTabOrder(self.b_16, self.p_18)
        QWidget.setTabOrder(self.p_18, self.a_17)
        QWidget.setTabOrder(self.a_17, self.a_16)
        QWidget.setTabOrder(self.a_16, self.a_20)
        QWidget.setTabOrder(self.a_20, self.p_19)
        QWidget.setTabOrder(self.p_19, self.b_18)
        QWidget.setTabOrder(self.b_18, self.a_19)
        QWidget.setTabOrder(self.a_19, self.p_21)
        QWidget.setTabOrder(self.p_21, self.a_21)
        QWidget.setTabOrder(self.a_21, self.a_18)
        QWidget.setTabOrder(self.a_18, self.p_20)
        QWidget.setTabOrder(self.p_20, self.b_20)
        QWidget.setTabOrder(self.b_20, self.b_19)
        QWidget.setTabOrder(self.b_19, self.fifthTable)
        QWidget.setTabOrder(self.fifthTable, self.p_22)
        QWidget.setTabOrder(self.p_22, self.p_24)
        QWidget.setTabOrder(self.p_24, self.p_25)
        QWidget.setTabOrder(self.p_25, self.p_23)
        QWidget.setTabOrder(self.p_23, self.a_22)
        QWidget.setTabOrder(self.a_22, self.b_21)
        QWidget.setTabOrder(self.b_21, self.sixthTable)
        QWidget.setTabOrder(self.sixthTable, self.b_22)
        QWidget.setTabOrder(self.b_22, self.b_24)
        QWidget.setTabOrder(self.b_24, self.b_23)
        QWidget.setTabOrder(self.b_23, self.a_23)
        QWidget.setTabOrder(self.a_23, self.a_25)
        QWidget.setTabOrder(self.a_25, self.b_25)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtnMap.setText(QCoreApplication.translate("MainWindow", u"Mapa de \n"
"Internados", None))
        self.menuBtnAtendimento.setText(QCoreApplication.translate("MainWindow", u"Atendimento", None))
        self.menuBtnHistoric.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico\n"
"do Paciente", None))
        self.menuBtnPatient.setText(QCoreApplication.translate("MainWindow", u"Cadastro\n"
"Paciente", None))
        self.menuBtnExport.setText(QCoreApplication.translate("MainWindow", u"Exporta\u00e7\u00e3o", None))
        self.menuBtnRegister.setText(QCoreApplication.translate("MainWindow", u"Cadastro\n"
"Profissional", None))
        self.menuBtnRecibo.setText(QCoreApplication.translate("MainWindow", u"Recibos", None))
        self.p_26.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_27.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_28.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_30.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_30.setText("")
        self.a_28.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_30.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_26.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_26.setText("")
#if QT_CONFIG(tooltip)
        self.b_29.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_29.setText("")
        self.a_26.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_28.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_28.setText("")
        self.a_27.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_27.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_27.setText("")
        self.a_29.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_30.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_29.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.c_26.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_27.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_28.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_29.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_30.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Maternidade", None))
        self.p_2.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_2.setText("")
        self.a_2.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apartamento 2", None))
        self.c_2.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
#if QT_CONFIG(tooltip)
        self.b_33.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_33.setText("")
#if QT_CONFIG(tooltip)
        self.b_34.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_34.setText("")
        self.a_33.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_36.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_32.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_36.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_36.setText("")
        self.p_33.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_31.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_35.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_37.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_37.setText("")
#if QT_CONFIG(tooltip)
        self.b_31.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_31.setText("")
        self.p_32.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_34.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_35.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_37.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_37.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_34.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_31.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_35.setText("")
        self.p_36.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_32.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_32.setText("")
        self.c_31.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_32.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_33.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_34.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_35.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_36.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_37.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pediatria", None))
        self.p_20.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_21.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_21.setText("")
#if QT_CONFIG(tooltip)
        self.b_19.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_19.setText("")
        self.a_18.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_21.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_20.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_18.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_18.setText("")
        self.p_21.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.c_19.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_20.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.p_19.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_19.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_20.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_20.setText("")
        self.c_21.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_18.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Enfermaria 4", None))
        self.p_38.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.c_38.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_39.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.a_39.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.c_40.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.p_39.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_38.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_38.setText("")
        self.a_38.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_40.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.b_39.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_39.setText("")
        self.a_40.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_40.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_40.setText("")
        self.a_1.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_1.setText("")
        self.p_1.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.c_1.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Apartamento 1", None))
        self.p_24.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_25.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_22.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_22.setText("")
        self.a_22.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_22.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_23.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_23.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_24.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_24.setText("")
#if QT_CONFIG(tooltip)
        self.b_23.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_23.setText("")
        self.a_25.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_25.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_25.setText("")
        self.a_24.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.c_22.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_23.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_24.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_25.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Enfermaria 5", None))
        self.a_7.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_6.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_7.setText("")
        self.p_9.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_9.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_9.setText("")
#if QT_CONFIG(tooltip)
        self.b_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_8.setText("")
        self.a_8.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_6.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_6.setText("")
        self.p_8.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_7.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_9.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.c_6.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_7.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_8.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_9.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enfermaria 1", None))
#if QT_CONFIG(tooltip)
        self.b_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apartamento 5", None))
        self.p_5.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_5.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.c_5.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.a_4.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_4.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Apartamento 4", None))
        self.c_4.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.p_12.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_13.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_11.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_11.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.p_10.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_12.setText("")
#if QT_CONFIG(tooltip)
        self.b_13.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_13.setText("")
#if QT_CONFIG(tooltip)
        self.b_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_10.setText("")
        self.p_13.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_10.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_11.setText("")
        self.a_12.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.c_10.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_11.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_12.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_13.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enfermaria 2", None))
        self.p_17.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_15.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_16.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.a_16.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.a_14.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(tooltip)
        self.b_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_15.setText("")
#if QT_CONFIG(tooltip)
        self.b_14.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_14.setText("")
#if QT_CONFIG(tooltip)
        self.b_16.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_16.setText("")
        self.a_17.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_15.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
#if QT_CONFIG(tooltip)
        self.b_17.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_17.setText("")
        self.p_14.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.c_14.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_15.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_16.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.c_17.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Enfermaria 3", None))
#if QT_CONFIG(tooltip)
        self.b_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Editar informa\u00e7\u00f5es do Paciente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.b_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apartamento 3", None))
        self.a_3.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.p_3.setText(QCoreApplication.translate("MainWindow", u"Livre", None))
        self.c_3.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica", None))
        self.firstLineProfession.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PROFISS\u00c3O", None))
        self.firstLineAge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IDADE", None))
        self.firstLineUf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.firstLineTreatDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA DE ATENDIMENTO", None))
        self.firstLinePatientName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.firstLineCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.firstBoxClinic.setItemText(0, "")
        self.firstBoxClinic.setItemText(1, QCoreApplication.translate("MainWindow", u"AMBULAT\u00d3RIO", None))
        self.firstBoxClinic.setItemText(2, QCoreApplication.translate("MainWindow", u"GERAL", None))
        self.firstBoxClinic.setItemText(3, QCoreApplication.translate("MainWindow", u"OBST\u00c9TRICO", None))
        self.firstBoxClinic.setItemText(4, QCoreApplication.translate("MainWindow", u"CIR\u00daRGICO", None))
        self.firstBoxClinic.setItemText(5, QCoreApplication.translate("MainWindow", u"PEDI\u00c1TRICO", None))
        self.firstBoxClinic.setItemText(6, QCoreApplication.translate("MainWindow", u"SA\u00daDE MENTAL", None))
        self.firstBoxClinic.setItemText(7, QCoreApplication.translate("MainWindow", u"CATARATA", None))
        self.firstBoxClinic.setItemText(8, QCoreApplication.translate("MainWindow", u"PTER\u00cdGEO", None))

        self.firstLineCity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.firstLineSusCard.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CART\u00c3O DO SUS", None))
        self.firstLineCep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.firstLineBornDay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NASCIMENTO", None))
        self.firstLineAdress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.firstBtnClean.setText(QCoreApplication.translate("MainWindow", u"Limpar Form", None))
        self.firstLinePhoneTwo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CELULAR", None))
        self.firstBoxBed.setItemText(0, "")
        self.firstBoxBed.setItemText(1, QCoreApplication.translate("MainWindow", u"APARTAMENTO 1", None))
        self.firstBoxBed.setItemText(2, QCoreApplication.translate("MainWindow", u"APARTAMENTO 2", None))
        self.firstBoxBed.setItemText(3, QCoreApplication.translate("MainWindow", u"APARTAMENTO 3", None))
        self.firstBoxBed.setItemText(4, QCoreApplication.translate("MainWindow", u"APARTAMENTO 4", None))
        self.firstBoxBed.setItemText(5, QCoreApplication.translate("MainWindow", u"APARTAMENTO 5", None))
        self.firstBoxBed.setItemText(6, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 1", None))
        self.firstBoxBed.setItemText(7, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 2", None))
        self.firstBoxBed.setItemText(8, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 3", None))
        self.firstBoxBed.setItemText(9, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 4", None))
        self.firstBoxBed.setItemText(10, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 1", None))
        self.firstBoxBed.setItemText(11, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 2", None))
        self.firstBoxBed.setItemText(12, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 3", None))
        self.firstBoxBed.setItemText(13, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 4", None))
        self.firstBoxBed.setItemText(14, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 1", None))
        self.firstBoxBed.setItemText(15, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 2", None))
        self.firstBoxBed.setItemText(16, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 3", None))
        self.firstBoxBed.setItemText(17, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 4", None))
        self.firstBoxBed.setItemText(18, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 1", None))
        self.firstBoxBed.setItemText(19, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 2", None))
        self.firstBoxBed.setItemText(20, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 3", None))
        self.firstBoxBed.setItemText(21, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 4", None))
        self.firstBoxBed.setItemText(22, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 1", None))
        self.firstBoxBed.setItemText(23, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 2", None))
        self.firstBoxBed.setItemText(24, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 3", None))
        self.firstBoxBed.setItemText(25, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 4", None))
        self.firstBoxBed.setItemText(26, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 1", None))
        self.firstBoxBed.setItemText(27, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 2", None))
        self.firstBoxBed.setItemText(28, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 3", None))
        self.firstBoxBed.setItemText(29, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 4", None))
        self.firstBoxBed.setItemText(30, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 5", None))
        self.firstBoxBed.setItemText(31, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 1", None))
        self.firstBoxBed.setItemText(32, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 2", None))
        self.firstBoxBed.setItemText(33, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 3", None))
        self.firstBoxBed.setItemText(34, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 4", None))
        self.firstBoxBed.setItemText(35, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 5", None))
        self.firstBoxBed.setItemText(36, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 6", None))
        self.firstBoxBed.setItemText(37, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 7", None))
        self.firstBoxBed.setItemText(38, QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00c3O 1", None))
        self.firstBoxBed.setItemText(39, QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00c3O 2", None))
        self.firstBoxBed.setItemText(40, QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00c3O 3", None))

        self.firstBoxDependency.setItemText(0, "")
        self.firstBoxDependency.setItemText(1, QCoreApplication.translate("MainWindow", u"SUS", None))
        self.firstBoxDependency.setItemText(2, QCoreApplication.translate("MainWindow", u"PARTICULAR", None))
        self.firstBoxDependency.setItemText(3, QCoreApplication.translate("MainWindow", u"UNIMED", None))
        self.firstBoxDependency.setItemText(4, QCoreApplication.translate("MainWindow", u"TOTALMED", None))
        self.firstBoxDependency.setItemText(5, QCoreApplication.translate("MainWindow", u"CONV\u00caNIO MUNICIPAL", None))
        self.firstBoxDependency.setItemText(6, QCoreApplication.translate("MainWindow", u"CASSI", None))
        self.firstBoxDependency.setItemText(7, QCoreApplication.translate("MainWindow", u"GRATUIDADE", None))

        self.firstLinePhoneOne.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.firstLineFatherName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PAI", None))
        self.firstLineRG.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.firstBtnConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.firstLineDistrict.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.firstLineTreatHour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HORA DE ATENDIMENTO", None))
        self.firstBtnRegister.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.firstBoxSkinColor.setItemText(0, QCoreApplication.translate("MainWindow", u"BRANCO", None))
        self.firstBoxSkinColor.setItemText(1, QCoreApplication.translate("MainWindow", u"PARDO", None))
        self.firstBoxSkinColor.setItemText(2, QCoreApplication.translate("MainWindow", u"PRETO", None))
        self.firstBoxSkinColor.setItemText(3, QCoreApplication.translate("MainWindow", u"INDIGENA", None))
        self.firstBoxSkinColor.setItemText(4, QCoreApplication.translate("MainWindow", u"AMARELO", None))

        self.firstLineMotherName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DA M\u00c3E", None))
        self.firstBoxUrbanZone.setItemText(0, QCoreApplication.translate("MainWindow", u"URBANA", None))
        self.firstBoxUrbanZone.setItemText(1, QCoreApplication.translate("MainWindow", u"RURAL", None))

        self.firstBoxSex.setItemText(0, QCoreApplication.translate("MainWindow", u"MASCULINO", None))
        self.firstBoxSex.setItemText(1, QCoreApplication.translate("MainWindow", u"FEMININO", None))

        self.firstBoxCivilStats.setItemText(0, QCoreApplication.translate("MainWindow", u"SOLTEIRO", None))
        self.firstBoxCivilStats.setItemText(1, QCoreApplication.translate("MainWindow", u"CASADO", None))
        self.firstBoxCivilStats.setItemText(2, QCoreApplication.translate("MainWindow", u"VIUVO", None))
        self.firstBoxCivilStats.setItemText(3, QCoreApplication.translate("MainWindow", u"DIVORCIADO", None))

        self.firstLineResponsible.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RESPONS\u00c1VEL PELO PACIENTE", None))
        self.secondBtnClean.setText(QCoreApplication.translate("MainWindow", u"Limpar Form", None))
        self.secondLineCpf.setText("")
        self.secondLineCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.secondLinePatientName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.secondBtnConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.secondLineMotherName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DA M\u00c3E", None))
        ___qtablewidgetitem = self.secondTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00d3DIGO DA FICHA", None));
        ___qtablewidgetitem1 = self.secondTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem2 = self.secondTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PACIENTE", None));
        ___qtablewidgetitem3 = self.secondTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DATA DE INTERNA\u00c7\u00c3O", None));
        ___qtablewidgetitem4 = self.secondTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SERVI\u00c7O DE ADMISS\u00c3O", None));
        ___qtablewidgetitem5 = self.secondTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"M\u00c9DICO", None));
        ___qtablewidgetitem6 = self.secondTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CRM", None));
        ___qtablewidgetitem7 = self.secondTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CL\u00cdNICA", None));
        ___qtablewidgetitem8 = self.secondTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"LEITO", None));
        ___qtablewidgetitem9 = self.secondTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DEP\u00caNDENCIA", None));
        ___qtablewidgetitem10 = self.secondTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"HORA DE INTERNA\u00c7\u00c3O", None));
        ___qtablewidgetitem11 = self.secondTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ALTA", None));
        ___qtablewidgetitem12 = self.secondTable.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"HORA DA ALTA", None));
        ___qtablewidgetitem13 = self.secondTable.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"DATA DE ALTA", None));
        ___qtablewidgetitem14 = self.secondTable.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"RESPONS\u00c1VEL", None));
        self.thirdBoxDependency.setItemText(0, "")
        self.thirdBoxDependency.setItemText(1, QCoreApplication.translate("MainWindow", u"SUS", None))
        self.thirdBoxDependency.setItemText(2, QCoreApplication.translate("MainWindow", u"PARTICULAR", None))
        self.thirdBoxDependency.setItemText(3, QCoreApplication.translate("MainWindow", u"UNIMED", None))
        self.thirdBoxDependency.setItemText(4, QCoreApplication.translate("MainWindow", u"TOTALMED", None))
        self.thirdBoxDependency.setItemText(5, QCoreApplication.translate("MainWindow", u"CONV\u00caNIO MUNICIPAL", None))
        self.thirdBoxDependency.setItemText(6, QCoreApplication.translate("MainWindow", u"CASSI", None))
        self.thirdBoxDependency.setItemText(7, QCoreApplication.translate("MainWindow", u"GRATUIDADE", None))

        self.thirdLineMotherName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DA M\u00c3E", None))
        self.thirdLineFinalDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA FINAL", None))
        self.thirdLineInitDate.setText("")
        self.thirdLineInitDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA INICIAL", None))
        self.thirdBtnExport.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.thirdBoxClinic.setItemText(0, "")
        self.thirdBoxClinic.setItemText(1, QCoreApplication.translate("MainWindow", u"AMBULAT\u00d3RIO", None))
        self.thirdBoxClinic.setItemText(2, QCoreApplication.translate("MainWindow", u"GERAL", None))
        self.thirdBoxClinic.setItemText(3, QCoreApplication.translate("MainWindow", u"OBST\u00c9TRICO", None))
        self.thirdBoxClinic.setItemText(4, QCoreApplication.translate("MainWindow", u"CIR\u00daRGICO", None))
        self.thirdBoxClinic.setItemText(5, QCoreApplication.translate("MainWindow", u"SA\u00daDE MENTAL", None))
        self.thirdBoxClinic.setItemText(6, QCoreApplication.translate("MainWindow", u"PEDI\u00c1TRICO", None))
        self.thirdBoxClinic.setItemText(7, QCoreApplication.translate("MainWindow", u"CATARATA", None))
        self.thirdBoxClinic.setItemText(8, QCoreApplication.translate("MainWindow", u"PTER\u00cdGEO", None))

        self.thirdLineCpf.setText("")
        self.thirdLineCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.thirdBoxBed.setItemText(0, "")
        self.thirdBoxBed.setItemText(1, QCoreApplication.translate("MainWindow", u"APARTAMENTO 1", None))
        self.thirdBoxBed.setItemText(2, QCoreApplication.translate("MainWindow", u"APARTAMENTO 2", None))
        self.thirdBoxBed.setItemText(3, QCoreApplication.translate("MainWindow", u"APARTAMENTO 3", None))
        self.thirdBoxBed.setItemText(4, QCoreApplication.translate("MainWindow", u"APARTAMENTO 4", None))
        self.thirdBoxBed.setItemText(5, QCoreApplication.translate("MainWindow", u"APARTAMENTO 5", None))
        self.thirdBoxBed.setItemText(6, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 1", None))
        self.thirdBoxBed.setItemText(7, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 2", None))
        self.thirdBoxBed.setItemText(8, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 3", None))
        self.thirdBoxBed.setItemText(9, QCoreApplication.translate("MainWindow", u"ENFERMARIA 1 LEITO 4", None))
        self.thirdBoxBed.setItemText(10, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 1", None))
        self.thirdBoxBed.setItemText(11, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 2", None))
        self.thirdBoxBed.setItemText(12, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 3", None))
        self.thirdBoxBed.setItemText(13, QCoreApplication.translate("MainWindow", u"ENFERMARIA 2 LEITO 4", None))
        self.thirdBoxBed.setItemText(14, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 1", None))
        self.thirdBoxBed.setItemText(15, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 2", None))
        self.thirdBoxBed.setItemText(16, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 3", None))
        self.thirdBoxBed.setItemText(17, QCoreApplication.translate("MainWindow", u"ENFERMARIA 3 LEITO 4", None))
        self.thirdBoxBed.setItemText(18, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 1", None))
        self.thirdBoxBed.setItemText(19, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 2", None))
        self.thirdBoxBed.setItemText(20, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 3", None))
        self.thirdBoxBed.setItemText(21, QCoreApplication.translate("MainWindow", u"ENFERMARIA 4 LEITO 4", None))
        self.thirdBoxBed.setItemText(22, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 1", None))
        self.thirdBoxBed.setItemText(23, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 2", None))
        self.thirdBoxBed.setItemText(24, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 3", None))
        self.thirdBoxBed.setItemText(25, QCoreApplication.translate("MainWindow", u"ENFERMARIA 5 LEITO 4", None))
        self.thirdBoxBed.setItemText(26, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 1", None))
        self.thirdBoxBed.setItemText(27, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 2", None))
        self.thirdBoxBed.setItemText(28, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 3", None))
        self.thirdBoxBed.setItemText(29, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 4", None))
        self.thirdBoxBed.setItemText(30, QCoreApplication.translate("MainWindow", u"MATERNIDADE LEITO 5", None))
        self.thirdBoxBed.setItemText(31, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 1", None))
        self.thirdBoxBed.setItemText(32, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 2", None))
        self.thirdBoxBed.setItemText(33, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 3", None))
        self.thirdBoxBed.setItemText(34, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 4", None))
        self.thirdBoxBed.setItemText(35, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 5", None))
        self.thirdBoxBed.setItemText(36, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 6", None))
        self.thirdBoxBed.setItemText(37, QCoreApplication.translate("MainWindow", u"PEDIATRIA LEITO 7", None))

        self.thirdLinePatient.setText("")
        self.thirdLinePatient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.thirdCheckData.setText(QCoreApplication.translate("MainWindow", u"Manter Dados", None))
        self.thirdBtnSearch.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.fourthLineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PROFISSIONAL", None))
        self.fourthBtnConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.fourthBoxProfessionType.setItemText(0, QCoreApplication.translate("MainWindow", u"MEDICO", None))
        self.fourthBoxProfessionType.setItemText(1, QCoreApplication.translate("MainWindow", u"RECEPCIONISTA", None))

        self.fourthLineClean.setText(QCoreApplication.translate("MainWindow", u"Limpar Form", None))
        self.fourthLineCrm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CRM M\u00c9DICO", None))
        self.fourthLineAdress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.fifthBtnSearch.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.fifthLineCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.fifthLinePayer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PAGADOR", None))
        self.fifthBoxReciboType.setItemText(0, QCoreApplication.translate("MainWindow", u"Procedimento Ambulatorial", None))
        self.fifthBoxReciboType.setItemText(1, QCoreApplication.translate("MainWindow", u"Tratamento Cir\u00fargico", None))
        self.fifthBoxReciboType.setItemText(2, QCoreApplication.translate("MainWindow", u"Tratamento Cl\u00ednico", None))
        self.fifthBoxReciboType.setItemText(3, QCoreApplication.translate("MainWindow", u"Procedimento Cir\u00fargico", None))
        self.fifthBoxReciboType.setItemText(4, QCoreApplication.translate("MainWindow", u"Raio-X", None))
        self.fifthBoxReciboType.setItemText(5, QCoreApplication.translate("MainWindow", u"Cirurgia de Catarata", None))
        self.fifthBoxReciboType.setItemText(6, QCoreApplication.translate("MainWindow", u"Cirurgia de Pter\u00edgeo", None))

        self.fifthLineValue.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.fifthBtnTotalRecibo.setText(QCoreApplication.translate("MainWindow", u"Recibo Total", None))
        self.fifthLineObs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00c3O", None))
        self.fifthLinePatient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.fifthBtnCancel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.fifthBtnPrint.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Recibo Recep\u00e7\u00e3o N\u00b0 00001/2022", None))
        ___qtablewidgetitem15 = self.fifthTable.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 DO RECIBO", None));
        ___qtablewidgetitem16 = self.fifthTable.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None));
        ___qtablewidgetitem17 = self.fifthTable.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem18 = self.fifthTable.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"DATA DE EMISS\u00c3O", None));
        ___qtablewidgetitem19 = self.fifthTable.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem20 = self.fifthTable.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"PROCEDIMENTO", None));
        ___qtablewidgetitem21 = self.fifthTable.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"PAGADOR", None));
        ___qtablewidgetitem22 = self.fifthTable.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"SITUA\u00c7\u00c3O", None));
        self.sixthLinePatient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.sixthLineBornDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA DE NASCIMENTO", None))
        self.sixthBtnSearch.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.sixthLineMotherName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DA M\u00c3E", None))
        self.sixthBtnExport.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.sixthLineCpf.setText("")
        self.sixthLineCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        ___qtablewidgetitem23 = self.sixthTable.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem24 = self.sixthTable.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem25 = self.sixthTable.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None));
        ___qtablewidgetitem26 = self.sixthTable.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"NASCIMENTO", None));
        ___qtablewidgetitem27 = self.sixthTable.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"PROFISS\u00c3O", None));
        ___qtablewidgetitem28 = self.sixthTable.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"CART\u00c3O SUS", None));
        ___qtablewidgetitem29 = self.sixthTable.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem30 = self.sixthTable.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"NOME DA M\u00c3E", None));
        ___qtablewidgetitem31 = self.sixthTable.horizontalHeaderItem(8)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"NOME DO PAI", None));
        ___qtablewidgetitem32 = self.sixthTable.horizontalHeaderItem(9)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"CONTATO 1", None));
        ___qtablewidgetitem33 = self.sixthTable.horizontalHeaderItem(10)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"CONTATO 2", None));
        ___qtablewidgetitem34 = self.sixthTable.horizontalHeaderItem(11)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem35 = self.sixthTable.horizontalHeaderItem(12)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem36 = self.sixthTable.horizontalHeaderItem(13)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem37 = self.sixthTable.horizontalHeaderItem(14)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem38 = self.sixthTable.horizontalHeaderItem(15)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem39 = self.sixthTable.horizontalHeaderItem(16)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"ZONA", None));
        ___qtablewidgetitem40 = self.sixthTable.horizontalHeaderItem(17)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"SEXO", None));
        ___qtablewidgetitem41 = self.sixthTable.horizontalHeaderItem(18)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"COR", None));
        ___qtablewidgetitem42 = self.sixthTable.horizontalHeaderItem(19)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"ESTADO CIVIL", None));
        self.seventhLinePatient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.seventhBoxDischargeType.setItemText(0, "")
        self.seventhBoxDischargeType.setItemText(1, QCoreApplication.translate("MainWindow", u"12 - ALTA MELHORADO", None))
        self.seventhBoxDischargeType.setItemText(2, QCoreApplication.translate("MainWindow", u"14 - ALTA A PEDIDO", None))
        self.seventhBoxDischargeType.setItemText(3, QCoreApplication.translate("MainWindow", u"16 - ALTA POR EVAS\u00c3O", None))
        self.seventhBoxDischargeType.setItemText(4, QCoreApplication.translate("MainWindow", u"18 - ALTA POR OUTROS MOTIVOS", None))
        self.seventhBoxDischargeType.setItemText(5, QCoreApplication.translate("MainWindow", u"61 - ALTA DA M\u00c3E/PU\u00c9RPERA E DO RESC\u00c9M-NASCIDO", None))
        self.seventhBoxDischargeType.setItemText(6, QCoreApplication.translate("MainWindow", u"62 - ALTA DA M\u00c3E/PU\u00c9RPERA E \u00d3BITO DO RESC\u00c9M-NASCIDO", None))
        self.seventhBoxDischargeType.setItemText(7, QCoreApplication.translate("MainWindow", u"63 - ALTA DA M\u00c3E/PU\u00c9RPERA E PERMAN\u00caNCIA DO RESC\u00c9M-NASCIDO", None))

        self.seventhLineDischargeDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA DE ALTA", None))
        self.seventhLineCpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.seventhLineDischargeHour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HORA", None))
        self.seventhBtnConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirmar Alta", None))
    # retranslateUi

