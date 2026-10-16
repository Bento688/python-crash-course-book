from pathlib import Path

value = ''
name = ''

path = Path("guests.txt")

while name != 'q':
    name = input("Please input your name: ")
    if name == 'q':
        print("Writing guests!")
        break
    value += name
    value += "\n"
    print(f"Added guest [{name}] to the guest book!")

path.write_text(value)

