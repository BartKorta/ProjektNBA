# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windownvUmWJ.ui'
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
        MainWindow.resize(1002, 855)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(31, 64, 139);\n"
"border-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 100))
        self.header.setMaximumSize(QSize(16777215, 150))
        self.header.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame_38 = QFrame(self.header)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(200, 0))
        self.frame_38.setMaximumSize(QSize(200, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_38)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(140, 80))
        self.label.setMaximumSize(QSize(140, 80))
        self.label.setPixmap(QPixmap(u":/nowyPrzedrostek/longnba.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.header)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_45 = QLabel(self.frame_39)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(150, 70))
        self.label_45.setMaximumSize(QSize(150, 70))
        self.label_45.setPixmap(QPixmap(u":/nowyPrzedrostek/logo.png"))
        self.label_45.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_45, 0, Qt.AlignLeft)

        self.label_46 = QLabel(self.frame_39)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 20pt \"ROG Fonts\";\n"
"color: rgb(255, 0, 127);")

        self.horizontalLayout_6.addWidget(self.label_46)


        self.horizontalLayout_2.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.header)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(100, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_44 = QLabel(self.frame_40)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(35, 80))
        self.label_44.setMaximumSize(QSize(35, 80))
        self.label_44.setPixmap(QPixmap(u":/nowyPrzedrostek/nba.png"))
        self.label_44.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_44, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_40)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 730))
        self.body.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.body.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_items = QFrame(self.body)
        self.main_items.setObjectName(u"main_items")
        self.main_items.setMinimumSize(QSize(200, 0))
        self.main_items.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.main_items.setFont(font)
        self.main_items.setStyleSheet(u"QFrame{\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(201, 8, 42);\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 30px;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	background-color: #c9082a;\n"
"	color: #fff\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #ec3448;\n"
"}")
        self.main_items.setFrameShape(QFrame.StyledPanel)
        self.main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_items)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.buttGames = QPushButton(self.main_items)
        self.buttGames.setObjectName(u"buttGames")
        self.buttGames.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.buttGames)

        self.buttStand = QPushButton(self.main_items)
        self.buttStand.setObjectName(u"buttStand")
        self.buttStand.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.buttStand)

        self.buttNews = QPushButton(self.main_items)
        self.buttNews.setObjectName(u"buttNews")
        self.buttNews.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.buttNews)

        self.buttStats = QPushButton(self.main_items)
        self.buttStats.setObjectName(u"buttStats")
        self.buttStats.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.buttStats)

        self.butFavt = QPushButton(self.main_items)
        self.butFavt.setObjectName(u"butFavt")
        self.butFavt.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.butFavt)

        self.buttSett = QPushButton(self.main_items)
        self.buttSett.setObjectName(u"buttSett")
        self.buttSett.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.buttSett)


        self.horizontalLayout.addWidget(self.main_items)

        self.main_view = QFrame(self.body)
        self.main_view.setObjectName(u"main_view")
        self.main_view.setMinimumSize(QSize(800, 750))
        self.main_view.setAutoFillBackground(False)
        self.main_view.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.main_view.setFrameShape(QFrame.StyledPanel)
        self.main_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_view)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.main_view)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_games = QWidget()
        self.page_games.setObjectName(u"page_games")
        self.verticalLayout_52 = QVBoxLayout(self.page_games)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_2 = QLabel(self.page_games)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 70))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_2)

        self.frame_61 = QFrame(self.page_games)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(16777215, 90))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_61)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 90))
        self.frame_63.setMaximumSize(QSize(16777215, 90))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_66 = QFrame(self.frame_63)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"QFrame{\n"
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
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.PrevDateButt = QPushButton(self.frame_66)
        self.PrevDateButt.setObjectName(u"PrevDateButt")
        self.PrevDateButt.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_27.addWidget(self.PrevDateButt)


        self.horizontalLayout_26.addWidget(self.frame_66, 0, Qt.AlignHCenter)

        self.dateLabel = QLabel(self.frame_63)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.dateLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.dateLabel)

        self.frame_67 = QFrame(self.frame_63)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"QFrame{\n"
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
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_67)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.nextDateButt = QPushButton(self.frame_67)
        self.nextDateButt.setObjectName(u"nextDateButt")
        self.nextDateButt.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_54.addWidget(self.nextDateButt)


        self.horizontalLayout_26.addWidget(self.frame_67, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_63)


        self.verticalLayout_52.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.page_games)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_62)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.infoNoMatches = QLabel(self.frame_62)
        self.infoNoMatches.setObjectName(u"infoNoMatches")
        self.infoNoMatches.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")

        self.verticalLayout_56.addWidget(self.infoNoMatches, 0, Qt.AlignHCenter)

        self.MatchesTable = QTableWidget(self.frame_62)
        if (self.MatchesTable.columnCount() < 7):
            self.MatchesTable.setColumnCount(7)
        self.MatchesTable.setObjectName(u"MatchesTable")
        self.MatchesTable.setMinimumSize(QSize(750, 0))
        self.MatchesTable.setMaximumSize(QSize(256, 16777215))
        self.MatchesTable.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.MatchesTable.setFrameShape(QFrame.NoFrame)
        self.MatchesTable.setFrameShadow(QFrame.Plain)
        self.MatchesTable.setLineWidth(0)
        self.MatchesTable.setShowGrid(False)
        self.MatchesTable.setGridStyle(Qt.NoPen)
        self.MatchesTable.setColumnCount(7)
        self.MatchesTable.horizontalHeader().setVisible(False)
        self.MatchesTable.horizontalHeader().setHighlightSections(False)
        self.MatchesTable.verticalHeader().setVisible(False)
        self.MatchesTable.verticalHeader().setHighlightSections(False)

        self.verticalLayout_56.addWidget(self.MatchesTable, 0, Qt.AlignHCenter)


        self.verticalLayout_52.addWidget(self.frame_62)

        self.stackedWidget.addWidget(self.page_games)
        self.page_standings = QWidget()
        self.page_standings.setObjectName(u"page_standings")
        self.verticalLayout_4 = QVBoxLayout(self.page_standings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.page_standings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tableWidget = QTableWidget(self.page_standings)
        if (self.tableWidget.columnCount() < 16):
            self.tableWidget.setColumnCount(16)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        if (self.tableWidget.rowCount() < 30):
            self.tableWidget.setRowCount(30)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(624, 452))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(u"background-color: #ffffff;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"RecordSheet::item {\n"
"        border: 5px;\n"
"        color: black;\n"
"        padding: 3px 3px 3px 3px;\n"
"}")
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_standings)
        self.page_news = QWidget()
        self.page_news.setObjectName(u"page_news")
        self.verticalLayout_49 = QVBoxLayout(self.page_news)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_4 = QLabel(self.page_news)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 60))
        self.label_4.setMaximumSize(QSize(16777215, 70))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.label_4)

        self.frame_42 = QFrame(self.page_news)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 90))
        self.frame_42.setMaximumSize(QSize(16777215, 90))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"QFrame{\n"
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
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.NewsPrevButt = QPushButton(self.frame_45)
        self.NewsPrevButt.setObjectName(u"NewsPrevButt")
        self.NewsPrevButt.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_8.addWidget(self.NewsPrevButt)


        self.horizontalLayout_7.addWidget(self.frame_45, 0, Qt.AlignHCenter)

        self.teamNameNews = QLabel(self.frame_42)
        self.teamNameNews.setObjectName(u"teamNameNews")
        self.teamNameNews.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.teamNameNews.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.teamNameNews)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"QFrame{\n"
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
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_44)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.NewsNextButt = QPushButton(self.frame_44)
        self.NewsNextButt.setObjectName(u"NewsNextButt")
        self.NewsNextButt.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_50.addWidget(self.NewsNextButt)


        self.horizontalLayout_7.addWidget(self.frame_44, 0, Qt.AlignHCenter)


        self.verticalLayout_49.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.page_news)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_43)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_46)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(150, 0))
        self.frame_51.setMaximumSize(QSize(150, 16777215))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_52 = QLabel(self.frame_51)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(42, 80))
        self.label_52.setPixmap(QPixmap(u":/nowyPrzedrostek/one.png"))
        self.label_52.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_52)

        self.logoNews1 = QLabel(self.frame_51)
        self.logoNews1.setObjectName(u"logoNews1")

        self.horizontalLayout_19.addWidget(self.logoNews1)


        self.horizontalLayout_9.addWidget(self.frame_51)

        self.article1 = QLabel(self.frame_46)
        self.article1.setObjectName(u"article1")
        self.article1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_9.addWidget(self.article1)

        self.frame_56 = QFrame(self.frame_46)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(120, 0))
        self.frame_56.setMaximumSize(QSize(120, 16777215))
        self.frame_56.setStyleSheet(u"QFrame{\n"
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
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.artlink1 = QPushButton(self.frame_56)
        self.artlink1.setObjectName(u"artlink1")
        self.artlink1.setMaximumSize(QSize(100, 16777215))
        self.artlink1.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_18.addWidget(self.artlink1)


        self.horizontalLayout_9.addWidget(self.frame_56)


        self.verticalLayout_51.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_47)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(150, 0))
        self.frame_52.setMaximumSize(QSize(150, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_54 = QLabel(self.frame_52)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(42, 80))
        self.label_54.setPixmap(QPixmap(u":/nowyPrzedrostek/two.png"))
        self.label_54.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_54)

        self.logoNews2 = QLabel(self.frame_52)
        self.logoNews2.setObjectName(u"logoNews2")

        self.horizontalLayout_20.addWidget(self.logoNews2)


        self.horizontalLayout_10.addWidget(self.frame_52)

        self.article2 = QLabel(self.frame_47)
        self.article2.setObjectName(u"article2")
        self.article2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.article2)

        self.frame_57 = QFrame(self.frame_47)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(120, 0))
        self.frame_57.setMaximumSize(QSize(120, 16777215))
        self.frame_57.setStyleSheet(u"QFrame{\n"
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
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.artlink2 = QPushButton(self.frame_57)
        self.artlink2.setObjectName(u"artlink2")
        self.artlink2.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_17.addWidget(self.artlink2)


        self.horizontalLayout_10.addWidget(self.frame_57)


        self.verticalLayout_51.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_43)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_48)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(150, 0))
        self.frame_53.setMaximumSize(QSize(150, 16777215))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_56 = QLabel(self.frame_53)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(42, 80))
        self.label_56.setPixmap(QPixmap(u":/nowyPrzedrostek/three.png"))
        self.label_56.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_56)

        self.logoNews3 = QLabel(self.frame_53)
        self.logoNews3.setObjectName(u"logoNews3")

        self.horizontalLayout_21.addWidget(self.logoNews3)


        self.horizontalLayout_11.addWidget(self.frame_53)

        self.article3 = QLabel(self.frame_48)
        self.article3.setObjectName(u"article3")
        self.article3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_11.addWidget(self.article3)

        self.frame_58 = QFrame(self.frame_48)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(120, 0))
        self.frame_58.setMaximumSize(QSize(120, 16777215))
        self.frame_58.setStyleSheet(u"QFrame{\n"
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
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.artlink3 = QPushButton(self.frame_58)
        self.artlink3.setObjectName(u"artlink3")
        self.artlink3.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_16.addWidget(self.artlink3)


        self.horizontalLayout_11.addWidget(self.frame_58)


        self.verticalLayout_51.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_43)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_49)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(150, 0))
        self.frame_54.setMaximumSize(QSize(150, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_58 = QLabel(self.frame_54)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(42, 80))
        self.label_58.setPixmap(QPixmap(u":/nowyPrzedrostek/four.png"))
        self.label_58.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_58)

        self.logoNews4 = QLabel(self.frame_54)
        self.logoNews4.setObjectName(u"logoNews4")

        self.horizontalLayout_22.addWidget(self.logoNews4)


        self.horizontalLayout_12.addWidget(self.frame_54)

        self.article4 = QLabel(self.frame_49)
        self.article4.setObjectName(u"article4")
        self.article4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_12.addWidget(self.article4)

        self.frame_59 = QFrame(self.frame_49)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(120, 0))
        self.frame_59.setMaximumSize(QSize(120, 16777215))
        self.frame_59.setStyleSheet(u"QFrame{\n"
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
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.artlink4 = QPushButton(self.frame_59)
        self.artlink4.setObjectName(u"artlink4")
        self.artlink4.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_15.addWidget(self.artlink4)


        self.horizontalLayout_12.addWidget(self.frame_59)


        self.verticalLayout_51.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_43)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_50)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(150, 0))
        self.frame_55.setMaximumSize(QSize(150, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_60 = QLabel(self.frame_55)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(42, 80))
        self.label_60.setPixmap(QPixmap(u":/nowyPrzedrostek/five.png"))
        self.label_60.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.label_60)

        self.logoNews5 = QLabel(self.frame_55)
        self.logoNews5.setObjectName(u"logoNews5")

        self.horizontalLayout_23.addWidget(self.logoNews5)


        self.horizontalLayout_13.addWidget(self.frame_55)

        self.article5 = QLabel(self.frame_50)
        self.article5.setObjectName(u"article5")
        self.article5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_13.addWidget(self.article5)

        self.frame_60 = QFrame(self.frame_50)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(120, 0))
        self.frame_60.setMaximumSize(QSize(120, 16777215))
        self.frame_60.setStyleSheet(u"QFrame{\n"
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
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.artlink5 = QPushButton(self.frame_60)
        self.artlink5.setObjectName(u"artlink5")
        self.artlink5.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_14.addWidget(self.artlink5)


        self.horizontalLayout_13.addWidget(self.frame_60)


        self.verticalLayout_51.addWidget(self.frame_50)


        self.verticalLayout_49.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.page_news)
        self.page_stats = QWidget()
        self.page_stats.setObjectName(u"page_stats")
        self.verticalLayout_57 = QVBoxLayout(self.page_stats)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_5 = QLabel(self.page_stats)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 70))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.label_5)

        self.frame_68 = QFrame(self.page_stats)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMaximumSize(QSize(16777215, 100))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_68)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 80))
        self.frame_70.setMaximumSize(QSize(16777215, 80))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"QFrame{\n"
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
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.PlayersPrevButt = QPushButton(self.frame_71)
        self.PlayersPrevButt.setObjectName(u"PlayersPrevButt")
        self.PlayersPrevButt.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_29.addWidget(self.PlayersPrevButt)


        self.horizontalLayout_28.addWidget(self.frame_71, 0, Qt.AlignHCenter)

        self.teamNamePlayers = QLabel(self.frame_70)
        self.teamNamePlayers.setObjectName(u"teamNamePlayers")
        self.teamNamePlayers.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.teamNamePlayers.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.teamNamePlayers)

        self.frame_72 = QFrame(self.frame_70)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"QFrame{\n"
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
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_72)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.PlayersNextButt = QPushButton(self.frame_72)
        self.PlayersNextButt.setObjectName(u"PlayersNextButt")
        self.PlayersNextButt.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_58.addWidget(self.PlayersNextButt)


        self.horizontalLayout_28.addWidget(self.frame_72, 0, Qt.AlignHCenter)


        self.verticalLayout_59.addWidget(self.frame_70)


        self.verticalLayout_57.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.page_stats)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(700, 0))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_69)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.playersTable = QTableWidget(self.frame_69)
        if (self.playersTable.columnCount() < 7):
            self.playersTable.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.playersTable.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.playersTable.setObjectName(u"playersTable")
        self.playersTable.setMinimumSize(QSize(780, 0))
        self.playersTable.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 127);\n"
