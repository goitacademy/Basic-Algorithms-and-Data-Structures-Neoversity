# import sys
# import numpy as np
# import itertools
# from copy import deepcopy
#
#
# def held_karp(dists):
#     L = {}
#
#     for k in range(1, nb_vertices):
#         L[((k), k)] = (dists[0][k], 0)
#     print('L=', L)
#
#     for subset_size in range(2, nb_vertices):
#         for subset in itertools.combinations(range(1, nb_vertices), subset_size):
#
#             list_subset = list(int(k) for k in subset)
#             # Find the lowest cost to get to this subset
#             for k in subset:
#                 list_subset_prev = deepcopy(list_subset)
#                 list_subset_prev.remove(k)
#                 res = []
#                 for m in subset:
#                     if m == 0 or m == k:
#                         continue
#                     if (len(list_subset_prev) == 1):
#
#                         res.append((L[((list_subset_prev[0]), m)][0] + dists[m][k], m))
#                     else:
#                         res.append((L[(tuple(list_subset_prev), m)][0] + dists[m][k], m))
#                 L[(tuple(list_subset), k)] = min(res)
#
#     list_vertices = list(int(k) for k in range(1, nb_vertices))
#
#     # Calculate optimal cost
#     res = []
#     for k in range(1, nb_vertices):
#         res.append((L[(tuple(list_vertices), k)][0] + dists[k][0], k))
#     opt, parent = min(res)
#
#     return opt
#
#
# if __name__ == '__main__':
#
#     with open('datasets/tsp0015.txt') as data_file:
#         vertices = []
#         nb_vertices = int(data_file.readline())
#         print("expected number of vertices : {0}\n".format(nb_vertices))
#         for line in data_file:
#             vertices.append(tuple(float(x) for x in line.split()))
#
#     vertices = np.array(vertices)
#     #    print(vertices.shape)
#     print(vertices)
#
#     dists = np.zeros((nb_vertices, nb_vertices))
#     for i in range(nb_vertices):
#         for j in range(nb_vertices):
#             dists[i, j] = np.sqrt(np.sum((vertices[i, :] - vertices[j, :]) ** 2))
#
#     #    print(dists.shape)
#     print(dists)
#     #    print(len(dists))
#     #    print('')
#
#     print(held_karp(dists))

import math


def held_karp_salesman(distances):
    """
    Знаходить оптимальний маршрут комівояжера і його вартість з використанням динамічного програмування
    та алгоритму Хелда-Карпа.

    Часова складність: O(n^2 * 2^n)
    Просторова складність: O(n * 2^n)

    Параметри:
    distances (list[list[int]]): Матриця відстаней між містами.

    Повертає:
    tuple: Оптимальний маршрут (список міст у порядку відвідування) і його вартість (мінімальна відстань).
    """
    n = len(distances)  # Кількість міст
    dp = [[math.inf] * n for _ in range(1 << n)]  # Таблиця для збереження мінімальних відстаней
    parent = [[None] * n for _ in range(1 << n)]  # Таблиця для збереження шляхів

    # Початковий випадок: початок з міста 0
    dp[1][0] = 0

    # Заповнення таблиці DP
    for mask in range(1 << n):  # Перебираємо всі можливі підмножини міст
        for last in range(n):  # Перебираємо всі можливі останні відвідані міста
            if not (mask & (1 << last)):  # Якщо місто не входить до підмножини, пропускаємо його
                continue
            for next in range(n):  # Перебираємо всі можливі наступні міста
                if mask & (1 << next):  # Якщо місто вже відвідане, пропускаємо його
                    continue
                new_mask = mask | (1 << next)  # Оновлюємо підмножину з новим містом
                new_dist = dp[mask][last] + distances[last][next]  # Обчислюємо нову відстань
                if new_dist < dp[new_mask][next]:  # Якщо нова відстань менша за поточну
                    dp[new_mask][next] = new_dist  # Оновлюємо таблицю DP
                    parent[new_mask][next] = last  # Зберігаємо шлях

    # Знаходимо оптимальний маршрут та мінімальну вартість
    min_cost = math.inf  # Початкова мінімальна вартість
    end_city = None  # Місто, де закінчується маршрут
    full_mask = (1 << n) - 1  # Маска для всіх міст

    for last in range(1, n):  # Перебираємо всі міста, щоб знайти мінімальну вартість маршруту
        cost = dp[full_mask][last] + distances[last][0]  # Додаємо вартість повернення в початкове місто
        if cost < min_cost:  # Якщо знайдена вартість менша за поточну мінімальну
            min_cost = cost  # Оновлюємо мінімальну вартість
            end_city = last  # Зберігаємо місто, де закінчується маршрут

    # Відновлюємо оптимальний маршрут
    tour = []  # Список для збереження маршруту
    mask = full_mask  # Маска для всіх міст
    last = end_city  # Починаємо з кінцевого міста
    while mask:  # Поки маска не пуста
        tour.append(last)  # Додаємо місто до маршруту
        new_last = parent[mask][last]  # Знаходимо попереднє місто
        mask ^= (1 << last)  # Видаляємо місто з маски
        last = new_last  # Переходимо до попереднього міста
    tour = tour[::-1]  # Обертаємо маршрут, щоб почати з початкового міста
    tour.append(0)  # Додаємо початкове місто в кінець для завершення циклу

    return tour, min_cost  # Повертаємо оптимальний маршрут та його вартість


# Приклад використання функції
distances = [
    [0, 20, 42, 35],
    [20, 0, 30, 34],
    [42, 30, 0, 12],
    [35, 34, 12, 0]
]



tour, min_cost = held_karp_salesman(distances)

print("Оптимальний маршрут:", tour)
print("Мінімальна відстань:", min_cost)
