import os
import yaml

char_dir = 'records/characters/'
files = os.listdir(char_dir)
count = 0
for f in files:
    if not f.endswith('.md'): continue
    filepath = os.path.join(char_dir, f)
    with open(filepath, 'r') as file:
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
