from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # count the words from the text
    words = contents.split()
    num_words = len(words)
    print(f"There are {num_words} words in {path}")
