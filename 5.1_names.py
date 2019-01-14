import csv
"""
script writes and reads csv files
"""


def write_csv(data):
    with open('names_5.1.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['surname'], data['age']))
        print(f'Member: {data}')

def write_csv_dictwriter(data):
    with open('names_5.11.csv', 'a') as f:
        order = ['age', 'name', 'surname']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def main():
    d1 = {'name': 'Jhon', 'surname': 'Middle', 'age': 32}
    d2 = {'name': 'Kate', 'surname': 'Smith', 'age': 25}
    d3 = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 19}

    group = [d1, d2, d3]

    for member in group:
        write_csv(member)
        write_csv_dictwriter(member)

    with open('cmc_pages_4.2.csv') as file:
        fieldnames = ['name', 'price', 'change', 'url']
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
