from pathlib import Path

path = Path("number.txt")

if path and path.is_file() and path.read_text():
    content = path.read_text()

    try:
        try_number = int(content)
    except Exception as e:
        raise ValueError(f"Content of [{path}] cannot be translated into an integer.")

    if isinstance(try_number, int):
        try_number += 1
        path.write_text(str(try_number))
        print(f"Successfully incremented the number to {try_number}")


else:
    print(f"No file with name [{path}] found, creating one!")
    path.write_text("1")
