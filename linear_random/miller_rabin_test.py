import random

def is_prime(n, k=5):
    """Перевірка простоти числа n за допомогою алгоритму Рабіна-Міллера."""

    # Якщо n < 2, воно не може бути простим
    if n < 2:
        return False
    # Якщо n == 2 або n == 3, воно є простим
    if n in (2, 3):
        return True
    # Якщо n парне, воно не є простим
    if n % 2 == 0:
        return False

    # 1) Представляємо число n як n-1 = 2^r * d, де d — непарне число.
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # def fermat_test(n, k=5):
    #     if n <= 1:
    #         return False
    #     for _ in range(k):
    #         a = random.randint(1, n - 1)
    #     if pow(a, n - 1, n) != 1:
    #         return False
    #     return True


    # Перевіряємо k випадкових баз
    for _ in range(k):
        # 2) Виберіть випадкове число a з діапазону [2, n−2].
        a = random.randint(2, n - 2)
        # 3) Обчисліть x = a^m mod n. Якщо x=1 або x=n−1, то перейдіть до наступного кроку.
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        # 4) Повторіть q разів: обчисліт x=x^2 modn. Якщо x=n−1, то перейдіть до наступного кроку.
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else: # Якщо попередній крок не вдалося завершити, то n є складеним.
            return False
    # Якщо жоден із кроків не визначив n як складене, то n ймовірно просте.
    return True



# Тестування функції
number = 61
iterations = 10
if is_prime(number, iterations):
    print(f"Число {number} ймовірно є простим.")
else:
    print(f"Число {number} є складеним.")
