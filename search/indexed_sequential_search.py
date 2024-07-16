def create_index_table(array, step):
    # Функція створює індексну таблицю з відсортованого масиву з кроком `step`
    index_table = []
    for i in range(0, len(array), step):
        index_table.append((array[i], i))  # Додаємо кортеж (значення, індекс) у таблицю
    return index_table

# Функція для індексно-послідовного пошуку
def indexed_sequential_search(array, index_table, target):
    # Пошук в індексній таблиці
    start = 0
    end = len(index_table) - 1
    while start <= end:
        mid = (start + end) // 2  # Обчислення середини діапазону
        print(f"Шукаємо у індексній таблиці: діапазон {start}-{end}, середина {mid}")

        if index_table[mid][0] == target:
            return index_table[mid][1]  # Повертаємо індекс з індексної таблиці
        elif index_table[mid][0] < target:
            start = mid + 1  # Зміщуємо пошук до правої половини
        else:
            end = mid - 1  # Зміщуємо пошук до лівої половини
    print(f"Шукаємо у індексній таблиці: діапазон {start}-{end}, середина {mid}")
    # Визначення діапазону для послідовного пошуку
    if start == 0:
        search_range = (0, index_table[0][1])
    elif start >= len(index_table):
        search_range = (index_table[-1][1], len(array))
    else:
        search_range = (index_table[start - 1][1], index_table[start][1])

    print(f"Пошук у діапазоні {search_range}")

    # Послідовний пошук в діапазоні
    for i in range(search_range[0], search_range[1]):
        print(f"Порівнюємо {array[i]} з {target}")
        if array[i] == target:
            return i  # Повертаємо позицію, де знайдено елемент
    return -1  # якщо елемент не знайдено


target = 15

# Основний відсортований масив
main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
print(f"Основний відсортований масив: {main_array},\nЦілове значення: {target}")
# Створення індексної таблиці з кроком 4
index_table = create_index_table(main_array, 4)
print(f"Індексна таблиця: {index_table}")


result = indexed_sequential_search(main_array, index_table, target)
if result != -1:
    print(f"Елемент {target} знайдено на позиції {result}")
else:
    print(f"Елемент {target} не знайдено")
