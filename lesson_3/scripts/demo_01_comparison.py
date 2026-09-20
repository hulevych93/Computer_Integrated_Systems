"""Заняття 3 · Демонстрація 1. Порівняння та тип bool."""

# --- КРОК 1. Результат порівняння — це значення ------------------------
print(5 > 3)                  # True
print(5 < 3)                  # False

result = 5 > 3
print(type(result))           # <class 'bool'>

# True і False пишуться з великої літери й не беруться в лапки
flag = True
print(True + True)            # 2 — у розрахунках це 1 і 0

print("-" * 40)

# --- КРОК 2. Шість операторів порівняння -------------------------------
a = float(input("a = "))
b = float(input("b = "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a >  b:", a > b)
print("a <  b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("-" * 40)

# --- КРОК 3. Пастка дійсних чисел --------------------------------------
print(0.1 + 0.2 == 0.3)                      # False
print(abs((0.1 + 0.2) - 0.3) < 1e-9)         # True

# те саме через стандартну функцію
import math
print(math.isclose(0.1 + 0.2, 0.3))          # True

print("-" * 40)

# --- КРОК 4. Порівняння рядків -----------------------------------------
name1 = input("Прізвище 1: ").strip()
name2 = input("Прізвище 2: ").strip()

print("Однакові:", name1 == name2)
print("Без урахування регістру:", name1.lower() == name2.lower())
