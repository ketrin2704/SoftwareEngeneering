#!/usr/bin/env python

import sys

def main():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split(",")

        if len(data) != 8:
            continue

        unique_code, name, country, indusrty, tag, ddate, uom, value = data

        if tag == 'Accounts':
        # Now print out the data that will be passed to the reducer
            print ("{0}\t{1}".format(indusrty, value))

if __name__ == "__main__":
    main()