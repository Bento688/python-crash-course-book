from pathlib import Path

contents = "I love programming\n"
contents += "I love C as well.\n"
contents += "I love my girlfriend.\n"

path = Path("rambles.txt")
path.write_text(contents)




