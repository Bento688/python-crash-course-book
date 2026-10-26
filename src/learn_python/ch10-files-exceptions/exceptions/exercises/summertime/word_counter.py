from pathlib import Path
from typing import List
import time


def count_unique_words(path: Path):
    # create a hashmap
    word_map = {}
    path_name = path.name

    try:
        with open(path, "r") as file:
            for line in file:
                words_in_line = line.split()
                for word in words_in_line:
                    word = word.lower()
                    word_map[word] = word_map.get(word, 0) + 1

        print(f"There are {len(word_map)} distinct words in {path_name}")
    except FileNotFoundError:
        print(f"Path: {path} not found!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent

    start_time = time.perf_counter()
    # get all the txt files in the directory
    files: List[Path] = [
        item for item in script_dir.iterdir() if item.suffix.lower() == ".txt"
    ]

    for file in files:
        count_unique_words(file)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
