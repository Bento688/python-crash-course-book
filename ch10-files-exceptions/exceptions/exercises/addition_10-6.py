"""Prompt users for input and handle values"""

while True:
    a = input("First number: ")
    b = input("Second number: ")
    if b == 'q':
        print("Quitting")
        break

    try:
        a = int(a)
        b = int(b)
    except ValueError as e:
        print(str(e))
    else:
        print(a + b)
