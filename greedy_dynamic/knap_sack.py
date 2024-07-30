# Табуляція/2D масив Рішення
def knapSack_2D_array(capacity, weights, values, n): # O(n×capacity) V = O(n×capacity)
    # Створити двовимірний список для зберігання максимальних значень параметру knapsack
    # Ініціалізуємо усі значення 0
    dp = [[0 for _ in range(capacity + 1)] for i in range(len(weights) + 1)]

    # Перебір кожного елементу
    for i in range(n):
        # Перебрати всі можливі варіанти об'єму рюкзака
        for curr_capacity in range(capacity + 1):
            # Якщо вага поточного предмета менша або дорівнює поточному об'єму
            if weights[i] <= curr_capacity:
                # Вибираємо між включенням та виключенням поточного елементу
                # Якщо включаємо поточний елемент,
                # додамо його вартість до максимального значення, яке можна отримати
                # з урахуванням залишкової ємності та попередніх елементів
                # Важливе зауваження для мене:
                # Віднімаючи weights[i] від поточної ємності curr_capacity,
                # ми фактично обчислюємо, скільки ємності залишилося після включення елемента.
                # Потім, додаючи values[i] до виразу,
                # ми додаємо значення поточного елемента до максимально можливого значення
                # за допомогою залишкової ємності.
                # Отже, це означає, що я фактично обчислюю значення, якщо додаю поточний елемент
                # додаючи значення поточного елемента до значень решти елементів
                # якщо я включу поточний елемент.
                # Якщо ми виключаємо поточний елемент, максимальне значення залишається таким же, як у попередній комірці
                dp[i + 1][curr_capacity] = max(
                    dp[i][curr_capacity], values[i] + dp[i][curr_capacity - weights[i]]
                )
            else:
                # Якщо вага поточного елементу більша за поточну місткість,
                # ми не можемо включити елемент, тому максимальне значення залишається таким самим, як у попередній комірці
                dp[i + 1][curr_capacity] = dp[i][curr_capacity]

    # Повернути максимальне значення, яке може бути досягнуте з усіма елементами та заданою ємністю

    return dp[-1][-1]


# Рішення для одновимірного масиву
def knapSack_one_1D_Array(capacity, weights, values, n) -> int: # O(n×capacity) V = O(capacity)
    # Створюємо 1D список для зберігання максимально можливого значення для кожного об'єму
    dp = [0 for _ in range(capacity + 1)]

    # Перебір кожного елементу
    for i in range(n):
        # Зворотний цикл - через нього нам потрібен лише один 1D список
        for curr_cap in range(capacity, weights[i] - 1, -1):
            # Якщо вага поточного елементу менша або дорівнює поточній ємності,
            # обчислити максимальне значення, яке може бути досягнуте включенням або виключенням поточного елементу
            if weights[i] <= curr_cap:
                dp[curr_cap] = max(values[i] + dp[curr_cap - weights[i]], dp[curr_cap])
            else:
                # Якщо вага поточного елементу перевищує поточну ємність, то перериваємо цикл
                break

    # Повернути максимально досяжне значення для даної ємності
    return dp[-1]


# Рішення двох одновимірних масивів
def knapSack_two_1D_Array(capacity, weights, values, n) -> int: # O(n×capacity) V = O(capacity)
    # Ініціалізуємо два 1D списки для зберігання максимально можливого значення для кожної ємності
    # до розгляду поточного елементу та після розгляду поточного елементу.
    max_values_before = [0 for _ in range(capacity + 1)]
    max_values_after = [0 for _ in range(capacity + 1)]

    # Перебір кожного елементу
    for item_index in range(n):
        # Оновити список max_values_after для кожної ємності
        for curr_capacity in range(capacity + 1):
            if weights[item_index] <= curr_capacity:
                # Якщо поточний предмет можна помістити в рюкзак, обчислити максимальне значення
                # включивши або виключивши поточний предмет.
                max_values_after[curr_capacity] = max(
                    values[item_index] + max_values_before[curr_capacity - weights[item_index]],
                    max_values_before[curr_capacity])
            else:
                # Якщо поточний елемент не може бути включений, зберегти попереднє значення.
                max_values_after[curr_capacity] = max_values_before[curr_capacity]

        # Встановити список max_values_before таким, що дорівнює списку max_values_after для наступної ітерації.
        max_values_before[:] = max_values_after[:]

    # Повернути максимальне значення, досяжне для даної ємності.
    return max_values_after[-1]


# Рекурсивне рішення
def knapSack_recursive(W, wt, val, n): # O(2^n) V = O(n)
    return knapSackRecursion(W, wt, val, n, 0, 0)

def knapSackRecursion(max_weight, wt, val, n, ind, curr_weight):
    if ind >= n or curr_weight >= max_weight:
        return 0

    # Включити поточний елемент, якщо його вага в межах ємності
    if wt[ind] <= max_weight - curr_weight:
        include_curr = val[ind] + knapSackRecursion(max_weight, wt, val, n, ind + 1, curr_weight + wt[ind])
    else:
        include_curr = 0

    # Виключення поточного елементу і перехід до наступного елементу
    exclude_curr = knapSackRecursion(max_weight, wt, val, n, ind + 1, curr_weight)

    # Повернути максимальне значення, отримане при включенні або виключенні поточного елементу
    return max(include_curr, exclude_curr)

# Пояснення:
# W - максимальна вага рюкзака.
# wt - список ваг предметів.
# val - список вартостей предметів.
# n - кількість предметів.

W = 10
wt = [1, 3, 4, 6, 2, 1]
val = [10, 40, 50, 70, 90, 40]
n = len(wt)
print(knapSack_2D_array(W, wt, val, n))
print(knapSack_one_1D_Array(W, wt, val, n))
print(knapSack_two_1D_Array(W, wt, val, n))
print(knapSack_recursive(W, wt, val, n))

