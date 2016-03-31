#!/usr/bin/python3.4

import sys
import re
import time

db_file = 'newrelic.csv'


def parse_input(data):
    return re.findall(r'([\d\.]+)', data)


def set_time(result):
    when = time.strftime('%Y-%m-%d %H:%M:%S')
    result.insert(0, when)


def get_db_line(result):
    delimiter = ','
    return delimiter.join(result)


def write_line_to_db(line):
    db = open(db_file, 'a+')
    db.write(line + '\n')
    db.close()


def print_new_line(line):
    print(line)


def main():
    data = sys.argv[1]
    result = parse_input(data)
    set_time(result)
    line = get_db_line(result)
    write_line_to_db(line)
    print_new_line(line)

if __name__ == '__main__':
    main()
