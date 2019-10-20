import csv
from draft import Draft
from all_nba import players

BEGIN_YEAR = 1990
END_YEAR = 2015

database = []
for i in range(BEGIN_YEAR, END_YEAR+1):
    print("Collecting data for:", i)
    for p in Draft(i).get_draftees():
        database.append(p.get_stats())

for p in database:
    if p[0] in players:
        p.append('1')
    else:
        p.append('0')

with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for p in database:
        filewriter.writerow(p)