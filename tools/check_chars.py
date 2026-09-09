import os
import yaml

from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
char_dir = repo_root / 'records' / 'characters'
count = 0
for root, dirs, files in os.walk(char_dir):
    for f in files:
        if not f.endswith('.md'): continue
        filepath = os.path.join(root, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        if content.startswith('---'):
            yaml_part = content.split('---')[1]
            try:
                data = yaml.safe_load(yaml_part)
                if data.get('race') == '' or data.get('stats', {}).get('level') is None:
                    count += 1
            except Exception as e:
                pass
print(f"Characters needing updates: {count}")
