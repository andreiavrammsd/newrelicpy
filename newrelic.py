#!/usr/bin/python3.4

import sys
import reader
import data
import validation
import backup
import db

db_file = 'newrelic.csv'


def print_new_line(result):
    print(', '.join(result))


def main():
    input_data = reader.read(sys.argv[1])
    validation.validate(input_data)
    data.add_time(input_data)

    backup.save(db_file)
    db.insert(db_file, input_data)
    backup.save(db_file)

    print_new_line(input_data)

if __name__ == '__main__':
    main()
