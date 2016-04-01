#!/usr/bin/python3.4

import sys
import reader
import data
import validation
import backup
import db
import output

db_file = 'newrelic.csv'


def main():
    input_data = reader.read(sys.argv[1])
    validation.validate(input_data)
    data.add_time(input_data)

    backup.save(db_file)
    db.insert(db_file, input_data)
    backup.save(db_file)

    output.write(input_data)

if __name__ == '__main__':
    main()
