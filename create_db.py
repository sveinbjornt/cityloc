# -*- encoding: utf-8 -*-
"""
    Create city database from from cities CSV file provided by

    ???????????
    
"""

from __future__ import print_function
from __future__ import unicode_literals

from builtins import input

import sys
import os
import sqlite3
import unicodecsv
import humanize

from pathlib import Path


def create_db(path):
    dbconn = sqlite3.connect(path)

    create_table_sql = """
    CREATE TABLE cities (
    id INTEGER UNIQUE PRIMARY KEY, 
    name TEXT,
    name_ascii TEXT,
    country TEXT,
    lat_wgs84 REAL,
    long_wgs84 REAL,
    region TEXT,
    capital INTEGER,
    population INTEGER
    );
    """

    dbconn.cursor().execute(create_table_sql)

    return dbconn


def read_rows(csv_file, delimiter=",", encoding="utf8"):
    reader = unicodecsv.DictReader(csv_file, delimiter=delimiter, encoding=encoding)
    for row in reader:
        yield row


def insert_entry(e):
    for k in e:
        e[k] = e[k].strip()

    to_float = ["lat", "lng"]

    for k in to_float:
        if e[k] == "":
            e[k] = None
        else:
            try:
                e[k] = float(e[k])
            except:
                print("Failed to convert '" + k + "' to float, setting to null")
                e[k] = None

    if e["capital"] == "primary":
        e["capital"] = 1
    else:
        e["capital"] = 0

    try:
        qargs = [
            None,
            e["city"],
            e["city_ascii"],
            e["iso2"],
            e["lat"],
            e["lng"],
            e["admin_name"],
            e["capital"],
            e["population"],
        ]
        c = dbconn.cursor()
        c.execute("INSERT INTO cities VALUES (?,?,?,?,?,?,?,?,?)", qargs)
    except Exception as e:
        print(e)


CSV_FILENAME = "worldcities.csv"
DEFAULT_DBPATH = "cityloc/resources/cities.db"

if __name__ == "__main__":
    # Optional args to specify input and output files
    csv_path = sys.argv[1] if len(sys.argv) > 1 else CSV_FILENAME
    db_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_DBPATH

    # Delete previous db file
    if Path(db_path).is_file():
        if input("%s exists, overwrite? (y/n): " % db_path).lower().startswith("y"):
            os.remove(db_path)
        else:
            print("Aborting")
            sys.exit()

    dbconn = create_db(db_path)

    f = open(csv_path, "rb")

    cnt = 0
    for r in read_rows(f):
        insert_entry(r)
        cnt += 1
        if cnt % 1000 == 0:
            dbconn.commit()
            print("\tInserting: %d\r" % cnt, end="")
            sys.stdout.flush()

    dbconn.commit()

    bytesize = os.stat(db_path).st_size
    human_size = humanize.naturalsize(bytesize)

    print("\nCreated database with %d entries (%s)" % (cnt, human_size))
