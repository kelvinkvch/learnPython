import csv
villains = [
    {
        'first': 'Doctor',
        'last': 'No'
    },
    {
        'first': 'Rosa',
        'last': 'Klebb'
    },
    {
        'first': 'Mister',
        'last': 'Big'
    },
    {
        'first': 'Auric',
        'last': 'Goldfinger'
    },
    {
        'first': 'Ernst',
        'last': 'Blofeld'
    },
]
with open('proutfile\zt.csv', 'w',newline='') as f:
    csvout = csv.DictWriter(f, fieldnames=['first', 'last'])
    csvout.writeheader()
    csvout.writerows(villains)