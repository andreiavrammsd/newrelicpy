#!/usr/bin/python3.4

import sys
import re
import time
import validation
import backup
import db

db_file = 'newrelic.csv'


def parse_input(data):
    return re.findall(r'([\d\.]+)', data)


def set_time(result):
    when = time.strftime('%Y-%m-%d %H:%M:%S')
    result.insert(0, when)


def print_new_line(result):
    print(', '.join(result))


def main():
    data = sys.argv[1]
    result = parse_input(data)

    validation.validate(result)

    set_time(result)

    backup.save(db_file)
    db.insert(db_file, result)
    backup.save(db_file)

    print_new_line(result)

if __name__ == '__main__':
    main()
