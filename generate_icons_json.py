import os
import json

# Категорії, які відповідають назвам вкладок і папок
CATEGORIES = ['social', 'browsers', 'games', 'apps']
BASE_DIR = 'icons'
OUTPUT_FILE = os.path.join(BASE_DIR, 'icons.json')

data = {}

for category in CATEGORIES:
    folder_path = os.path.join(BASE_DIR, category)
    if not os.path.isdir(folder_path):
        continue

    icons = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.ico'):
            icons.append({
                'name': os.path.splitext(filename)[0].capitalize(),
                'src': f'{BASE_DIR}/{category}/{filename}'
            })

    data[category] = icons

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'✅ Згенеровано {OUTPUT_FILE}')
