import numpy as np
from time import time

def algorithm(cities):  # Часова складність: O(n^3)
    """
     Функція шукає найкоротший шлях для відвідування всіх міст, починаючи з кожного міста.
     Це робить її часову складність O(n^3), оскільки для кожного міста ми обчислюємо
     відстані до всіх інших міст і порівнюємо шляхи.
    """
    best_order = []  # Найкращий порядок міст
    best_length = float('inf')  # Найкоротша довжина шляху (початково нескінченність)

    for i_start, start in enumerate(cities):  # Перебираємо всі міста як стартові точки
        order = [i_start]  # Початковий порядок міст (починаємо з поточного міста)
        length = 0  # Початкова довжина шляху

        i_next, next, dist = get_closest(start, cities, order)  # Знаходимо найближче місто до стартового
        length += dist  # Додаємо відстань до загальної довжини шляху
        order.append(i_next)  # Додаємо індекс наступного міста до порядку

        while len(order) < cities.shape[0]:  # Поки не відвідаємо всі міста
            i_next, next, dist = get_closest(next, cities, order)  # Знаходимо найближче місто до поточного
            length += dist  # Додаємо відстань до загальної довжини шляху
            order.append(i_next)  # Додаємо індекс наступного міста до порядку

        # print(order)  # Для відлагодження: друкуємо порядок міст

        if length < best_length:  # Якщо знайдений шлях коротший за найкращий
            best_length = length  # Оновлюємо найкращу довжину шляху
            best_order = order  # Оновлюємо найкращий порядок міст

    return best_order, best_length  # Повертаємо найкращий порядок міст і найкоротшу довжину шляху

def get_closest(city, cities, visited):  # Часова складність: O(n)
    """
    Функція знаходить найближче місто до поточного, яке ще не відвідано.
    Її часова складність O(n), оскільки ми перевіряємо всі міста.
    """
    best_distance = float('inf')  # Найкоротша відстань (початково нескінченність)

    for i, c in enumerate(cities):  # Перебираємо всі міста
        if i not in visited:  # Якщо місто ще не відвідане
            distance = dist_squared(city, c)  # Обчислюємо відстань до поточного міста

            if distance < best_distance:  # Якщо відстань менша за найкращу
                closest_city = c  # Оновлюємо найближче місто
                i_closest_city = i  # Оновлюємо індекс найближчого міста
                best_distance = distance  # Оновлюємо найкращу відстань

    return i_closest_city, closest_city, best_distance  # Повертаємо індекс, координати і відстань до найближчого міста

def dist_squared(c1, c2):  # Часова складність: O(1)
    """
    Функція знаходить найближче місто до поточного, яке ще не відвідано.
    Її часова складність O(n), оскільки ми перевіряємо всі міста.
    """
    return pow(c2[0] - c1[0], 2) + pow(c2[1] - c1[1], 2)  # Обчислюємо квадрат евклідової відстані між двома містами



def main():
    # loading data
    f = open("datasets/tsp0038.txt", 'r').read().splitlines()
    f.pop(0)
    cities = np.array([tuple(map(float, coord.split())) for coord in f])

    # calculating path
    start = time()
    path, length = algorithm(cities)
    print(path)
    tottime = time() - start
    print("Знайдено шлях довжиною %s за %s секунд" % (round(length, 2), round(tottime, 2)))


if __name__ == "__main__":
    main()