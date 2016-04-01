#!/usr/bin/python3.4

import sys
import time
import reader
import validation
import backup
import db

db_file = 'newrelic.csv'


def set_time(result):
    when = time.strftime('%Y-%m-%d %H:%M:%S')
    result.insert(0, when)


def print_new_line(result):
    print(', '.join(result))


def main():
    input_data = reader.read(sys.argv[1])
    validation.validate(input_data)

    set_time(input_data)

    backup.save(db_file)
    db.insert(db_file, input_data)
    backup.save(db_file)

    print_new_line(input_data)

if __name__ == '__main__':
    main()