"gridline-color: rgb(0, 0, 127);\n"
"selection-background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 0, 127);")
        self.playersTable.setFrameShape(QFrame.NoFrame)
        self.playersTable.setFrameShadow(QFrame.Plain)
        self.playersTable.setLineWidth(0)
        self.playersTable.setMidLineWidth(0)
        self.playersTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.playersTable.setAutoScroll(True)
        self.playersTable.setAlternatingRowColors(False)
        self.playersTable.setShowGrid(False)
        self.playersTable.setGridStyle(Qt.NoPen)
        self.playersTable.setSortingEnabled(True)
        self.playersTable.setColumnCount(7)
        self.playersTable.horizontalHeader().setVisible(False)
        self.playersTable.verticalHeader().setVisible(False)

        self.verticalLayout_60.addWidget(self.playersTable)


        self.verticalLayout_57.addWidget(self.frame_69)

        self.stackedWidget.addWidget(self.page_stats)
        self.page_fav = QWidget()
        self.page_fav.setObjectName(u"page_fav")
        self.verticalLayout_5 = QVBoxLayout(self.page_fav)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.page_fav)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.page_fav)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(60, 60))
        self.label_14.setStyleSheet(u"background-image: url(C:/Users/barto/Documents/PythonImages/logonba.png);")
        self.label_14.setPixmap(QPixmap(u":/nowyPrzedrostek/ny.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.nypick = QRadioButton(self.frame_10)
        self.nypick.setObjectName(u"nypick")
        self.nypick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_13.addWidget(self.nypick, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_10, 0, Qt.AlignVCenter)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(60, 60))
        self.label_15.setStyleSheet(u"")
        self.label_15.setPixmap(QPixmap(u":/nowyPrzedrostek/bkn.png"))
        self.label_15.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.bknpick = QRadioButton(self.frame_11)
        self.bknpick.setObjectName(u"bknpick")
        self.bknpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_14.addWidget(self.bknpick, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(60, 60))
        self.label_16.setStyleSheet(u"background-image: url(:/nowyPrzedrostek/bos.png);")
        self.label_16.setPixmap(QPixmap(u":/nowyPrzedrostek/bos.png"))
        self.label_16.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.bospick = QRadioButton(self.frame_8)
        self.bospick.setObjectName(u"bospick")
        self.bospick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.bospick, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(60, 60))
        self.label_17.setStyleSheet(u"")
        self.label_17.setPixmap(QPixmap(u":/nowyPrzedrostek/phi.png"))
        self.label_17.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.phipick = QRadioButton(self.frame_12)
        self.phipick.setObjectName(u"phipick")
        self.phipick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_16.addWidget(self.phipick, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(60, 60))
        self.label_18.setPixmap(QPixmap(u":/nowyPrzedrostek/tor.png"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.torpick = QRadioButton(self.frame_9)
        self.torpick.setObjectName(u"torpick")
        self.torpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_17.addWidget(self.torpick, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_9)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setSpacing(1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(60, 60))
        self.label_19.setPixmap(QPixmap(u":/nowyPrzedrostek/chi.png"))
        self.label_19.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.chipick = QRadioButton(self.frame_13)
        self.chipick.setObjectName(u"chipick")
        self.chipick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_19.addWidget(self.chipick, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_14)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(60, 60))
        self.label_20.setPixmap(QPixmap(u":/nowyPrzedrostek/cle.png"))
        self.label_20.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.clepick = QRadioButton(self.frame_14)
        self.clepick.setObjectName(u"clepick")
        self.clepick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_20.addWidget(self.clepick, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(60, 60))
        self.label_21.setPixmap(QPixmap(u":/nowyPrzedrostek/det.png"))
        self.label_21.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.detpick = QRadioButton(self.frame_15)
        self.detpick.setObjectName(u"detpick")
        self.detpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_21.addWidget(self.detpick, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_17)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_22 = QLabel(self.frame_17)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(60, 60))
        self.label_22.setPixmap(QPixmap(u":/nowyPrzedrostek/ind.png"))
        self.label_22.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.indpick = QRadioButton(self.frame_17)
        self.indpick.setObjectName(u"indpick")
        self.indpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_23.addWidget(self.indpick, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_16)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(60, 60))
        self.label_23.setPixmap(QPixmap(u":/nowyPrzedrostek/mil.png"))
        self.label_23.setScaledContents(True)

        self.verticalLayout_24.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.milpick = QRadioButton(self.frame_16)
        self.milpick.setObjectName(u"milpick")
        self.milpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_24.addWidget(self.milpick, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_9.addWidget(self.frame_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_4)
        self.verticalLayout_22.setSpacing(1)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(1, 1, 1, 1)
        self.frame_18 = QFrame(self.frame_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_18)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_24 = QLabel(self.frame_18)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(60, 60))
        self.label_24.setPixmap(QPixmap(u":/nowyPrzedrostek/okc.png"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_25.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.okcpick = QRadioButton(self.frame_18)
        self.okcpick.setObjectName(u"okcpick")
        self.okcpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_25.addWidget(self.okcpick, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.frame_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(60, 60))
        self.label_25.setPixmap(QPixmap(u":/nowyPrzedrostek/den.png"))
        self.label_25.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.denpick = QRadioButton(self.frame_20)
        self.denpick.setObjectName(u"denpick")
        self.denpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_26.addWidget(self.denpick, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_19)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_26 = QLabel(self.frame_19)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(60, 60))
        self.label_26.setMaximumSize(QSize(60, 60))
        self.label_26.setPixmap(QPixmap(u":/nowyPrzedrostek/min.png"))
        self.label_26.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.minpick = QRadioButton(self.frame_19)
        self.minpick.setObjectName(u"minpick")
        self.minpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_27.addWidget(self.minpick, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.frame_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_21)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_27 = QLabel(self.frame_21)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(60, 60))
        self.label_27.setPixmap(QPixmap(u":/nowyPrzedrostek/utah.png"))
        self.label_27.setScaledContents(True)

        self.verticalLayout_28.addWidget(self.label_27, 0, Qt.AlignHCenter)

        self.utahpick = QRadioButton(self.frame_21)
        self.utahpick.setObjectName(u"utahpick")
        self.utahpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_28.addWidget(self.utahpick, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_22)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_28 = QLabel(self.frame_22)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(60, 60))
        self.label_28.setPixmap(QPixmap(u":/nowyPrzedrostek/por.png"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_29.addWidget(self.label_28, 0, Qt.AlignHCenter)

        self.porpick = QRadioButton(self.frame_22)
        self.porpick.setObjectName(u"porpick")
        self.porpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_29.addWidget(self.porpick, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_22)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_5)
        self.verticalLayout_30.setSpacing(1)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(1, 1, 1, 1)
        self.frame_23 = QFrame(self.frame_5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_23)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_29 = QLabel(self.frame_23)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(60, 60))
        self.label_29.setPixmap(QPixmap(u":/nowyPrzedrostek/gs.png"))
        self.label_29.setScaledContents(True)

        self.verticalLayout_31.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.gspick = QRadioButton(self.frame_23)
        self.gspick.setObjectName(u"gspick")
        self.gspick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_31.addWidget(self.gspick, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_5)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_24)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_30 = QLabel(self.frame_24)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(60, 60))
        self.label_30.setPixmap(QPixmap(u":/nowyPrzedrostek/lac.png"))
        self.label_30.setScaledContents(True)

        self.verticalLayout_32.addWidget(self.label_30, 0, Qt.AlignHCenter)

        self.lacpick = QRadioButton(self.frame_24)
        self.lacpick.setObjectName(u"lacpick")
        self.lacpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_32.addWidget(self.lacpick, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_5)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_25)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_31 = QLabel(self.frame_25)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(60, 60))
        self.label_31.setPixmap(QPixmap(u":/nowyPrzedrostek/phx.png"))
        self.label_31.setScaledContents(True)

        self.verticalLayout_33.addWidget(self.label_31, 0, Qt.AlignHCenter)

        self.phxpic = QRadioButton(self.frame_25)
        self.phxpic.setObjectName(u"phxpic")
        self.phxpic.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_33.addWidget(self.phxpic, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_5)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_26)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_32 = QLabel(self.frame_26)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(60, 60))
        self.label_32.setPixmap(QPixmap(u":/nowyPrzedrostek/lal.png"))
        self.label_32.setScaledContents(True)

        self.verticalLayout_34.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.lalpick = QRadioButton(self.frame_26)
        self.lalpick.setObjectName(u"lalpick")
        self.lalpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_34.addWidget(self.lalpick, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_5)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_27)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_33 = QLabel(self.frame_27)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(60, 60))
        self.label_33.setPixmap(QPixmap(u":/nowyPrzedrostek/sac.png"))
        self.label_33.setScaledContents(True)

        self.verticalLayout_35.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.sacpick = QRadioButton(self.frame_27)
        self.sacpick.setObjectName(u"sacpick")
        self.sacpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_35.addWidget(self.sacpick, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.frame_27)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_6)
        self.verticalLayout_36.setSpacing(1)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(1, 1, 1, 1)
        self.frame_28 = QFrame(self.frame_6)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_28)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(60, 60))
        self.label_34.setPixmap(QPixmap(u":/nowyPrzedrostek/atl.png"))
        self.label_34.setScaledContents(True)

        self.verticalLayout_38.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.atlpick = QRadioButton(self.frame_28)
        self.atlpick.setObjectName(u"atlpick")
        self.atlpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_38.addWidget(self.atlpick, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_6)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_29)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_35 = QLabel(self.frame_29)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(60, 60))
        self.label_35.setPixmap(QPixmap(u":/nowyPrzedrostek/cha.png"))
        self.label_35.setScaledContents(True)

        self.verticalLayout_39.addWidget(self.label_35, 0, Qt.AlignHCenter)

        self.chapick = QRadioButton(self.frame_29)
        self.chapick.setObjectName(u"chapick")
        self.chapick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_39.addWidget(self.chapick, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_6)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_30)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_36 = QLabel(self.frame_30)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(60, 60))
        self.label_36.setPixmap(QPixmap(u":/nowyPrzedrostek/mia.png"))
        self.label_36.setScaledContents(True)

        self.verticalLayout_40.addWidget(self.label_36, 0, Qt.AlignHCenter)

        self.miapick = QRadioButton(self.frame_30)
        self.miapick.setObjectName(u"miapick")
        self.miapick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_40.addWidget(self.miapick, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_6)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_31)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_37 = QLabel(self.frame_31)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(60, 60))
        self.label_37.setPixmap(QPixmap(u":/nowyPrzedrostek/wsh.png"))
        self.label_37.setScaledContents(True)

        self.verticalLayout_41.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.wshpick = QRadioButton(self.frame_31)
        self.wshpick.setObjectName(u"wshpick")
        self.wshpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_41.addWidget(self.wshpick, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_6)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_32)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_38 = QLabel(self.frame_32)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(60, 60))
        self.label_38.setPixmap(QPixmap(u":/nowyPrzedrostek/orl.png"))
        self.label_38.setScaledContents(True)

        self.verticalLayout_42.addWidget(self.label_38, 0, Qt.AlignHCenter)

        self.orlpick = QRadioButton(self.frame_32)
        self.orlpick.setObjectName(u"orlpick")
        self.orlpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_42.addWidget(self.orlpick, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_32)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_7)
        self.verticalLayout_37.setSpacing(1)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(1, 1, 1, 1)
        self.frame_33 = QFrame(self.frame_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_33)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_39 = QLabel(self.frame_33)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(60, 60))
        self.label_39.setPixmap(QPixmap(u":/nowyPrzedrostek/dal.png"))
        self.label_39.setScaledContents(True)

        self.verticalLayout_43.addWidget(self.label_39, 0, Qt.AlignHCenter)

        self.dalpick = QRadioButton(self.frame_33)
        self.dalpick.setObjectName(u"dalpick")
        self.dalpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_43.addWidget(self.dalpick, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_34)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_40 = QLabel(self.frame_34)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(60, 60))
        self.label_40.setPixmap(QPixmap(u":/nowyPrzedrostek/hou.png"))
        self.label_40.setScaledContents(True)

        self.verticalLayout_44.addWidget(self.label_40, 0, Qt.AlignHCenter)

        self.houpick = QRadioButton(self.frame_34)
        self.houpick.setObjectName(u"houpick")
        self.houpick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_44.addWidget(self.houpick, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_7)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_35)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_41 = QLabel(self.frame_35)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(60, 70))
        self.label_41.setPixmap(QPixmap(u":/nowyPrzedrostek/no.png"))
        self.label_41.setScaledContents(True)

        self.verticalLayout_45.addWidget(self.label_41, 0, Qt.AlignHCenter)

        self.nopick = QRadioButton(self.frame_35)
        self.nopick.setObjectName(u"nopick")
        self.nopick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_45.addWidget(self.nopick, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_7)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_36)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_42 = QLabel(self.frame_36)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(60, 60))
        self.label_42.setPixmap(QPixmap(u":/nowyPrzedrostek/sa.png"))
        self.label_42.setScaledContents(True)

        self.verticalLayout_46.addWidget(self.label_42, 0, Qt.AlignHCenter)

        self.sapick = QRadioButton(self.frame_36)
        self.sapick.setObjectName(u"sapick")
        self.sapick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_46.addWidget(self.sapick)


        self.verticalLayout_37.addWidget(self.frame_36, 0, Qt.AlignHCenter)

        self.frame_37 = QFrame(self.frame_7)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_37)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_43 = QLabel(self.frame_37)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(60, 60))
        self.label_43.setPixmap(QPixmap(u":/nowyPrzedrostek/mem.png"))
        self.label_43.setScaledContents(True)

        self.verticalLayout_47.addWidget(self.label_43, 0, Qt.AlignHCenter)

        self.mempick = QRadioButton(self.frame_37)
        self.mempick.setObjectName(u"mempick")
        self.mempick.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_47.addWidget(self.mempick, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.frame_37)


        self.verticalLayout_11.addWidget(self.frame_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)


        self.verticalLayout_5.addWidget(self.frame)

        self.label_47 = QLabel(self.page_fav)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")

        self.verticalLayout_5.addWidget(self.label_47, 0, Qt.AlignHCenter)

        self.frame_41 = QFrame(self.page_fav)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"QFrame{\n"
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
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_41)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.confFavTeamsButt = QPushButton(self.frame_41)
        self.confFavTeamsButt.setObjectName(u"confFavTeamsButt")
        self.confFavTeamsButt.setMinimumSize(QSize(250, 0))
        self.confFavTeamsButt.setMaximumSize(QSize(250, 48))
        self.confFavTeamsButt.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_48.addWidget(self.confFavTeamsButt)


        self.verticalLayout_5.addWidget(self.frame_41, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_fav)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.label_7 = QLabel(self.page_settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 20, 211, 51))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_view)


        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"PERSONAL NBA TRACKER", None))
        self.label_44.setText("")
        self.buttGames.setText(QCoreApplication.translate("MainWindow", u"GAMES", None))
        self.buttStand.setText(QCoreApplication.translate("MainWindow", u"STANDINGS", None))
        self.buttNews.setText(QCoreApplication.translate("MainWindow", u"NEWS", None))
        self.buttStats.setText(QCoreApplication.translate("MainWindow", u"PLAYERS", None))
        self.butFavt.setText(QCoreApplication.translate("MainWindow", u"FAV TEAMS", None))
        self.buttSett.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your Teams Games", None))
        self.PrevDateButt.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.nextDateButt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.infoNoMatches.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"League Standings", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"POS.", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"LOGO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TEAM NAME", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"W", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"L", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PCT", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"GB", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"HOME", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"AWAY", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DIV", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"CONF", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"PPG", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"O PPG", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"DIFF", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"STRK", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"L10", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Latest TOP 5 News", None))
        self.NewsPrevButt.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.teamNameNews.setText(QCoreApplication.translate("MainWindow", u"Team Name", None))
        self.NewsNextButt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_52.setText("")
        self.logoNews1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.article1.setText(QCoreApplication.translate("MainWindow", u"Article no 1.", None))
        self.artlink1.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_54.setText("")
        self.logoNews2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.article2.setText(QCoreApplication.translate("MainWindow", u"Article no 2.", None))
        self.artlink2.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_56.setText("")
        self.logoNews3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.article3.setText(QCoreApplication.translate("MainWindow", u"Article no 3.", None))
        self.artlink3.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_58.setText("")
        self.logoNews4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.article4.setText(QCoreApplication.translate("MainWindow", u"Article no 4.", None))
        self.artlink4.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_60.setText("")
        self.logoNews5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.article5.setText(QCoreApplication.translate("MainWindow", u"Article no 5.", None))
        self.artlink5.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Players Info", None))
        self.PlayersPrevButt.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.teamNamePlayers.setText(QCoreApplication.translate("MainWindow", u"Team Name", None))
        self.PlayersNextButt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        ___qtablewidgetitem16 = self.playersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.playersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Pos.", None));
        ___qtablewidgetitem18 = self.playersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem19 = self.playersTable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Ht", None));
        ___qtablewidgetitem20 = self.playersTable.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Wt", None));
        ___qtablewidgetitem21 = self.playersTable.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"College", None));
        ___qtablewidgetitem22 = self.playersTable.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pick Teams you want to follow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Atlantic", None))
        self.label_14.setText("")
        self.nypick.setText(QCoreApplication.translate("MainWindow", u"Knicks", None))
        self.label_15.setText("")
        self.bknpick.setText(QCoreApplication.translate("MainWindow", u"Nets", None))
        self.label_16.setText("")
        self.bospick.setText(QCoreApplication.translate("MainWindow", u"Celtics", None))
        self.label_17.setText("")
        self.phipick.setText(QCoreApplication.translate("MainWindow", u"Phila", None))
        self.label_18.setText("")
        self.torpick.setText(QCoreApplication.translate("MainWindow", u"Raptors", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Central", None))
        self.label_19.setText("")
        self.chipick.setText(QCoreApplication.translate("MainWindow", u"Bulls", None))
        self.label_20.setText("")
        self.clepick.setText(QCoreApplication.translate("MainWindow", u"Cavs", None))
        self.label_21.setText("")
        self.detpick.setText(QCoreApplication.translate("MainWindow", u"Pistons", None))
        self.label_22.setText("")
        self.indpick.setText(QCoreApplication.translate("MainWindow", u"Pacers", None))
        self.label_23.setText("")
        self.milpick.setText(QCoreApplication.translate("MainWindow", u"Bucks", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Northwest", None))
        self.label_24.setText("")
        self.okcpick.setText(QCoreApplication.translate("MainWindow", u"Thunder", None))
        self.label_25.setText("")
        self.denpick.setText(QCoreApplication.translate("MainWindow", u"Nuggets", None))
        self.label_26.setText("")
        self.minpick.setText(QCoreApplication.translate("MainWindow", u"Wolves", None))
        self.label_27.setText("")
        self.utahpick.setText(QCoreApplication.translate("MainWindow", u"Jazz", None))
        self.label_28.setText("")
        self.porpick.setText(QCoreApplication.translate("MainWindow", u"Blazers", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pacific", None))
        self.label_29.setText("")
        self.gspick.setText(QCoreApplication.translate("MainWindow", u"Warriors", None))
        self.label_30.setText("")
        self.lacpick.setText(QCoreApplication.translate("MainWindow", u"Clippers", None))
        self.label_31.setText("")
        self.phxpic.setText(QCoreApplication.translate("MainWindow", u"Suns", None))
        self.label_32.setText("")
        self.lalpick.setText(QCoreApplication.translate("MainWindow", u"Lakers", None))
        self.label_33.setText("")
        self.sacpick.setText(QCoreApplication.translate("MainWindow", u"Kings", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Southeast", None))
        self.label_34.setText("")
        self.atlpick.setText(QCoreApplication.translate("MainWindow", u"Hawks", None))
        self.label_35.setText("")
        self.chapick.setText(QCoreApplication.translate("MainWindow", u"Hornets", None))
        self.label_36.setText("")
        self.miapick.setText(QCoreApplication.translate("MainWindow", u"Heat", None))
        self.label_37.setText("")
        self.wshpick.setText(QCoreApplication.translate("MainWindow", u"Wizards", None))
        self.label_38.setText("")
        self.orlpick.setText(QCoreApplication.translate("MainWindow", u"Magic", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Southwest", None))
        self.label_39.setText("")
        self.dalpick.setText(QCoreApplication.translate("MainWindow", u"Mavericks", None))
        self.label_40.setText("")
        self.houpick.setText(QCoreApplication.translate("MainWindow", u"Rockets", None))
        self.label_41.setText("")
        self.nopick.setText(QCoreApplication.translate("MainWindow", u"Pelicans", None))
        self.label_42.setText("")
        self.sapick.setText(QCoreApplication.translate("MainWindow", u"Spurs", None))
        self.label_43.setText("")
        self.mempick.setText(QCoreApplication.translate("MainWindow", u"Grizzlies", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Warning! This action will force application realoading and re-logging.", None))
        self.confFavTeamsButt.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
    # retranslateUi



