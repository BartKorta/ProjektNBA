# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_windowAbtLyW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(400, 440)
        SignUp.setMinimumSize(QSize(400, 440))
        SignUp.setMaximumSize(QSize(400, 440))
        SignUp.setStyleSheet(u"background-color: rgb(31, 64, 139);")
        self.centralwidget = QWidget(SignUp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 40))
        self.label.setStyleSheet(u"font: 22pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 151, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 151, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 230, 201, 21))
        self.label_4.setStyleSheet(u"font: 12pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")
        self.userInp = QLineEdit(self.centralwidget)
        self.userInp.setObjectName(u"userInp")
        self.userInp.setGeometry(QRect(210, 100, 181, 41))
        self.userInp.setStyleSheet(u"border: 3px solid  rgb(255, 0, 127);\n"
"border-radius: 5px;\n"
"background-color: rgb(31, 64, 139);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.passInp = QLineEdit(self.centralwidget)
        self.passInp.setObjectName(u"passInp")
        self.passInp.setGeometry(QRect(210, 160, 181, 41))
        self.passInp.setStyleSheet(u"border: 3px solid  rgb(255, 0, 127);\n"
"border-radius: 5px;\n"
"background-color: rgb(31, 64, 139);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.confpassInp = QLineEdit(self.centralwidget)
        self.confpassInp.setObjectName(u"confpassInp")
        self.confpassInp.setGeometry(QRect(210, 220, 181, 41))
        self.confpassInp.setStyleSheet(u"border: 3px solid  rgb(255, 0, 127);\n"
"border-radius: 5px;\n"
"background-color: rgb(31, 64, 139);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 290, 211, 80))
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
        self.regButt = QPushButton(self.frame)
        self.regButt.setObjectName(u"regButt")
        self.regButt.setGeometry(QRect(10, 20, 181, 41))
        self.regButt.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.alert = QLabel(self.centralwidget)
        self.alert.setObjectName(u"alert")
        self.alert.setGeometry(QRect(0, 50, 401, 41))
        self.alert.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.alert.setAlignment(Qt.AlignCenter)
        SignUp.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SignUp)
        self.statusbar.setObjectName(u"statusbar")
        SignUp.setStatusBar(self.statusbar)

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SignUp", u"SIGN UP", None))
        self.label_2.setText(QCoreApplication.translate("SignUp", u"USERNAME:", None))
        self.label_3.setText(QCoreApplication.translate("SignUp", u"PASSWORD:", None))
        self.label_4.setText(QCoreApplication.translate("SignUp", u"CONFIRM PASS:", None))
#if QT_CONFIG(tooltip)
        self.userInp.setToolTip(QCoreApplication.translate("SignUp", u"<html><head/><body><p>Input your login...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.passInp.setToolTip(QCoreApplication.translate("SignUp", u"<html><head/><body><p>Input your login...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.confpassInp.setToolTip(QCoreApplication.translate("SignUp", u"<html><head/><body><p>Input your login...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regButt.setText(QCoreApplication.translate("SignUp", u"REGISTER", None))
        self.alert.setText("")
    # retranslateUi

