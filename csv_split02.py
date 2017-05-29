import unicodecsv as csv
import logging

n_split = 100000
count = 0
u = 0


r = open('Parakike.csv', 'rU')
reader = csv.reader(r, delimiter=',', encoding='utf-8')
logging.basicConfig(filename='log_split_csv.log', level=logging.INFO)
w = open('result%d.csv' % (u), 'wb')
for row in reader:
    writer = csv.writer(w, encoding='utf-8')
    count += 1
    writer.writerow(row)
    logging.info('Url leida y copiadas num: %d' % (count))
    if count == n_split:
        u += 1
        w = open('result%d.csv' % (u), 'wb')
        logging.info('csv de 100.000 urls creado numero {}'.format(u))
        count = 0


