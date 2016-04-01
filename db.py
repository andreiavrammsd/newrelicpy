import csv


def insert(db_file: str, line: list):
    with open(db_file, 'a+', newline='\n') as db:
        writer = csv.writer(db, delimiter=',')
        writer.writerow(line)
