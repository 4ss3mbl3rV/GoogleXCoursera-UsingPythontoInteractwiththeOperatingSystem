import csv

f = open('csv_file.txt')

# access to the csv_file
csv_f = csv.reader(f)
# iterating through the csv_f variable
for row in csv_f:
    name, phone, role = row
    print(f'Name: {name}, Phone: {phone}, role: {role}')
f.close()
