print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except Exception as e:
        print(f"Unable to calculate the pair {first_number} / {second_number}!\n")
    else:
        print(f"The answer is: {answer}\n")

