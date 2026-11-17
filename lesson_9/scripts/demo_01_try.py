"""Заняття 9 · Демонстрація 1. Перехоплення помилки.
"""

value1 = 10

try:
    value2 = int(input("Enter the value2:\n"))
    division = value1 / value2
    print(division)
except ZeroDivisionError:
    print("You can not divide by zero.")
except ValueError:
    print("You have entered a word instead of a number.")
except Exception:
    print("Something went wrong.")


print("Program runs...")
