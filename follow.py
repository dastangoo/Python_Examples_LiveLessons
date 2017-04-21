# follow.py
#
# Watch a log file

import os
import time
import csv

def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue # Retry
        yield line   # Emit a line

def parse_check_data(lines):
    rows = csv.reader(lines)
    types = [str, float, str, float, float, float, int]
    converted = ( [func(val) for func, val in zip(types, row)] for row in rows)
    return converted

lines = follow('Data/stocklog.csv')
rows = parse_check_data(lines)
negchange = (row for row in rows if row[4] < 0)

for row in negchange:
    name = row[0]
    price = row[1]
    change = row[4]
    print('{:>10s} {:>10.2f} {:>10.2f}'.format(name, price, change))
