import csv

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f'{row["name"]} has {row["users"]}')

# using dictWriter()
users = [{'name': 'Sol Mansi', 'username': 'solm', 'department': 'IT infrastructure'}]
keys = ['name', 'username', 'department']
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
