import PySide2
import database_config
from selenium import webdriver
from datetime import datetime,timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import ui
import loading
import time
import teamsinfo
from teamsinfo import Team, NBATeams,Standing, TableRow
import PySide2
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtGui import *
import sys
import sqlite3
import signin
import signup
import nba_info_config

### some constant values

PATH = "C:\Program Files\chromedriver.exe"
BleacherLink = 'https://bleacherreport.com/'
##endof Const val

# Download article titles

def get_articles(listteams):
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=opt)
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    print(listteams)
    biglist = []
    for i in listteams:
        c.execute("SELECT brlink, abb FROM teams WHERE name=?",(i,))
        linkteam = c.fetchone()
        link = BleacherLink+linkteam[0]
        icon=linkteam[1].lower()
        driver.get(link)
        news = driver.find_elements_by_class_name("atom.articleTitle")
        l2 = list()
        for i in range(0,5):
            tlink = news[i].get_attribute('href')
            text = news[i].text
            l2.append((text,tlink,icon))
        biglist.append(l2)
    ActiveUser.setNewsTable(biglist)
    print(ActiveUser.newstable)


class ActiveUser:
    NAME = ''
    teams = []
    currentIt = 0
    newstable = []
    day_diff = 0
    matches = []
    @staticmethod
    def changeUsername(newusername):
        ActiveUser.NAME = newusername
    @staticmethod
    def clear():
        ActiveUser.NAME = ''
        ActiveUser.matches.clear()
    @staticmethod
    def updateteams():
        ActiveUser.teams.clear()
        n=ActiveUser.NAME
        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        tcurs = c.execute("SELECT team FROM favteams WHERE username=?", (n,))
        teams = tcurs.fetchall()
        for i in teams:
            ActiveUser.teams.append(i[0])

    @staticmethod
    def changeIt(isnext):
        if isnext:
            if ActiveUser.currentIt+1==len(ActiveUser.teams):
                ActiveUser.currentIt=0
            else:
                ActiveUser.currentIt+=1
        else:
            if ActiveUser.currentIt==0:
                ActiveUser.currentIt=len(ActiveUser.teams)-1
            else:
                ActiveUser.currentIt=ActiveUser.currentIt-1
    @staticmethod
    def setNewsTable(newstab):
        ActiveUser.newstable = newstab
    @staticmethod
    def changeDaydiff(isfur):
        if isfur:
            ActiveUser.day_diff=ActiveUser.day_diff+1
        else:
            ActiveUser.day_diff=ActiveUser.day_diff-1

    @staticmethod
    def getSelectedDay():
        return (datetime.now()+timedelta(days=ActiveUser.day_diff)).strftime('%d-%m-%Y')

    @staticmethod
    def getDayMatchFormat():
        return (datetime.now()+timedelta(days=ActiveUser.day_diff)).strftime('%d.%m')

    @staticmethod
    def setMatches(list):
        ActiveUser.matches=list

class Loading(QtWidgets.QMainWindow):
    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        self.ui = loading.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.ui.pushButton.clicked.connect(lambda: self.getArticles())
        print("HERE")
        self.show()
        time.sleep(5)
        #time.sleep(5)
        #self.getArticles()
        #self.getMatches()
        #mainWindow = MainWindow()
        #mainWindow.show()
        #self.hide()



class SignInWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = signin.Ui_SignIn()
        self.ui.setupUi(self)
        self.show()
        self.registerWindow = SignUpWindow()
        ### Navigation to next windows
        self.ui.passInp.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ui.newAccButt.clicked.connect(lambda: self.openSignUp())
        self.ui.logButt.clicked.connect(lambda: self.login())

    def openSignUp(self):
        self.registerWindow.show()

    def login(self):
        self.ui.alert.setText('')
        nick = self.ui.userInp.text()
        password = self.ui.passInp.text()
        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        name = c.execute("SELECT * FROM users WHERE username=? AND password=?", (nick,password,))
        odp2 = name.fetchone()
        if odp2==None:
            self.ui.alert.setText('Wrong password or username')
            return
        self.ui.alert.setText('Please wait. Loading...')
        ActiveUser.NAME = nick

        ActiveUser.updateteams()
        if len(ActiveUser.teams)>0:
            get_articles(ActiveUser.teams)
            ActiveUser.setMatches(nba_info_config.get_matches(ActiveUser.teams))
        mainWindow = MainWindow()

        self.hide()


class SignUpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = signup.Ui_SignUp()
        self.ui.setupUi(self)
        self.ui.alert.setText('')
        self.ui.passInp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.confpassInp.setEchoMode(QtWidgets.QLineEdit.Password)
        ### Register new user
        self.ui.regButt.clicked.connect(lambda: self.newuser())

    def newuser(self):
        self.ui.alert.setText('')
        nick = self.ui.userInp.text()
        password = self.ui.passInp.text()
        confpass = self.ui.confpassInp.text()

        if password!=confpass:
            self.ui.alert.setText('Passwords must be identical')
            return

        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        name = c.execute("SELECT username FROM users WHERE username=?",(nick,))
        o1 = name.fetchone()

        if len(password)<6:
            self.ui.alert.setText('Required password length: 6')
            return

        if o1!=None:
            self.ui.alert.setText('User already exists')
            return

        self.ui.alert.setText('')
        c.execute("INSERT INTO users values(?,?)",(nick,password))
        conn.commit()
        c.close()

        self.hide()



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #print(ActiveUser.newstable)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0,92,157,150))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.set_checked_if_ness()
        self.insert_rows_for_games()
        self.show()
        self.ui.dateLabel.setText(ActiveUser.getSelectedDay())
        self.ui.nextDateButt.clicked.connect(lambda: self.button_date_clicked(True))
        self.ui.PrevDateButt.clicked.connect(lambda: self.button_date_clicked(False))
        self.ui.PlayersNextButt.clicked.connect(lambda: self.buttClickedPlayers(True))
        self.ui.PlayersPrevButt.clicked.connect(lambda: self.buttClickedPlayers(False))
        self.changeTeamNamePlayers()
        if len(ActiveUser.teams) > 0:
            self.insert_rows_for_players()
        self.ui.playersTable.clicked.connect(lambda: self.open_link())
        ### STACKED PAGES NAVIGATION
        if len(ActiveUser.teams)==0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_fav)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_standings)

        if len(ActiveUser.teams) > 0:
            self.ui.buttGames.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_games))
            self.ui.buttNews.clicked.connect(lambda: self.when_clicked_news())
            self.ui.buttStand.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_standings))
            self.ui.buttSett.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
            self.ui.buttStats.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_stats))
            self.ui.butFavt.clicked.connect(lambda: self.when_fav_teams_page())
        self.ui.buttSett.clicked.connect(lambda: self.logout())
        self.ui.confFavTeamsButt.clicked.connect(lambda: self.save_choices())
        if len(ActiveUser.teams) > 0:
            self.insert_rows()
        self.ui.NewsNextButt.clicked.connect(lambda: self.buttClickedNews(True))
        self.ui.NewsPrevButt.clicked.connect(lambda: self.buttClickedNews(False))
        self.changeTeamNameNews()
        self.configNews(0)
        self.ui.artlink1.clicked.connect(lambda: self.buttons_clickers(0))
        self.ui.artlink2.clicked.connect(lambda: self.buttons_clickers(1))
        self.ui.artlink3.clicked.connect(lambda: self.buttons_clickers(2))
        self.ui.artlink4.clicked.connect(lambda: self.buttons_clickers(3))
        self.ui.artlink5.clicked.connect(lambda: self.buttons_clickers(4))

    def logout(self):
        ActiveUser.NAME = ''
        ActiveUser.teams = []
        ActiveUser.currentIt = 0
        ActiveUser.newstable = []
        ActiveUser.day_diff = 0
        ActiveUser.matches = []
        ActiveUser.clear()
        self.destroy()
        self.ui.MatchesTable.destroy()
        signin = SignInWindow()
        self.close()
    def when_clicked_news(self):
        self.changeTeamNameNews()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_news)
    def button_date_clicked(self,isfur):
        ActiveUser.changeDaydiff(isfur)
        self.ui.dateLabel.setText(ActiveUser.getSelectedDay())
        self.insert_rows_for_games()
    def buttons_clickers(self, number):
        self.openBrowserWithLink(ActiveUser.newstable[ActiveUser.currentIt][number][1])
    def buttClickedNews(self, isnext):
        ActiveUser.changeIt(isnext)
        self.changeTeamNameNews()
    def buttClickedPlayers(self,isnext):
        ActiveUser.changeIt(isnext)
        self.changeTeamNamePlayers()

    def openBrowserWithLink(self,link):
        driver = webdriver.Chrome(PATH)
        driver.get(link)

    def changeTeamNameNews(self):
        if len(ActiveUser.teams)==0:
            self.ui.teamNameNews.setText('No team selected.')
        else:
            self.ui.teamNameNews.setText(ActiveUser.teams[ActiveUser.currentIt])
            self.configNews(ActiveUser.currentIt)
    def changeTeamNamePlayers(self):
        if len(ActiveUser.teams) == 0:
            self.ui.teamNamePlayers.setText('No team selected.')
        else:
            self.ui.teamNamePlayers.setText(ActiveUser.teams[ActiveUser.currentIt])
            self.insert_rows_for_players()

    def when_fav_teams_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_fav)
        self.set_checked_if_ness()
    def test(self):
        self.ui.teamNameNews.setText("test")

    def configNews(self, i):
        if len(ActiveUser.newstable)>0:
            print(ActiveUser.newstable[i])
            img = self.get_image_for_label(ActiveUser.newstable[i][0][2])
            self.ui.article1.setText(ActiveUser.newstable[i][0][0])
            self.ui.article2.setText(ActiveUser.newstable[i][1][0])
            self.ui.article3.setText(ActiveUser.newstable[i][2][0])
            self.ui.article4.setText(ActiveUser.newstable[i][3][0])
            self.ui.article5.setText(ActiveUser.newstable[i][4][0])
            self.ui.logoNews1.setText('')
            self.ui.logoNews1.setPixmap(img)
            self.ui.logoNews1.setScaledContents(True)
            self.ui.logoNews1.setMaximumSize(50,50)
            self.ui.logoNews2.setText('')
            self.ui.logoNews2.setPixmap(img)
            self.ui.logoNews2.setScaledContents(True)
            self.ui.logoNews2.setMaximumSize(50, 50)
            self.ui.logoNews3.setText('')
            self.ui.logoNews3.setPixmap(img)
            self.ui.logoNews3.setScaledContents(True)
            self.ui.logoNews3.setMaximumSize(50, 50)
            self.ui.logoNews4.setText('')
            self.ui.logoNews4.setPixmap(img)
            self.ui.logoNews4.setScaledContents(True)
            self.ui.logoNews4.setMaximumSize(50, 50)
            self.ui.logoNews5.setText('')
            self.ui.logoNews5.setPixmap(img)
            self.ui.logoNews5.setScaledContents(True)
            self.ui.logoNews5.setMaximumSize(50, 50)


    def insert_rows_for_games(self):
        counter=0
        matches_to_insert=list()

        for i in ActiveUser.matches:
            if i.time==ActiveUser.getDayMatchFormat():
                matches_to_insert.append(i)
                counter+=1
        self.ui.MatchesTable.setRowCount(counter)
        if counter==0:
            self.ui.infoNoMatches.setText('No matches for selected date.')
            self.ui.MatchesTable.setColumnCount(0)
        else:
            self.ui.infoNoMatches.setText('')
            conn = sqlite3.connect('nba.db')
            c = conn.cursor()
            counter=0
            self.ui.MatchesTable.setColumnCount(8)
            for i in matches_to_insert:
                t1=c.execute("SELECT abb FROM teams WHERE name=?",(i.team_home,))
                labbt1 = t1.fetchone()
                abbt1=str(labbt1[0])
                t2=c.execute("SELECT abb FROM teams WHERE name=?",(i.team_away,))
                labbt2 = t2.fetchone()
                abbt2=str(labbt2[0])
                img1 = self.get_proper_image_for_games(abbt1)
                img2 = self.get_proper_image_for_games(abbt2)
                self.ui.MatchesTable.setItem(counter,0,QtWidgets.QTableWidgetItem(i.hour + '     '))
                self.ui.MatchesTable.setCellWidget(counter,1,img1)
                self.ui.MatchesTable.setItem(counter,2,QtWidgets.QTableWidgetItem(i.team_home+'  '))
                self.ui.MatchesTable.setItem(counter, 3, QtWidgets.QTableWidgetItem(i.scoreshome))
                self.ui.MatchesTable.setItem(counter,4,QtWidgets.QTableWidgetItem(':'))
                self.ui.MatchesTable.setItem(counter, 5, QtWidgets.QTableWidgetItem(i.scoresaway))
                self.ui.MatchesTable.setItem(counter,6,QtWidgets.QTableWidgetItem(i.team_away))
                self.ui.MatchesTable.setCellWidget(counter, 7, img2)
                self.ui.MatchesTable.setRowHeight(counter,80)
                counter+=1
            self.ui.MatchesTable.resizeColumnsToContents()

    def insert_rows_for_players(self):
        self.ui.playersTable.setEditTriggers(QtWidgets.QTreeView.NoEditTriggers)
        self.ui.playersTable.horizontalHeader().setVisible(True)
        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        tplayers = c.execute("SELECT playername, position, age, ht, wt, college, salary FROM players WHERE team=?",
                             (ActiveUser.teams[ActiveUser.currentIt],))
        players=tplayers.fetchall()
        counter = 0
        self.ui.playersTable.setColumnCount(7)
        self.ui.playersTable.setRowCount(len(players))
        for i in players:
            for j in range(0,len(i)):
                    self.ui.playersTable.setItem(counter,j,QtWidgets.QTableWidgetItem(str(i[j])))

            counter+=1
        self.ui.playersTable.resizeColumnsToContents()
        conn.close()


    def open_link(self):
        rows=self.ui.playersTable.selectedItems()
        plname=rows[0].text()
        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        c.execute("SELECT link FROM players WHERE team=? AND playername=?",(ActiveUser.teams[ActiveUser.currentIt],plname))
        currlink = c.fetchone()
        if currlink!=None:
            driver = webdriver.Chrome(PATH)
            driver.get(currlink[0])


    def insert_rows(self):
        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        teams_names = c.execute("SELECT name FROM standings ORDER BY position")
        teams_names2 = teams_names.fetchall()
        result2=c.execute("SELECT * FROM standings ORDER BY position")
        result=result2.fetchall()
        counter = 0
        for i in result:
            for j in range(0,(len(i)+1)):
                if j==0:
                    self.ui.tableWidget.setItem(counter, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                elif j==1:
                    t_name = str(teams_names2[counter][0])
                    t_abb = c.execute("SELECT abb FROM teams WHERE name=?",(t_name,))
                    abb = str(t_abb.fetchone()[0])
                    img = self.get_proper_image(abb)
                    self.ui.tableWidget.setCellWidget(counter, 1, img)
                else:
                    self.ui.tableWidget.setItem(counter,j,QtWidgets.QTableWidgetItem(str(i[j-1])))
            counter += 1
        conn.close()
        self.ui.tableWidget.horizontalHeader().setVisible(True)
        self.ui.tableWidget.resizeColumnsToContents()

    def get_image_for_label(self,abb):
        pixmap = QPixmap()
        abb2 = 'images/' + abb.lower() + '.png'
        pixmap.load(abb2)
        pixmap.scaled(50,50)
        return pixmap
    def get_proper_image(self,abb):
        pixmap = QPixmap()
        abb = 'images/'+abb.lower()+'.png'
        pixmap.load(abb)
        pixmap.scaled(50,50)
        image = QtWidgets.QLabel(self.centralWidget())
        image.setText("")
        image.setScaledContents(True)
        image.setPixmap(pixmap)
        image.setMaximumHeight(50)
        image.setMaximumWidth(50)
        return image
    def get_proper_image_for_games(self,abb):
        pixmap = QPixmap()
        abb = 'images/' + abb.lower() + '.png'
        pixmap.load(abb)
        pixmap.scaled(60, 60)
        image = QtWidgets.QLabel(self.centralWidget())
        image.setText("")
        image.setScaledContents(True)
        image.setPixmap(pixmap)
        image.setMaximumHeight(60)
        image.setMaximumWidth(60)
        return image
    def save_choices(self):
        ActiveUser.currentIt=0
        usname = ActiveUser.NAME
        conn = sqlite3.connect('nba.db')
        c = conn.cursor()
        c.execute("DELETE FROM favteams WHERE username=?",(usname,))
        conn.commit()
        conn.close()

        c = sqlite3.connect('nba.db')
        if self.ui.clepick.isChecked():
            self.new_choice('Cleveland Cavaliers',c)
        if self.ui.orlpick.isChecked():
            self.new_choice('Orlando Magic',c)
        if self.ui.indpick.isChecked():
            self.new_choice('Indiana Pacers',c)
        if self.ui.atlpick.isChecked():
            self.new_choice('Atlanta Hawks',c)
        if self.ui.nopick.isChecked():
            self.new_choice('New Orleans Pelicans',c)
        if self.ui.lacpick.isChecked():
            self.new_choice('LA Clippers',c)
        if self.ui.phipick.isChecked():
            self.new_choice('Philadelphia 76ers',c)
        if self.ui.phxpic.isChecked():
            self.new_choice('Phoenix Suns',c)
        if self.ui.utahpick.isChecked():
            self.new_choice('Utah Jazz',c)
        if self.ui.porpick.isChecked():
            self.new_choice('Portland Trail Blazers',c)
        if self.ui.sacpick.isChecked():
            self.new_choice('Sacramento Kings',c)
        if self.ui.minpick.isChecked():
            self.new_choice('Minnesota Timberwolves',c)
        if self.ui.sapick.isChecked():
            self.new_choice('San Antonio Spurs',c)
        if self.ui.bknpick.isChecked():
            self.new_choice('Brooklyn Nets',c)
        if self.ui.lalpick.isChecked():
            self.new_choice('Los Angeles Lakers',c)
        if self.ui.miapick.isChecked():
            self.new_choice('Miami Heat',c)
        if self.ui.okcpick.isChecked():
            self.new_choice('Oklahoma City Thunder',c)
        if self.ui.nypick.isChecked():
            self.new_choice('New York Knicks',c)
        if self.ui.bospick.isChecked():
            self.new_choice('Boston Celtics',c)
        if self.ui.milpick.isChecked():
            self.new_choice('Milwaukee Bucks',c)
        if self.ui.dalpick.isChecked():
            self.new_choice('Dallas Mavericks',c)
        if self.ui.mempick.isChecked():
            self.new_choice('Memphis Grizzlies',c)
        if self.ui.chapick.isChecked():
            self.new_choice('Charlotte Hornets',c)
        if self.ui.denpick.isChecked():
            self.new_choice('Denver Nuggets',c)
        if self.ui.gspick.isChecked():
            self.new_choice('Golden State Warriors',c)
        if self.ui.torpick.isChecked():
            self.new_choice('Toronto Raptors',c)
        if self.ui.houpick.isChecked():
            self.new_choice('Houston Rockets',c)
        if self.ui.detpick.isChecked():
            self.new_choice('Detroit Pistons',c)
        if self.ui.wshpick.isChecked():
            self.new_choice('Washington Wizards',c)
        if self.ui.chipick.isChecked():
            self.new_choice('Chicago Bulls',c)
        c.commit()
        c.close()
        ActiveUser.updateteams()
        print(ActiveUser.teams)
        self.set_checked_if_ness()
        signin = SignInWindow()
        self.close()

    def new_choice(self,team,conn):
        un = ActiveUser.NAME
        cur = conn.cursor()
        cur.execute("INSERT INTO favteams values(?,?)",(un,team))

    def set_checked_if_ness(self):
        self.ui.clepick.setChecked(ActiveUser.teams.__contains__('Cleveland Cavaliers'))
        self.ui.orlpick.setChecked(ActiveUser.teams.__contains__('Orlando Magic'))
        self.ui.indpick.setChecked(ActiveUser.teams.__contains__('Indiana Pacers'))
        self.ui.atlpick.setChecked(ActiveUser.teams.__contains__('Atlanta Hawks'))
        self.ui.nopick.setChecked(ActiveUser.teams.__contains__('New Orleans Pelicans'))
        self.ui.lacpick.setChecked(ActiveUser.teams.__contains__('LA Clippers'))
        self.ui.phipick.setChecked(ActiveUser.teams.__contains__('Philadelphia 76ers'))
        self.ui.phxpic.setChecked(ActiveUser.teams.__contains__('Phoenix Suns'))
        self.ui.utahpick.setChecked(ActiveUser.teams.__contains__('Utah Jazz'))
        self.ui.porpick.setChecked(ActiveUser.teams.__contains__('Portland Trail Blazers'))
        self.ui.sacpick.setChecked(ActiveUser.teams.__contains__('Sacramento Kings'))
        self.ui.minpick.setChecked(ActiveUser.teams.__contains__('Minnesota Timberwolves'))
        self.ui.sapick.setChecked(ActiveUser.teams.__contains__('San Antonio Spurs'))
        self.ui.bknpick.setChecked(ActiveUser.teams.__contains__('Brooklyn Nets'))
        self.ui.lalpick.setChecked(ActiveUser.teams.__contains__('Los Angeles Lakers'))
        self.ui.miapick.setChecked(ActiveUser.teams.__contains__('Miami Heat'))
        self.ui.okcpick.setChecked(ActiveUser.teams.__contains__('Oklahoma City Thunder'))
        self.ui.nypick.setChecked(ActiveUser.teams.__contains__('New York Knicks'))
        self.ui.bospick.setChecked(ActiveUser.teams.__contains__('Boston Celtics'))
        self.ui.milpick.setChecked(ActiveUser.teams.__contains__('Milwaukee Bucks'))
        self.ui.dalpick.setChecked(ActiveUser.teams.__contains__('Dallas Mavericks'))
        self.ui.mempick.setChecked(ActiveUser.teams.__contains__('Memphis Grizzlies'))
        self.ui.chapick.setChecked(ActiveUser.teams.__contains__('Charlotte Hornets'))
        self.ui.denpick.setChecked(ActiveUser.teams.__contains__('Denver Nuggets'))
        self.ui.gspick.setChecked(ActiveUser.teams.__contains__('Golden State Warriors'))
        self.ui.torpick.setChecked(ActiveUser.teams.__contains__('Toronto Raptors'))
        self.ui.houpick.setChecked(ActiveUser.teams.__contains__('Houston Rockets'))
        self.ui.detpick.setChecked(ActiveUser.teams.__contains__('Detroit Pistons'))
        self.ui.wshpick.setChecked(ActiveUser.teams.__contains__('Washington Wizards'))
        self.ui.chipick.setChecked(ActiveUser.teams.__contains__('Chicago Bulls'))

if __name__ == '__main__':
    #database_config.update_standings()
    #database_config.create_table_players()
    #database_config.insert_players()

    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("SELECT * FROM players WHERE team=?",('New York Knicks',))
    rx = c.fetchall()
    #print(rx)
    c.execute("SELECT * FROM users")
    r1 = c.fetchall()
    #print(r1)
    app = QtWidgets.QApplication(sys.argv)
    window = SignInWindow()
    sys.exit(app.exec_())


    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    list = list()
    name1= 'New York Knicks'
    name2= 'Cleveland Cavaliers'
    list.append(name1)
    list.append(name2)
    for name in list:
        c.execute("SELECT abb FROM teams WHERE name=?",(name,))
        odp=c.fetchone()
        for i in odp:
            print(i)

    teamsinfo.nba_teams_data_run()
    #print(NBATeams.teams[0].getName())

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

    driver = webdriver.Chrome(PATH)
    driver.get('https://www.flashscore.pl/koszykowka/usa/nba/')
    teams = driver.find_elements_by_class_name("event__participant")
    scores = driver.find_elements_by_class_name("event__score")
    #for i in teams:
    #    print(i.text)
    #for i in scores:
    #    print(i.text)
    driver.get('https://www.espn.com/nba/scoreboard')

    teams2 = driver.find_elements_by_class_name("sb-team-short")
    points = driver.find_elements_by_class_name("total")
    for i in teams2:
        print(i.text)
        print()

    for i in points:
        print(i.text)

    driver.get("https://bleacherreport.com/new-york-knicks")
    news = driver.find_elements_by_class_name("atom.articleTitle")
    x=0
    for i in news:
        links = driver.find_element(By.PARTIAL_LINK_TEXT, i.text)
        if x==0:
            links.click()
        x+=1

    for i in news:
        print(i.text)



    driver.get('https://www.flashscore.pl/koszykowka/usa/nba/tabela/')
    tabela = driver.find_elements_by_class_name("rowCellParticipant")
    for i in tabela:
        print(i.text)
    driver.quit()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
