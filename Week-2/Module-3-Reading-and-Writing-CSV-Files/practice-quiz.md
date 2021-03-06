# Practice Quiz: Reading & Writing CSV Files

__To pass__ 80% or Higher

__Total points__ 5

1. We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents_of_file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader. _(point 1)_

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
```

2. Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. How do you skip over the header record with the field names? _(point 1)_

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, 'r') as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in list(rows)[1:]:
      name, color, types = row
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(color, name, types)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
```

3. In order to use the writerows() function of DictWriter() to write a list of dictionaries to each line of a CSV file, what steps should we take? (Check all that apply) _(point 1)_
- [x] Create an instance of the DictWriter() class
- [x] Write the fieldnames parameter into the first row using writeheader()
- [x] Open the csv file using with open
- [ ] Import the OS module

4. Which of the following is true about unpacking values into variables when reading rows of a CSV file? (Check all that apply) _(point 1)_
- [x] We need the same amount of variables as there are columns of data in the CSV 
- [x] Rows can be read using both csv.reader and csv.DictReader
- [x] An instance of the reader class must be created first
- [ ] The CSV file does not have to be explicitly opened

5. If we are analyzing a file's contents to correctly structure its data, what action are we performing on the file? _(point 1)_
- [ ] Writing
- [ ] Appending
- [x] Parsing
- [ ] Reading