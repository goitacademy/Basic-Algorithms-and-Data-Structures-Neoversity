def linear_search(arr, target):
    """
    Функція для лінійного пошуку елемента в масиві.

    Parameters:
    arr (list): Масив для пошуку.
    target: Елемент, який шукаємо.

    Returns:
    int: Індекс елемента в масиві або -1, якщо елемент не знайдено.
    """
    # Проходимо по всьому масиву
    for index in range(len(arr)):
        # Перевіряємо, чи дорівнює поточний елемент шуканому значенню
        if arr[index] == target:
            return index  # Повертаємо індекс знайденого елемента
    return -1  # Повертаємо -1, якщо елемент не знайдено

# Приклад використання
array = [12, 11, 13, 5, 6, 7]
target = 5
result = linear_search(array, target)

if result != -1:
    print(f"Елемент знайдено на індексі {result}")
else:
    print("Елемент не знайдено")
