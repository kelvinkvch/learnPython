import csv
from pprint import pprint
with open('proutfile\zt.csv') as f:
    cin=csv.DictReader(f)
    res=[row for row in cin]

pprint(res)