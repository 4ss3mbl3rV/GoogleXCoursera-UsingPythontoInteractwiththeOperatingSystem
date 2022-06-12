import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

# display return code of the subprocess

print(result.returncode)

# display STDOUT of the subprocess
print(result.stdout.decode().split())

# re-assign result and display STDERR
result = subprocess.run(["rm", "file_does_not_exist"])
print(result.stderr)
