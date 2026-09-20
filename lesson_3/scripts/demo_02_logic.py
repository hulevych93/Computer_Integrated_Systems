"""Заняття 3 · Демонстрація 2. Логічні операції and, or, not."""

T_MIN = -40.0
T_MAX = 60.0
P_MIN = 90.0
P_MAX = 110.0

t = float(input("Температура, °C: ").replace(",", "."))

# --- КРОК 1. «У межах діапазону» через and -----------------------------
in_range = t >= T_MIN and t <= T_MAX
print("У межах:", in_range)

# --- КРОК 2. Той самий сенс — ланцюжком --------------------------------
in_range_short = T_MIN <= t <= T_MAX
print("Ланцюжком:", in_range_short)

# --- КРОК 3. Протилежна умова: or і not --------------------------------
out = t < T_MIN or t > T_MAX
out_not = not in_range

print("Поза межами (or): ", out)
print("Поза межами (not):", out_not)

print("-" * 40)

# --- КРОК 4. Дві умови одночасно ---------------------------------------
p = float(input("Тиск, кПа: ").replace(",", "."))

p_ok = P_MIN <= p <= P_MAX
both_ok = in_range and p_ok

print("Температура в нормі:", in_range)
print("Тиск у нормі:       ", p_ok)
print("Обидва в нормі:     ", both_ok)
print("Хоча б один поза:   ", not both_ok)
