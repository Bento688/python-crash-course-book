
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    first_name = input("First name: ")

    if first_name == "q":
        print("Program terminated.")
        break

    last_name = input("Last name: ")

    if last_name == "q":
        print("Program terminated.")
        break

    formatted_name = get_formatted_name(first_name, last_name)

    print(f"Hello, {formatted_name}!")
