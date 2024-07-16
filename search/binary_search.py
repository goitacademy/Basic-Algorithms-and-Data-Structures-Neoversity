def binary_search(arr, target):
    """
    Функція для бінарного пошуку елемента в відсортованому масиві.

    Parameters:
    arr (list): Відсортований масив для пошуку.
    target: Елемент, який шукаємо.

    Returns:
    int: Індекс елемента в масиві або -1, якщо елемент не знайдено.
    """
    left = 0  # Ліва межа масиву
    right = len(arr) - 1  # Права межа масиву

    while left <= right:
        mid = (left + right) // 2  # Знаходимо середину масиву
        print(f"left: {left},\t "
              f"right: {right},\t "
              f"mid: {mid},\t "
              f"target: {target},\t "
              f"arr_mid: {arr[mid]},\t"
              f"arr: {arr[left:right]}")


        if arr[mid] == target:
            return mid  # Якщо знайдено шуканий елемент, повертаємо його індекс
        elif arr[mid] < target:
            left = mid + 1  # Якщо шуканий елемент більший, зміщуємо ліву межу
        else:
            right = mid - 1  # Якщо шуканий елемент менший, зміщуємо праву межу


    return -1  # Повертаємо -1, якщо елемент не знайдено

# Приклад використання
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(array, target)

if result != -1:
    print(f"Елемент {target} знайдено на індексі {result}")
else:
    print(f"Елемент {target} не знайдено в масиві")
