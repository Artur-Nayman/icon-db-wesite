import os
import json
from PIL import Image

CATEGORIES = ['social', 'browsers', 'games', 'apps']
BASE_DIR = 'icons'
OUTPUT_FILE = os.path.join(BASE_DIR, 'icons.json')

data = {}

def reformat_file(files, icon_directory):
    for file in files:
        if file.endswith(('.ico', '.png')):
            file_path = os.path.join(icon_directory, file)
            img = Image.open(file_path)
            img = img.convert('RGBA')
            new_path = os.path.splitext(file_path)[0] + '.ico'
            img.save(new_path, format='ICO')
            if file.lower().endswith('.png'):
                os.remove(file_path)
                print(f"Видалено оригінальний PNG: {file_path}")

for category in CATEGORIES:
    category_dir = os.path.join(BASE_DIR, category)
    if not os.path.isdir(category_dir):
        continue
    icon_files = [f for f in os.listdir(category_dir) if f.endswith(('.ico', '.png'))]
    reformat_file(icon_files, category_dir)

for category in CATEGORIES:
    folder_path = os.path.join(BASE_DIR, category)
    if not os.path.isdir(folder_path):
        continue

    icons = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.ico'):
            icons.append({
                'name': os.path.splitext(filename)[0].capitalize(),
                'src': f'{category}/{filename}'
            })

    data[category] = icons

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'✅ Згенеровано {OUTPUT_FILE}')
