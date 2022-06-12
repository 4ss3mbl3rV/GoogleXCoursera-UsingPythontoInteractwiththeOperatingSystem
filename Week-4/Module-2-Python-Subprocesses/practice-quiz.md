# Practice Quiz: Python Subprocesses

__To Pass__ 80% or higher

__Total points__ 5

1. What type of object does a run function return? _(point 1)_
- [ ] returncode
- [x] CompletedProcess
- [ ] capture_output
- [ ] stdout

2. How can you change the current working directory where a command will be executed? _(point 1)_
- [x] Use the cwd parameter.
- [ ] Use the env parameter.
- [ ] Use the capture_output parameter.
- [ ] Use the shell parameter.

3. When a child process is run using the subprocess module, which of the following are true? (check all that apply) _(point 1)_
- [x] The child process is run in a secondary environment.
- [x] The parent process is blocked while the child process finished.
- [ ] The parent process and child process both run simulteneuosly.
- [x] Control is returned to the parent process when the child process ends.

4. When using the ___run___ command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command? _(point 1)_
- [ ] cwd
- [x] capture_output
- [ ] timeout
- [ ] shell

5. What does the copy method of os.environ do? _(point 1)_
- [x] Creates a new dictionary of environment variables
- [ ] Runs a second instance of an environment
- [ ] Joins two strings
- [ ] Removes a file from a directory
