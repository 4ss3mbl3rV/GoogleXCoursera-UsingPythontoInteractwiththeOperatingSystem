import shutil

du = shutil.disk_usage('C:\\')

# print total number of disk in bytes
print(du)

# caculate percentage
print(du.free/du.total * 100)
