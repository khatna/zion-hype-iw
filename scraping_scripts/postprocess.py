import csv

pre = open('data_pre.csv', 'r')
post = open('data.csv', 'w')

writer = csv.writer(post, delimiter=',')
reader = csv.reader(pre, delimiter=',')

for row in reader:
    height = float(row[10])
    weight = float(row[11])
    woh = weight/height
    row[10] = str(round(woh,2))
    del row[11]
    writer.writerow(row)

pre.close()
post.close()