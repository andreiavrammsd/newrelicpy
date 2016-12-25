import csv
from app import config
from pathlib import Path
from shutil import copy

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

def setup():
    db = Path(db_file)

    if not db.is_file():
        copy(config.get('db_file_template'), db_file)
