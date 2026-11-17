"""Заняття 9 · Демонстрація 2. Надійний ввід.
"""

def read_float(promt):
    temp = 0

    while True:
        try:
            tmp = input(promt)
            tmp.strip()
            tmp = tmp.replace(",", ".")
            temp = float(tmp)

            if temp < -273.15:
                print("Не може такого бути.")
            else:        
                break
        except ValueError:
            print("Введіть число, наприклад 20.5")

    return temp


temp = read_float("Temperature:\n")
print("Your temp: ", temp)

