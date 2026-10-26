from pathlib import Path

filepath = Path("pi_million_digits.txt")
contents = filepath.read_text()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Input your birthday (mmddyy): ")
if birthday in pi_string:
    print("Your birthday is in the first million digits of Pi!")
else:
    print("Your birthday is not in the first million digits of Pi!")


