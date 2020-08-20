import csv

field_names = ['name', 'age']
data = [
{'name': 'Jill', 'age': 32},
{'name': 'Sara', 'age': 28},
]
with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)

