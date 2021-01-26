# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signin_windowIUXcfB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignIn(object):
    def setupUi(self, SignIn):
        if not SignIn.objectName():
            SignIn.setObjectName(u"SignIn")
        SignIn.resize(400, 440)
        SignIn.setMinimumSize(QSize(400, 440))
        SignIn.setMaximumSize(QSize(400, 440))
        SignIn.setStyleSheet(u"background-color: rgb(31, 64, 139);")
        self.centralwidget = QWidget(SignIn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 401, 40))
        self.label.setStyleSheet(u"font: 22pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 151, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 210, 151, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.userInp = QLineEdit(self.centralwidget)
        self.userInp.setObjectName(u"userInp")
        self.userInp.setGeometry(QRect(170, 130, 221, 41))
        self.userInp.setStyleSheet(u"border: 3px solid  rgb(255, 0, 127);\n"
"border-radius: 5px;\n"
"background-color: rgb(31, 64, 139);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.passInp = QLineEdit(self.centralwidget)
        self.passInp.setObjectName(u"passInp")
        self.passInp.setGeometry(QRect(170, 200, 221, 41))
        self.passInp.setStyleSheet(u"border: 3px solid  rgb(255, 0, 127);\n"
"border-radius: 5px;\n"
"background-color: rgb(31, 64, 139);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 250, 157, 72))
        self.frame.setStyleSheet(u"QFrame{\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 30px;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	background-color: #00007f;\n"
"	color: #fff\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logButt = QPushButton(self.frame)
        self.logButt.setObjectName(u"logButt")
        self.logButt.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.logButt)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 355, 161, 21))
        self.label_4.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(170, 320, 161, 81))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 30px;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	background-color: #00007f;\n"
"	color: #fff\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.newAccButt = QPushButton(self.frame_2)
        self.newAccButt.setObjectName(u"newAccButt")
        self.newAccButt.setGeometry(QRect(10, 30, 131, 31))
        self.alert = QLabel(self.centralwidget)
        self.alert.setObjectName(u"alert")
        self.alert.setGeometry(QRect(0, 70, 401, 41))
        self.alert.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.alert.setAlignment(Qt.AlignCenter)
        SignIn.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SignIn)
        self.statusbar.setObjectName(u"statusbar")
        SignIn.setStatusBar(self.statusbar)

        self.retranslateUi(SignIn)

        QMetaObject.connectSlotsByName(SignIn)
    # setupUi

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QCoreApplication.translate("SignIn", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SignIn", u"SIGN IN", None))
        self.label_2.setText(QCoreApplication.translate("SignIn", u"USERNAME:", None))
        self.label_3.setText(QCoreApplication.translate("SignIn", u"PASSWORD:", None))
#if QT_CONFIG(tooltip)
        self.userInp.setToolTip(QCoreApplication.translate("SignIn", u"<html><head/><body><p>Input your login...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.logButt.setText(QCoreApplication.translate("SignIn", u"LOG IN", None))
        self.label_4.setText(QCoreApplication.translate("SignIn", u"Don't have account?", None))
        self.newAccButt.setText(QCoreApplication.translate("SignIn", u"CLICK HERE", None))
        self.alert.setText("")
    # retranslateUi

