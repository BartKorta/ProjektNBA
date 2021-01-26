# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading screenOrybbZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import test

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QSize(800, 450))
        MainWindow.setMaximumSize(QSize(800, 450))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"border: 8px solid rgb(255, 0, 0);\n"
"border-radius: 20px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setStyleSheet(u"border: 0px solid;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 321, 141))
        self.label.setStyleSheet(u"border: 0px soldid;")
        self.label.setPixmap(QPixmap(u":/nowyPrzedrostek/logo.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 210, 781, 71))
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"font: 24pt \"ROG Fonts\";\n"
"border: 0px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 30, 281, 161))
        self.label_3.setStyleSheet(u"border: 0px soldid;")
        self.label_3.setPixmap(QPixmap(u":/nowyPrzedrostek/longnba.png"))
        self.label_3.setScaledContents(True)
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()

        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 781, 41))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt bold \"Microsoft YaHei\";\n"
"border: 0px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.getDataLabel = QLabel(self.frame_2)
        self.getDataLabel.setObjectName(u"getDataLabel")
        self.getDataLabel.setGeometry(QRect(0, 0, 781, 41))
        self.getDataLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt bold \"Microsoft YaHei\";\n"
"border: 0px;")
        self.getDataLabel.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(640, 30, 93, 28))

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PERSONAL NBA TRACKER", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PLEASE WAIT ...", None))
        self.getDataLabel.setText(QCoreApplication.translate("MainWindow", u"Getting data ...", None))
        self.pushButton.setText("")
    # retranslateUi

