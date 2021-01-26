import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from main import ActiveUser, PATH
BleacherLink = 'https://bleacherreport.com/'

# Download article titles
Matches = list()
class Match:
    def __init__(self,teamhome,teamaway,shome,saway,t,h):
        self.team_home=teamhome
        self.team_away=teamaway
        self.scoreshome=shome
        self.scoresaway=saway
        self.time=t
        self.hour=h
    def __str__(self):
        res = self.time + '   ' + self.team_home + ' ' + self.scoreshome + ':' + self.scoresaway + ' ' + self.team_away
        return res
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
    driver.close()

def get_matches(act_teams):
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(PATH,options=opt)
    driver.get('https://www.flashscore.pl/koszykowka/usa/nba/wyniki/')
    teamshome = driver.find_elements_by_class_name("event__participant.event__participant--home")
    teamsaway = driver.find_elements_by_class_name("event__participant.event__participant--away")
    homescores = driver.find_elements_by_class_name('event__score.event__score--home')
    awayscores = driver.find_elements_by_class_name('event__score.event__score--away')
    matchdate = driver.find_elements_by_class_name('event__time')
    for i in range(0,len(teamshome)):
        time =matchdate[i].text[0:5]
        hour =matchdate[i].text[7:11]
        if len(hour)<5:
            hour+='0'
        if act_teams.__contains__(teamshome[i].text) or act_teams.__contains__(teamsaway[i].text):
            Matches.append(Match(teamshome[i].text,teamsaway[i].text,homescores[i].text,awayscores[i].text,time,hour))

    driver.get('https://www.flashscore.pl/koszykowka/usa/nba/spotkania/')
    teamshome2 = driver.find_elements_by_class_name("event__participant.event__participant--home")
    teamsaway2 = driver.find_elements_by_class_name("event__participant.event__participant--away")
    matchdate2 = driver.find_elements_by_class_name('event__time')
    for i in range(0,len(matchdate2)):
        time = matchdate2[i].text[0:5]
        hour = matchdate2[i].text[7:12]
        if len(hour)<5:
            hour+='0'
        if act_teams.__contains__(teamshome2[i].text) or act_teams.__contains__(teamsaway2[i].text):
            Matches.append(Match(teamshome2[i].text,teamsaway2[i].text,'0','0',time,hour))
    driver.close()
    return Matches

