import csv
from peewee import *


# Connect to a Postgres database.
db = PostgresqlDatabase(database='test', user='postgres',
                        password='3650700', host='localhost')


class Coin(Model):
    name = CharField(max_length=255)
    url = TextField()
    price = CharField()
    change = CharField()

    class Meta:
        database = db


def main():
    # establish link to database
    db.connect()
    # create tables in db
    db.create_tables([Coin])

    print('Start reading from csv file...')
    with open('cmc_pages_4.2.csv') as f:
        order = ['name', 'price', 'change', 'url']
        reader = csv.DictReader(f, fieldnames=order)
        coins = list(reader)

        print('Start writing to database...')
        # V1: first slow example
        # for row in coins:
            # create object of class Coin (экземпляр класса Coin)
            # coin = Coin(name=row['name'], url=row['url'], price=row['price'], change=row['change'])
            # coin.save()


        with db.atomic():
            # V2 with transactions
            # for row in coins:
            #     Coin.create(**row)

            # V3 with index and slices
            for index in range(0, len(coins), 100):
                Coin.insert_many(coins[index:index+100]).execute()


if __name__ == '__main__':
    main()
