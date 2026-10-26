import json
from pathlib import Path

path = Path('username.json')

content = path.read_text()

print(f"Hello! {json.loads(content)}! Good to have you back!")
