import csv
from app import config


def insert(line: list):
    db_file = config.get('db_file')

    with open(db_file, 'a+', newline='\n') as db:
        writer = csv.writer(db, delimiter=',')
        writer.writerow(line)
