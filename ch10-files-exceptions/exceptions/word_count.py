from pathlib import Path


def count_words(path: Path):
    """Count the approximate number of words in a file."""
    try:
        content = path.read_text()
    except FileNotFoundError:
        # print(f"Sorry, {path} does not exist.")

        # Failing silently
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path("alice.txt")
count_words(path)
