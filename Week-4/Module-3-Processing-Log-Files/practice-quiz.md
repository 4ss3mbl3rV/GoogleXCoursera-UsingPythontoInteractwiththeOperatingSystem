# Practice Quiz: Processing Log Files

__To Pass__ 80% or higher

__Total points__ 5

1. You have created a Python script to read a log of users running CRON jobs. The script needs to accept a command line argument for the path to the log file. Which line of code accomplishes this? _(point 1)_
- [ ] import sys
- [ ] syslog =sys.argv[1]
- [ ] print(line.strip())
- [ ] usernames = {}

2. Which of the following is a data structure that can be used to count how many times a specific error appears in a log? _(point 1)_
- [x] Dictionary
- [ ] Continue
- [ ] Search
- [ ] Get

3. Which keyword will return control back to the top of a loop when iterating through logs? _(point 1)_
- [x] Continue
- [ ] Get
- [ ] With
- [ ] Search

4. When searching log files using regex, which regex statement will search for the alphanumeric word "IP" followed by one or more digits wrapped in parentheses using a capturing group? _(point 1)_
- [ ] `r"IP \(\d+\)$"`
- [ ] `b"IP \((\w+)\)$"`
- [x] `b"IP \((\w+)\)$"`
- [ ] `b"IP \((\w+)\)$"`

1. Which of the following are true about parsing log files? (Select all that apply.) _(point 1)_
- [ ] Load the entire log files into memory.
- [x] You should parse log files line by line.
- [x] It is efficient to ignore lines that don't contain the information we need.
- [x] We have to ___open()___ the logs files first.
