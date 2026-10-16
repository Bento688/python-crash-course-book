from pathlib import Path
from typing import List


def read_file(path: Path):
    try:
        content = path.read_text()
    except FileNotFoundError as e:
        # print(str(e))
        pass
    else:
        for word in content.split():
            print(word)


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent

    # get all the txt files in the directory
    files: List[Path] = [
        item for item in script_dir.iterdir() if item.suffix.lower() == ".txt"
    ]

    for file in files:
        read_file(file)
