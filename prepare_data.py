from draft import Draft
from all_nba import players

BEGIN_YEAR = 1990
END_YEAR = 1990

database = []
for i in range(BEGIN_YEAR, END_YEAR+1):
    print("Collecting data for:", i)
    for p in Draft(i).get_draftees():
        database.append(p.get_stats())

for s in database:
    print(s)