# Basic Linux Commands Cheat-Sheets

This list includes a bunch of different commands that are useful to know when working with Linux. Not all of these commands are covered in the videos, so feel free to investigate them on your own.

__Managing files and directories__
- __cd directory__: changes the current working directory to the specified one
- __pwd:__ prints the current working directory
- __ls:__ lists the contents of the current directory
- __ls directory:__ lists the contents of the received directory  
- __ls -l:__ lists the additional information for the contents of the directory  
- __ls -a:__ lists all files, including those hidden  
- __ls -la:__ applies both the -l and the -a flags  
- __mkdir directory:__ creates the directory with the received name
- __rmdir directory:__ deletes the directory with the received name (if empty)
- __cp old_name new_name:__ copies old_name into new_name
- __mv old_name new_name:__ moves old_name into new_name
- __touch file_name:__ creates an empty file or updates the modified time if it exists
- __chmod modifiers files:__ changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable
- __chown user files:__ changes the owner of the files to the given user
- __chgrp group files:__ changes the group of the files to the given group

__Operating with the content of files__
- __cat file:__ shows the content of the file through standard output
- __wc file:__ counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin
- __file file:__ prints the type of the given file, as recognized by the operating system
- __head file:__ shows the first 10 lines of the given file
- __tail file:__ shows the last 10 lines of the given file
- __less file:__ scrolls through the contents of the given file (press "q" to quit)
- __sort file:__ sorts the lines of the file alphabetically
- __cut -dseparator -ffields file:__ for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

__Additional commands__
- __echo "message":__ prints the message to standard output\
- __date:__ prints the current date
- __who:__ prints the list of users currently logged into the computer
- __man command:__ shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)
- __uptime:__ shows how long the computer has been running
- __free:__ shows the amount of unused memory on the current system

***

# Redirections, Pipes and Signals

__Managing streams__

These are the redirectors that we can use to take control of the streams of our programs
- command __>__ file: redirects standard output, overwrites file
- command __>>__ file: redirects standard output, appends to file
- command __<__ file: redirects standard input from file
- command __2>__ file: redirects standard error to file
- command1 __|__ command2: connects the output of command1 to the input of command2

__Operating with process__

These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.
- __ps:__ lists the processes executing in the current terminal for the current user
- __ps ax:__ lists all processes currently executing for all users  
- __ps e:__ shows the environment for the processes listed  
- __kill PID:__ sends the SIGTERM signal to the process identified by PID
- __fg:__ causes a job that was stopped or in the background to return to the foreground
- __bg:__ causes a job that was stopped to go to the background
- __jobs:__ lists the jobs currently running or stopped
- __top:__ shows the processes currently using the most CPU time (press "q" to quit)  