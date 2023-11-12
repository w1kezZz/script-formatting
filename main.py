import re
import os

with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

# Создание словаря для хранения данных
files_data = {}

# Обработка каждой строки данных
for line in data:
    try:
        match = re.match(r'https?://([\w.-]+)/([\w.-]+):(.+)', line)
        if match:
            url = match.group(1)
            domain = re.sub(r'https?://', '', url)
            url_file = re.sub(r'[^\w\s]', '.', domain)
            username = match.group(3)
            password = match.group(3)
            file_path = os.path.join('files', f'{url_file}.txt')

            # Создание или добавление данных в соответствующий файл
            if url_file in files_data:
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(f'{username}\n')
            else:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(f'{username}\n')
                    files_data[url_file] = True
    except:
        continue

print("Готово!")