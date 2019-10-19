import requests
from bs4 import BeautifulSoup

# Table entry where we want to stop collecting data
LIMIT = 120

# Collect All-NBA history
page = requests.get('https://www.basketball-reference.com/awards/all_league.html')
anba = BeautifulSoup(page.text, 'html.parser')

pg_tbl = anba.find(id='awards_all_league')
data = pg_tbl.select('tbody tr')[:LIMIT]

# Set of players who got All-NBA honors
players = set()
valid_keys = [str(i) for i in range(1, 16)]
for row in data:
    for col in row:
        if col['data-stat'] in valid_keys:
            players.add(col.getText()[:-2])

