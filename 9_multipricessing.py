import csv
import requests
from multiprocessing import Pool
from time import sleep


def get_html(url):
    sleep(1)
    r = requests.get(url)
    if r.ok:
        return r.text
    else: 
        return r.status_code


def write_csv(data):
    with open('9_sites_multiproc.csv', 'a') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(text):
    cnt = 0
    data = text.strip().split('\n')[1:]

    for row in data:
        columns = row.strip().split('\t')
        name = columns[0]
        url = columns[1]
        description = columns[2]
        traffic = columns[3]
        percent = columns[4]

        data = {'name': name,
                'url': url,
                'description': description,
                'traffic': traffic,
                'percent': percent}
        write_csv(data)
        print(f'{cnt}.')
        cnt += 1
    print('Finish!')


def make_all(url):
    text = get_html(url)
    get_page_data(text)


def main():
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 6321)]
    for url in urls:
        print(url)

    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main()
