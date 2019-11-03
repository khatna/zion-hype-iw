import csv
from draft import Draft
from all_nba import players

with open('rookies.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for p in Draft(2019).get_draftees():
        filewriter.writerow(p.get_stats())