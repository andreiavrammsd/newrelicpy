#!/usr/bin/python3.4

import sys
from app import reader, validation, data, backup, db, output


def main():
    input_data = reader.read(sys.argv[1])
    validation.validate(input_data)
    data.add_time(input_data)

    backup.save()
    db.insert(input_data)
    backup.save()

    output.write(input_data)

if __name__ == '__main__':
    main()
