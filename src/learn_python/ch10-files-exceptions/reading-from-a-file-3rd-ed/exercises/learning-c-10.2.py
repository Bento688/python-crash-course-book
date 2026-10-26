from pathlib import Path
import re

file_path = Path("in-python.txt")

full_content = file_path.read_text()

# print the contents line by line.
lines = full_content.splitlines()
for index, line in enumerate(lines):
    new_line = re.sub(r"python", "C", line, flags=re.IGNORECASE)
    lines[index] = new_line

for line in lines:
    print(line)
