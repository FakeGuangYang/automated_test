import csv


def parse_csv(file):
    mylist = []
    with open(file, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        return mylist[1:]
