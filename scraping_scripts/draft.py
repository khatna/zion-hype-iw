import requests
import all_nba
from player import Player
from bs4 import BeautifulSoup

baseurl_bb = 'https://www.basketball-reference.com/'

class Draft:
    def __init__(self, year):
        page = requests.get(baseurl_bb + 'draft/NBA_' + str(year) + '.html')
        draft = BeautifulSoup(page.text, 'html.parser')

        draft_tbl = draft.find(id='stats')
        players_tbl = draft_tbl.select('tbody tr')[:20]

        players_pre = {}
        name = ''
        pick = ''
        age = ''
        for player in players_tbl:
            for col in player.select('td'):
                if col['data-stat'] == 'player':
                    name = col.getText()
                    try: 
                        bio_page = requests.get(baseurl_bb + col.findChildren('a')[0]['href'])
                        bio = BeautifulSoup(bio_page.text, 'html.parser')
                        birth = bio.find(id="necro-birth")['data-birth'][:4]
                        age = str(int(year)-int(birth))
                    except:
                        print('Difficulty finding age for: ' + name)
                elif col['data-stat'] == 'pick_overall':
                    pick = col.getText()
                elif col['data-stat'] == 'college_name':
                    college = col.getText()

            players_pre[name] = [pick, age, college]

        self.players = [Player(p, v[0], v[1]) for p, v in players_pre.items() if v[2] != '']

    # Get the draft picks of given year as Player objects
    def get_draftees(self):
        return self.players
