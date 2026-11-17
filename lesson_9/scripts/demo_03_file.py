"""Заняття 9 · Демонстрація 3. Надійне читання файлу.

Перед запуском потрібен файл journal.csv із заняття 8.
"""

import csv
from pathlib import Path

FILENAME = "file.csv"
DELIMITER = ";"
ENCODING = "utf-8-sig"


# =====================================================================
# КРОК 3. Читання наявного журналу
# =====================================================================
# Повернути правильне ім'я файлу й прочитати журнал,
# перетворюючи value у float.
#
# Очікуваний вивід для журналу з заняття 8:
#   Записів у журналі: 5

jour = []

read = 0
skipped = 0

try:
    with open(FILENAME, "r", encoding=ENCODING) as file:
        reader = csv.DictReader(file, delimiter=DELIMITER)
        for row in reader:
            valueStr = row['value']
            try:
                value = float(valueStr)
                jour.append(value)
                read = read + 1
            except ValueError:
                skipped = skipped + 1 
except FileNotFoundError:
    print(f"Файл {FILENAME} ще не створено")

print("Прочитано записів:", read)
print("Пропущено рядків:", skipped)
print(jour)