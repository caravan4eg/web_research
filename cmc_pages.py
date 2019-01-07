import requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)
        return r.status_code


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')

        try:
            name = tds[1].find('a', class_='currency-name-container').text.strip()
        except:
            name = ''

        try:
            url = 'https://coinmarketcap.com' + tds[1].find('a', class_='currency-name-container').get('href')
        except:
            url = ''

        try:
            price = tds[3].find('a').get('data-usd').strip()
        except:
            price = ''

        try:
            change = tds[6].text.strip()
            print(name, change)
        except:
            change = ''


        data = {'name': name,
                'url': url,
                'price': price,
                'change': change}

        write_csv(data)


def write_csv(data):
    with open('cmc_pages_4.2.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['price'],
                         data['change'],
                         data['url']
                         ))



def main():
    url = 'https://coinmarketcap.com/'

    while True:
        # get html, get page data and write to csv file
        get_page_data(get_html(url))

        # get list (soup) of page objects
        soup = BeautifulSoup(get_html(url), 'lxml')
        '''
        Find there url as text of Next page button = 2,3...35
        Final url is concatenation of 'https://coinmarketcap.com/' and number this button and looks like https://coinmarketcap.com/2
        I'm looking for this number on button with word "Next"
        '''
        try:
            pattern = 'Next'
            url = 'https://coinmarketcap.com/' + soup.find('ul', class_='pagination').find('a', text = re.compile(pattern)).get('href')
        except:
            break




if __name__ == '__main__':
    main()
