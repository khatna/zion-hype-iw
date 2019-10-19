import requests
from bs4 import BeautifulSoup

# Find the draft picks of 2019 and get their basic data
page = requests.get('https://www.basketball-reference.com/draft/NBA_2019.html')
draft = BeautifulSoup(page.text, 'html.parser')

draft_tbl = draft.find(id='stats')
players_tbl = draft_tbl.select('tbody tr')[:30]

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
    players_pre[name]=[pick, college]

# Only want players who played in NCAA
players = {k:v for k, v in players_pre.items() if v[1] != ''}