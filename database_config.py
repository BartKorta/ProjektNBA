import sqlite3
PATH = "C:\Program Files\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ESPN_LINK='https://www.espn.com/nba/team/roster/_/name/'
# Create new table which contains NBA Teams basic information
def create_table_teams():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("""DROP TABLE teams""")
    c.execute("""CREATE TABLE teams (
                                    name text,
                                    abb text,
                                    color integer,
                                    brlink text
                                    )""")
    conn.commit()
    conn.close()

# Create new table which contains users credentials
def create_table_users():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE users (
                                    username text,
                                    password text)""")
    conn.commit()
    conn.close()

# Create new table which contains users fav NBA teams choices
def create_table_favteams():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE favteams (
                                        username text,
                                        team text)""")
    conn.commit()
    conn.close()
def create_table_players():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("""DROP TABLE players""")
    c.execute("""CREATE TABLE players (
                                            team text,
                                            playername text,
                                            position text,
                                            age text,
                                            ht text,
                                            wt text,
                                            college text,
                                            salary text,
                                            link text)""")
    conn.commit()
    conn.close()
# Create new table which contains rows of NBA teams stats in current season
def create_table_standings():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE standings (
                                        position integer,
                                        name text,
                                        w text,
                                        l text,
                                        pct text,
                                        gb text,
                                        home text,
                                        away text,
                                        div text,
                                        conf text,
                                        ppg text,
                                        oppg text,
                                        diff text,
                                        strk text,
                                        l10 text
                                        )""")
    conn.commit()
    conn.close()

def insert_players():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    driver = webdriver.Chrome(PATH)
    c.execute("SELECT name,abb FROM teams")
    tna = c.fetchall()
    for j in tna:
        if j[0]!='Los Angeles Clippers':
            link=ESPN_LINK+j[1].lower()
            driver.get(link)
            namesx = driver.find_elements_by_class_name('inline')
            counter = 0
            for i in range(0,len(namesx)):
                if counter.__mod__(8) == 1:
                    if namesx!='':
                        num = (namesx[i].text[len(namesx[i].text) - 1])
                        if str.isdigit(num):
                            num2 = namesx[i].text[len(namesx[i].text) - 2]
                            if str.isdigit(num2):
                                name=namesx[i].text[0:(len(namesx[i].text) - 2)]
                                lk=driver.find_element(By.PARTIAL_LINK_TEXT, namesx[i].text[0:(len(namesx[i].text) - 2)]).get_attribute(
                                    'href')
                                c.execute("INSERT INTO players values(?,?,?,?,?,?,?,?,?)", (
                                j[0],name,namesx[i+1].text,namesx[i+2].text,namesx[i+3].text,namesx[i+4].text,namesx[i+5].text,namesx[i+6].text,lk))

                            else:
                                name=namesx[i].text[0:(len(namesx[i].text) - 1)]
                                lk=driver.find_element(By.PARTIAL_LINK_TEXT, namesx[i].text[0:(len(namesx[i].text) - 1)]).get_attribute(
                                    'href')
                                c.execute("INSERT INTO players values(?,?,?,?,?,?,?,?,?)", (
                                    j[0], name, namesx[i + 1].text, namesx[i + 2].text, namesx[i + 3].text,
                                    namesx[i + 4].text, namesx[i + 5].text, namesx[i + 6].text, lk))
                counter += 1
    conn.commit()
    conn.close()
    print("DONE.")

# Update existing standings table , by downloading fresh data from the internet
def update_standings():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute('DELETE FROM standings;',)

    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=opt)
    driver.get('https://www.espn.com/nba/standings/_/group/league')
    standings_table = driver.find_elements_by_class_name("Table__TBODY")
    teams = standings_table[0].find_elements_by_tag_name("tr")
    rows = standings_table[1].find_elements_by_tag_name("tr")
    for i in range(0, len(teams)):
        tm = teams[i].find_element_by_tag_name("td")
        team_name = tm.text
        cells = rows[i].find_elements_by_tag_name("td")
        t = list()
        for j in cells:
            t.append(j.text)
        val =i+1
        c.execute("INSERT INTO standings values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(val, team_name, t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[9],t[10],t[11],t[12]))
    conn.commit()
    conn.close()
    driver.close()


# Manual insertion: teams info, table: teams
def insert_teams():
    conn = sqlite3.connect('nba.db')
    c = conn.cursor()
    c.execute("INSERT INTO teams VALUES('Cleveland Cavaliers','CLE',0,'cleveland-cavaliers')")
    c.execute("INSERT INTO teams VALUES('Orlando Magic', 'ORL', 0, 'orlando-magic')")
    c.execute("INSERT INTO teams VALUES('Indiana Pacers', 'IND', 0, 'indiana-pacers')")
    c.execute("INSERT INTO teams VALUES('Atlanta Hawks', 'ATL', 0, 'atlanta-hawks')")
    c.execute("INSERT INTO teams VALUES('New Orleans Pelicans', 'NO', 0, 'new-orleans-pelicans')")
    c.execute("INSERT INTO teams VALUES('LA Clippers', 'LAC', 0, 'los-angeles-clippers')")
    c.execute("INSERT INTO teams VALUES('Los Angeles Clippers','LAC',0,'los-angeles-clippers')")
    c.execute("INSERT INTO teams VALUES('Philadelphia 76ers', 'PHI', 0, 'philadelphia-76ers')")
    c.execute("INSERT INTO teams VALUES('Phoenix Suns', 'PHX', 0, 'phoenix-suns')")
    c.execute("INSERT INTO teams VALUES('Utah Jazz', 'UTAH', 0, 'utah-jazz')")
    c.execute("INSERT INTO teams VALUES('Portland Trail Blazers', 'POR', 0, 'portland-trail-blazers')")
    c.execute("INSERT INTO teams VALUES('Sacramento Kings', 'SAC', 0, 'sacramento-kings')")
    c.execute("INSERT INTO teams VALUES('Minnesota Timberwolves', 'MIN', 0, 'minnesota-timberwolves')")
    c.execute("INSERT INTO teams VALUES('San Antonio Spurs', 'SA', 0, 'san-antonio-spurs')")
    c.execute("INSERT INTO teams VALUES('Brooklyn Nets', 'BKN', 0, 'brooklyn-nets')")
    c.execute("INSERT INTO teams VALUES('Los Angeles Lakers', 'LAL', 0, 'los-angeles-lakers')")
    c.execute("INSERT INTO teams VALUES('Miami Heat', 'MIA', 0, 'miami-heat')")
    c.execute("INSERT INTO teams VALUES('Oklahoma City Thunder', 'OKC', 0, 'oklahoma-city-thunder')")
    c.execute("INSERT INTO teams VALUES('New York Knicks', 'NY', 0, 'new-york-knicks')")
    c.execute("INSERT INTO teams VALUES('Boston Celtics', 'BOS', 0, 'boston-celtics')")
    c.execute("INSERT INTO teams VALUES('Milwaukee Bucks', 'MIL', 0, 'milwaukee-bucks')")
    c.execute("INSERT INTO teams VALUES('Dallas Mavericks', 'DAL', 0, 'dallas-mavericks')")
    c.execute("INSERT INTO teams VALUES('Memphis Grizzlies', 'MEM', 0, 'memphis-grizzlies')")
    c.execute("INSERT INTO teams VALUES('Charlotte Hornets', 'CHA', 0, 'charlotte-hornets')")
    c.execute("INSERT INTO teams VALUES('Denver Nuggets', 'DEN', 0, 'denver-nuggets')")
    c.execute("INSERT INTO teams VALUES('Golden State Warriors', 'GS', 0, 'golden-state-warriors')")
    c.execute("INSERT INTO teams VALUES('Toronto Raptors', 'TOR', 0, 'toronto-raptors')")
    c.execute("INSERT INTO teams VALUES('Houston Rockets', 'HOU', 0, 'houston-rockets')")
    c.execute("INSERT INTO teams VALUES('Detroit Pistons', 'DET', 0, 'detroit-pistons')")
    c.execute("INSERT INTO teams VALUES('Washington Wizards', 'WSH', 0, 'washington-wizards')")
    c.execute("INSERT INTO teams VALUES('Chicago Bulls', 'CHI', 0, 'chicago-bulls')")
    conn.commit()