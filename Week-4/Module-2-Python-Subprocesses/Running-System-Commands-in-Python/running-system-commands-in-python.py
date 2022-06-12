import subprocess

subprocess.run(["date"])
result = subprocess.run(["ls", "some_files"])
print(result.returncode)
