import unicodecsv as csv
import logging

n_split = 100000
url_list = []
count = 0
u = 0


f = open('Parakike.csv', 'rU')
reader = csv.reader(f, delimiter=',', encoding='utf-8')
logging.basicConfig(filename='log_split_csv.log', level=logging.INFO)
for row in reader:
    for res in row:
        count += 1
        url_list.append(res)
        print url_list
        logging.info('Url leida num: %d' % (count))
        if count == n_split:
            u += 1
            with open('result%d.csv' % (u), 'wb') as n:
                writer = csv.writer(n, encoding='utf-8')
                writer.writerow(url_list)
                del url_list[:]
                count = 0
                logging.info('csv de 100.000 urls creado')





