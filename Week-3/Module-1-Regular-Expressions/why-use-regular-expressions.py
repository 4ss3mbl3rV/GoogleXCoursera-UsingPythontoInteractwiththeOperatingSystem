import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# access process code using index
index = log.index('[')
print(log[index+1:index+6])
# in above method we don't exactly know how long the string were
# it's make it difficult and not flexible

# access process code using regex
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])
