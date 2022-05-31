import os

# get directories in current working directory in list form
print(os.listdir())
# make new directory
os.mkdir('new_dir')
# change to new_dir/ directory
os.chdir('new_dir')
# get current woking directory
print(os.getcwd())
# to create a string containing cross-platform concatenated directories.
print(os.path.join('test', 'inner_test'))
# check whether is it directory or not
print(os.path.isdir(new_dir))
