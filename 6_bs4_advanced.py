from bs4 import BeautifulSoup
import re

# .find
# .find_all

# tag div and next attribute class or id and its name
# {'data-set': 'salary'}) for complex attributes
# like here: <div data-set="salary">

# .parent
# .find_parent
# .parents
# .find_parents

# .find_next_sibling()
# .find_previous_sibling()

# filter function regular expressions \d{1,9}
# re.findall(pattern, where)[0]
# re.search(pattern, where).group()
# soup.find_all('div', text=re.compile('\d{1,9}'))

def get_copywriter(person):
    whois = person.find('div', id = 'whois').text.strip()
    if 'Copywriter' in whois:
        return person
    return None

def get_salary(s):
    # we want to get clear digit from this "salary: 2700 usd per month"

    pattern = r'\d{1,9}'
    # salary = re.findall(pattern, s)[0]
    salary = re.search(pattern, s).group()
    print(salary)


def main():
    file = open('index.html').read()

    soup = BeautifulSoup(file, 'lxml')
    row_first = soup.find('div', class_='row')
    row_all = soup.find_all('div', {'class': 'row'})
    data_set = soup.find_all('div', {'data-set': 'salary'})
    # print(row_first)
    # print('****************\n')
    # print(row_all)
    # print('****************\n')
    # print(data_set, '\n')

    # << parent  >>
    # so we found that div "row" which is parent for Petr
    petr = soup.find('div', text = 'Petr').parent
    # print(petr)

    # .parent
    # so we will find closest parent: <div class="name1">
    alena = soup.find('div', text = 'Alena').parent

    # .find_parent
    # so we'll find needed class: <div class="row">
    alena = soup.find('div', text='Alena').find_parent(class_='row')

    # we have two copywriters among all tags we want to find
    # tags with copywriters
    # let's find them all: we'll filter them
    copywriters = []
    persons = soup.find_all('div', class_='row')
    for person in persons:
        cw = get_copywriter(person)
        if cw:
            copywriters.append(cw)

    print(copywriters)


    # let's find all salary: tags
    salary = soup.find_all('div', {'data-set': 'salary'})
    for i in salary:
        get_salary(i.text.strip())


    salary = soup.find_all('div', text=re.compile('\d{1,9}'))
    for i in salary:
        print(i.text.strip())


    # ^ - beginning of string
    # $ - end of string
    # . - any symbol
    # + - unlimited number of entries
    # '\d' - digit
    # '\w' - letters, digits, "_"
    # for find twitter
    # re'^@\w+'
    # will find





if __name__ == '__main__':
    main()




