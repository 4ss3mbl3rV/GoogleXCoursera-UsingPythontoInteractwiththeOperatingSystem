import csv

hosts = [['workstation.local', '192.168.25.46'],['webserver.cloud', '10.2.5.6']]

with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    # there are two functions of writing the data into the csvfile
    # writerow() which will write one row at a time
    # writerows() which will write all of them together
    writer.writerows(hosts)
