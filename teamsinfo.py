import sqlite3

class Team:
    def __init__(self,name,abb,color,brlink):
        self.name=name
        self.abb=abb
        self.color=color
        self.brlink=brlink
        self.espnlink=self.abb.lower()

    def getName(self):
        return self.name

    def getAbb(self):
        return self.abb

    def getColor(self):
        return self.color

    def getBrlink(self):
        return self.brlink

    def getEspnlink(self):
        return self.espnlink
class NBATeams:
    teams = list()

class TableRow:
    def __init__(self,pos,team,w,l,pct,gb,home,away,div,conf,ppg,oopppg,diff,strk,l10):
        self.pos=pos
        self.team=team
        self.w=w
        self.l=l
        self.pct=pct
        self.gb=gb
        self.home=home
        self.away=away
        self.div=div
        self.conf=conf
        self.ppg=ppg
        self.oopppg=oopppg
        self.diff=diff
        self.strk=strk
        self.l10=l10

    def get_params_to_list(self):
        l = list()
        #l.append(self.pos)
        #l.append(self.team.getName())
        #l.append(self.w)
        l.append(self.l)
        l.append(self.pct)
        l.append(self.gb)
        l.append(self.home)
        l.append(self.away)
        l.append(self.div)
        l.append(self.conf)
        l.append(self.strk)
        return l

    @staticmethod
    def add_with_list(pos,team,list):
        if len(list)==13:
            return TableRow(pos,team,list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11],list[12])
    def return_row(self):
        return str(self.pos)+' '+self.team.getName() + ' ' + self.team.getAbb() + ' ' + self.w + ' ' + self.l + ' '+self.pct

class Standing:
    table = list()

    @staticmethod
    def print_table():
        for i in Standing.table:
            print(i.return_row())

    @staticmethod
    def add_row(row):
        Standing.table.append(row)

    @staticmethod
    def getTable():
        return Standing.table


def nba_teams_data_run():

    NBATeams.teams.append(Team('Cleveland Cavaliers','CLE',0,'cleveland-cavaliers'))
    NBATeams.teams.append(Team('Orlando Magic', 'ORL', 0, 'orlando-magic'))
    NBATeams.teams.append(Team('Indiana Pacers', 'IND', 0, 'indiana-pacers'))
    NBATeams.teams.append(Team('Atlanta Hawks', 'ATL', 0, 'atlanta-hawks'))
    NBATeams.teams.append(Team('New Orleans Pelicans', 'NO', 0, 'new-orleans-pelicans'))
    NBATeams.teams.append(Team('LA Clippers', 'LAC', 0, 'los-angeles-clippers'))
    NBATeams.teams.append(Team('Philadelphia 76ers', 'PHI', 0, 'philadelphia-76ers'))
    NBATeams.teams.append(Team('Phoenix Suns', 'PHX', 0, 'phoenix-suns'))
    NBATeams.teams.append(Team('Utah Jazz', 'UTAH', 0, 'utah-jazz'))
    NBATeams.teams.append(Team('Portland Trail Blazers', 'POR', 0, 'portland-trail-blazers'))
    NBATeams.teams.append(Team('Sacramento Kings', 'SAC', 0, 'sacramento-kings'))
    NBATeams.teams.append(Team('Minnesota Timberwolves', 'MIN', 0, 'minnesota-timberwolves'))
    NBATeams.teams.append(Team('San Antonio Spurs', 'SA', 0, 'san-antonio-spurs'))
    NBATeams.teams.append(Team('Brooklyn Nets', 'BKN', 0, 'brooklyn-nets'))
    NBATeams.teams.append(Team('Los Angeles Lakers', 'LAL', 0, 'los-angeles-lakers'))
    NBATeams.teams.append(Team('Miami Heat', 'MIA', 0, 'miami-heat'))
    NBATeams.teams.append(Team('Oklahoma City Thunder', 'OKC', 0, 'oklahoma-city-thunder'))
    NBATeams.teams.append(Team('New York Knicks', 'NY', 0, 'new-york-knicks'))
    NBATeams.teams.append(Team('Boston Celtics', 'BOS', 0, 'boston-celtics'))
    NBATeams.teams.append(Team('Milwaukee Bucks', 'MIL', 0, 'milwaukee-bucks'))
    NBATeams.teams.append(Team('Dallas Mavericks', 'DAL', 0, 'dallas-mavericks'))
    NBATeams.teams.append(Team('Memphis Grizzlies', 'MEM', 0, 'memphis-grizzlies'))
    NBATeams.teams.append(Team('Charlotte Hornets', 'CHA', 0, 'charlotte-hornets'))
    NBATeams.teams.append(Team('Denver Nuggets', 'DEN', 0, 'denver-nuggets'))
    NBATeams.teams.append(Team('Golden State Warriors', 'GS', 0, 'golden-state-warriors'))
    NBATeams.teams.append(Team('Toronto Raptors', 'TOR', 0, 'toronto-raptors'))
    NBATeams.teams.append(Team('Houston Rockets', 'HOU', 0, 'houston-rockets'))
    NBATeams.teams.append(Team('Detroit Pistons', 'DET', 0, 'detroit-pistons'))
    NBATeams.teams.append(Team('Washington Wizards', 'WSH', 0, 'washington-wizards'))
    NBATeams.teams.append(Team('Chicago Bulls', 'CHI', 0, 'chicago-bulls'))


def find_team_by_name(team_name):
    for i in NBATeams.teams:
        if i.getName()==team_name:
            return i