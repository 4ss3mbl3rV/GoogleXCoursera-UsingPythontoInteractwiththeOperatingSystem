'''
    We can either iterating file using for loop or storing content of file inside
    the variable using readlines() method as well.
'''
with open('spider.txt') as file:
    for line in file:
        print(line.upper().strip())
