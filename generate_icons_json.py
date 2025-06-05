import os
import json

icons_dir = "icons"
output_file = os.path.join(icons_dir, "icons.json")

# Отримуємо список усіх .ico файлів
icons = [f for f in os.listdir(icons_dir) if f.endswith('.ico')]

# Записуємо в JSON
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(icons, f, ensure_ascii=False, indent=2)

print(f"icons.json збережено ({len(icons)} файлів).")
