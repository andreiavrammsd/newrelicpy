#!/usr/bin/python3.4

import sys
import re
import time
import csv

db_file = 'newrelic.csv'


def parse_input(data):
    return re.findall(r'([\d\.]+)', data)


def set_time(result):
    when = time.strftime('%Y-%m-%d %H:%M:%S')
    result.insert(0, when)


def write_line_to_db(result):
    with open(db_file, 'a+', newline='\n') as db:
        writer = csv.writer(db, delimiter=',')
        writer.writerow(result)


def print_new_line(result):
    print(', '.join(result))


def main():
    data = sys.argv[1]
    result = parse_input(data)
    set_time(result)
    write_line_to_db(result)
    print_new_line(result)

if __name__ == '__main__':
    main()
