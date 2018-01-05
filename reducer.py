import sys

def main():

    accountsTotal = 0
    oldKey = None

    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")
        if len(data) != 2:
            continue

        thisKey, thisSale = data

        if oldKey and oldKey != thisKey:
            print ("{0}\t{1}".format(oldKey, accountsTotal))

            accountsTotal = 0

        oldKey = thisKey

        accountsTotal += float(thisSale)

    if oldKey != None:
        print ("{0}\t{1}".format(oldKey, accountsTotal))

if __name__ == "__main__":
    main()