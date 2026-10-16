filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# input birthday
birthday = input("Input your birthday (mmddyy)")
if birthday in pi_string:
    print("Your birthday is in the first million digits of Pi!")
else:
    print("Your birthday is not in the first million digits of Pi!")

