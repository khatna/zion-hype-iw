import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.sports-reference.com/cbb/players/'
rel_stats_basic = ['pts_per_g', 'ast_per_g', 'trb_per_g', 'stl_per_g', 'blk_per_g', 'sos']

class Player:
    def __init__(self, name, pick):
        self.stats = [name, pick]
        format_name = name.replace(' ', '-').replace("'", '').replace('.', '').lower()
        page = requests.get(baseurl + format_name + '-1.html')
        html_doc = page.text.replace('<!--', '').replace('-->', '')
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
            basic_stats = soup.find(id='players_per_game')
            basic_stats = basic_stats.select('tbody tr')
            for stat in basic_stats[len(basic_stats) - 1]:
                if stat['data-stat'] in rel_stats_basic:
                    self.stats.append(stat.getText())

            adv_stats = soup.find(id='players_advanced').select('tbody tr')
            for stat in adv_stats[len(adv_stats) - 1]:
                if stat['data-stat'] == 'ts_pct' or stat['data-stat'] == 'fta_per_fga_pct':
                    self.stats.append(stat.getText())
        except:
            print('Difficulty finding player:', name)

    def get_stats(self):
        return self.stats
