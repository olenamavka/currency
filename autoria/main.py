import csv
import random
import sqlite3
from time import sleep
import requests
from bs4 import BeautifulSoup


def random_sleep():
    sleep(random.randint(1, 5))


def get_page_content(page: int, size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '-1',
        'custom.not': '-1',
        'page': page,
        'size': size
    }
    base_url = 'https://auto.ria.com/uk/search/'
    response = requests.get(base_url, params=query_parameters)
    response.raise_for_status()
    return response.text


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        with open(self.filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)


class SQLWriter:
    def __init__(self, filename, header1, header2, header3):
        self.filename = filename
        self.header1 = header1
        self.header2 = header2
        self.header3 = header3

    def write(self, row: list):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        sql1 = f'''
                          CREATE TABLE IF NOT EXISTS Autoria (
                              ID INTEGER PRIMARY KEY,
                              {self.header1} varchar(255),
                              {self.header2} varchar(255),
                              {self.header3} varchar(255)
                          );
                          '''
        # The alternative variant when not using headers separately
        # self.headers as for CSVWriter in __init__ method also.
        # sql1 = f'''
        #                   CREATE TABLE IF NOT EXISTS Autoria (
        #                       ID INTEGER PRIMARY KEY,
        #                       {" varchar(255), ".join(self.headers)} varchar(255)
        #                   );
        #                   '''

        sql2 = f'''
                INSERT INTO Autoria ({self.header1}, {self.header2}, {self.header3})
                VALUES ('{row[0]}', '{row[1]}', '{row[2]}');
                '''
        #  alternatively:  INSERT INTO Autoria {self.headers}

        cur.execute(sql1)
        cur.execute(sql2)
        con.commit()
        con.close()


class StdOutWriter:

    def write(self, row: list):
        print(row)


def main():
    writers = (
        CSVWriter('cars.csv', ['car_id', 'car_link', 'price']),
        SQLWriter('cars.db', 'car_id', 'car_link', 'price'),
        # SQLWriter('cars2.db', ('car_id', 'link', 'price')),   # in alternative case
        # StdOutWriter()
    )

    page = 0

    while True:

        print(f'Page: {page}')

        page_content = get_page_content(page)

        page += 1

        soup = BeautifulSoup(page_content, features="html.parser")

        search_results = soup.find("div", {"id": "searchResults"})
        ticket_items = search_results.find_all("section", {"class": "ticket-item"})

        if not ticket_items:
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find("div", {"class": "hide"})
            car_id = car_details['data-id']
            data_link_to_view = car_details['data-link-to-view']
            auto_details = ticket_item.find("div", {"class": "content-bar"})
            link = auto_details.find("a", {"class": "m-link-ticket"})['href']

            res = requests.get(link)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, features="html.parser")
            price_value = soup.find("span", {"class": "price_value"})

            if price_value is None:
                continue

            price = price_value.text
            for writer in writers:
                writer.write([car_id, data_link_to_view, price])

        random_sleep()


if __name__ == '__main__':
    main()
