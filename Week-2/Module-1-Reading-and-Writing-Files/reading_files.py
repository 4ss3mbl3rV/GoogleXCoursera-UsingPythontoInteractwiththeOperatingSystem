'''
    In this .py source code I'm going to demonstrate how to read a file from local storage,
    this file is called "spider.txt" which located in the current directory where this script is living in.
'''

# first method
print('Method #1:')
file = open('spider.txt')

print(file.readline())
print(file.read())

file.close()

# second method
print('Method #2:')
with open('spider') as f:
    print(f.readline())
    print(f.read())

'''
    The difference between read() and readline() are
    - read() will read all the contents from current position and go down the whole content.
    - readline() will read just only the current position, means its will read line by line.
'''
