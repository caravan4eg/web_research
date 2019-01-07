from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:  # server's response == 200
        return r.text
    else:
        return r.status_code


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', class_='projects-table projects-table_catalogue').find('tbody').find_all('tr', class_='projects-table__row ')
    print(len(trs))
    cnt = 0

    for tr in trs:
        tds = tr.find_all('td')

        try:
            name = tds[0].find('div', class_='projects-table__textlines').find('a').text.strip()
        except:
            name = ''

        try:
            url = tds[0].find('div', class_='projects-table__textlines').find('a').get('href')
        except:
            url = ''

        try:
        	v = tds[1].find('span', class_='projects-table__textline').text.strip()
        	visits = v.replace(' ', '')
        except:
        	s, visits = ''

        try:
        	l = tds[2].find('span', class_='projects-table__textline').text.strip()
        	looks = l.replace(' ', '')
        except:
        	l, looks = ''

        try:
        	p = tds[3].find('span', class_='projects-table__textline').text.strip()
        	popularity= p.replace(' ', '')
        except:
        	p, popularity = ''

        cnt += 1
        print(f'{cnt}. {name}, {url} (visits:{visits}, views:{looks}, popularity: {popularity})')

        data = {'name': name,
        		'url': url,
        		'visits': visits,
        		'views': looks,
        		'popularity': popularity
        		}
        write_csv(data)



def write_csv(data):
    with open('mrca_4.1.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
        				 data['url'],
        				 data['visits'],
        				 data['views'],
        				 data['popularity']
        				 ))


def main():
    pattern = 'https://top100.rambler.ru/navi/?range=day&statord=0&cat_open=0&rgn=0&theme=1050&page={}'

    for i in range(1, 303):
    	url = pattern.format(str(i))
    	get_page_data(get_html(url))



if __name__ == '__main__':
    main()
