import requests
import all_nba
from player import Player
from bs4 import BeautifulSoup

baseurl_bb = 'https://www.basketball-reference.com/draft/NBA_'

class Draft:
    def __init__(self, year):
        page = requests.get(baseurl_bb + str(year) + '.html')
        draft = BeautifulSoup(page.text, 'html.parser')

        draft_tbl = draft.find(id='stats')
        players_tbl = draft_tbl.select('tbody tr')[:20]

        players_pre = {}
        name = ''
        pick = ''
        for player in players_tbl:
            for col in player.select('td'):
                if col['data-stat'] == 'player':
                    name = col.getText()
                elif col['data-stat'] == 'pick_overall':
                    pick = col.getText()
                elif col['data-stat'] == 'college_name':
                    college = col.getText()
            players_pre[name] = [pick, college]

        self.players = [Player(p, v[0]) for p, v in players_pre.items() if v[1] != '']

    # Get the draft picks of given year as Player objects
    def get_draftees(self):
        return self.players
