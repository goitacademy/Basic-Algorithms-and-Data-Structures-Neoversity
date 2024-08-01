"""
Завдання
Уявімо, що у нас є компанія, яка виробляє два види продуктів: A та B.
Для виробництва цих продуктів використовуються три види ресурсів:
ресурс 1, ресурс 2 та ресурс 3. Кожен продукт приносить певний прибуток,
і ми хочемо максимізувати загальний прибуток.

Вхідні дані:
Продукт A приносить прибуток $3 за одиницю, продукт B - $5 за одиницю.
Кількість ресурсів:
Ресурс 1: 4 одиниці.
Ресурс 2: 12 одиниць.
Ресурс 3: 18 одиниць.
Продукт A потребує:
Ресурс 1: 1 одиницю на одиницю продукту.
Ресурс 2: 3 одиниці на одиницю продукту.
Ресурс 3: 2 одиниці на одиницю продукту.
Продукт B потребує:
Ресурс 1: 2 одиниці на одиницю продукту.
Ресурс 2: 2 одиниці на одиницю продукту.
Ресурс 3: 4 одиниці на одиницю продукту.
Постановка задачі:
Ми хочемо знайти оптимальні кількості продуктів A і B, які потрібно виробити,
щоб максимізувати загальний прибуток, не перевищуючи доступні ресурси.

Максимізувати: 3A + 5B
З обмеженнями:
1) 1A+2B≤4
2) 3A+2B≤12
3) 2A+4B≤18
4) A≥0,B≥0
"""


import numpy as np

def simplex(c, A, b):
    """
    Реалізація симплекс-методу для задачі лінійного програмування
    """
    m, n = A.shape

    # Створюємо таблицю симплекс-методу
    tableau = np.zeros((m+1, n+1))
    tableau[:-1, :-1] = A
    tableau[:-1, -1] = b
    tableau[-1, :-1] = -c

    # Функція для знаходження стовпця з найменшим значенням у останньому рядку
    def get_pivot_column():
        return np.argmin(tableau[-1, :-1])

    # Функція для знаходження рядка з мінімальним відношенням останнього стовпця до відповідного елементу в обраному стовпці
    def get_pivot_row(pivot_col):
        rows = np.where(tableau[:-1, pivot_col] > 0)[0]
        return rows[np.argmin(tableau[rows, -1] / tableau[rows, pivot_col])]

    # Поки є від'ємні значення у останньому рядку, продовжуємо ітерації
    while np.min(tableau[-1, :-1]) < 0:
        pivot_col = get_pivot_column()
        pivot_row = get_pivot_row(pivot_col)

        pivot_value = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_value

        for row in range(m+1):
            if row != pivot_row:
                tableau[row] -= tableau[row, pivot_col] * tableau[pivot_row]

    # Оптимальні значення змінних
    x = np.zeros(n)
    for i in range(n):
        col = tableau[:-1, i]
        if np.sum(col == 1) == 1 and np.sum(col == 0) == m-1:
            x[i] = tableau[np.where(col == 1)[0][0], -1]

    # Оптимальне значення цільової функції
    max_value = tableau[-1, -1]

    return np.round(x).astype(int), int(round(max_value))

# Вхідні дані
c = np.array([3, 5])
A = np.array([
    [1, 2],
    [3, 2],
    [2, 4]
])
b = np.array([8, 12, 18])

# Розв'язання задачі симплекс методом
x, max_value = simplex(c, A, b)

print(f"Оптимальна кількість продукту A: {x[0]}")
print(f"Оптимальна кількість продукту B: {x[1]}")
print(f"Максимальний прибуток: {max_value}")


# import pulp
#
# # Ініціалізація моделі
# model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)
#
# # Визначення змінних
# A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту A
# B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість продукту B
#
# # Функція цілі (Максимізація прибутку)
# model += 3 * A + 5 * B, "Profit"
#
# # Додавання обмежень
# model += 1 * A + 2 * B <= 8   # Обмеження по ресурсу 1
# model += 3 * A + 2 * B <= 12  # Обмеження по ресурсу 2
# model += 2 * A + 4 * B <= 18  # Обмеження по ресурсу 3
#
# # Розв'язання моделі
# model.solve()
#
# # Вивід результатів
# print("Виробляти продуктів A:", A.varValue)
# print("Виробляти продуктів B:", B.varValue)
# print("Максимальний прибуток:", pulp.value(model.objective))