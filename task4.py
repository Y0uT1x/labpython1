# Варіант 10 - Норвегія

import math


def task4(n=None):
    if n is None:
        n = input()

    if isinstance(n, float) and not n.is_integer():
        return "Помилка. Введене значення не є цілим числом"

    try:
        n = int(n)
    except (TypeError, ValueError):
        return "Помилка. Введене значення не є цілим числом"

    # шукаємо a і b такі, що a^2 + b^2 = n
    a = 1
    while a * a < n:
        b = round(math.sqrt(n - a * a))
        if a * a + b * b == n and b > 0:
            return f"{a}^2+{b}^2={n}"
        a += 1

    return f"Число {n} не можна представити квадратами цілих чисел"


if __name__ == "__main__":
    print(task4())
