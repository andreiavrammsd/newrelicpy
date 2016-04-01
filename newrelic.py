#!/usr/bin/python3.4

import sys
from app import reader, validation, data, backup, db, output


def main():
    if len(sys.argv) == 1:
        display()
    else:
        insert(sys.argv[1])


def display():
    rows = db.select()

    for row in rows:
        output.write(row, '\t')


def insert(arg):
    input_data = reader.read(arg)
    validation.validate(input_data)
    data.add_time(input_data)

    backup.save()
    db.insert(input_data)
    backup.save()

    output.write(input_data)


if __name__ == '__main__':
    main()
