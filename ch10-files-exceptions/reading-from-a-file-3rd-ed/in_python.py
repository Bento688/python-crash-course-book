from pathlib import Path

file_path = Path("in-python.txt")

# print full contents once
full_content = file_path.read_text()
print(full_content)

# print it line by line.
for line in full_content.splitlines():
    print(line)
