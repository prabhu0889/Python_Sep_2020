import csv

# with open('testleaf.csv') as f:
#     data = csv.reader(f)
#     for row in data:
#        for i in row:          # ['S.no', 'First_Name', 'Last_Name']
#            print(i)
#

# with open('testleaf.csv') as f:
#     data = csv.reader(f)
#     for ls in data:
#         print(ls[0].ljust(10), ls[1].ljust(15), ls[2])
#

with open('testleaf.csv') as f:
    data = csv.DictReader(f)           # k with v
    for i in data:
        print(i['S.no'].ljust(10), i['First_Name'].ljust(15), i['Last_Name'])




