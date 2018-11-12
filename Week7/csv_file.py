#/usr/bin/env python
import csv
from pprint import pprint
with open("routers.csv","r") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print("{} with IP {} is located at {}".format(row[0],row[1],row[2]))






