import csv
from app import config

db_file = config.get('db_file')


def insert(line: list):
    with open(db_file, 'a+', newline='\n') as db:
        writer = csv.writer(db, delimiter=',')
        writer.writerow(line)


def select() -> list:
    with open(db_file, 'r', newline='\n') as db:
        reader = csv.reader(db)
        rows = list(reader)

    return rows
