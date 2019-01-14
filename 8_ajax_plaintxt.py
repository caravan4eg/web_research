import csv
import requests
import time


def get_html(url):
    try:
        r = requests.get(url)
        if r.ok:
            print(f'Everything is OK. Status code: {r.status_code}')
            return r.text
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"
        print(f'Attention, Status code: {r.status_code}')
        time.sleep(5)
        return None


def write_csv(data):
    with open('8_websites.csv', 'a') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def main():
    cnt = 0
    for i in range(0, 2500): # 6666+1
        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
        response = get_html(url)
        data = response.strip().split('\n')[1:]

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
            if cnt % 100 == 0:
                print('Delay...')
                time.sleep(2)
    print('Finish!')





if __name__ == "__main__":
    main()
