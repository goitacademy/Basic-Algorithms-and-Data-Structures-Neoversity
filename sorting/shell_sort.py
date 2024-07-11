# Функція сортування Шелла (ітеративний підхід)
def shell_sort(array):
    n = len(array)  # Довжина масиву
    interval = n // 2  # Початковий інтервал

    # Продовжуємо сортувати поки інтервал більше 0
    while interval > 0:
        for i in range(interval, n):  # Проходимо по елементах масиву
            temp = array[i]  # Зберігаємо поточний елемент
            j = i
            # Переміщуємо елементи, що більше temp, на інтервал назад
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp  # Вставляємо temp на правильне місце
        interval //= 2  # Зменшуємо інтервал вдвічі
    return array  # Повертаємо відсортований масив

# Приклад використання
array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {shell_sort(array)}")


# Функція сортування Шелла (рекурсивний підхід)
def shell_sort_recursive(arr, gap=None):
    if gap is None:
        gap = len(arr) // 2  # Початковий інтервал

    if gap > 0:
        for i in range(gap, len(arr)):  # Проходимо по елементах масиву
            temp = arr[i]  # Зберігаємо поточний елемент
            j = i
            # Переміщуємо елементи, що більше temp, на інтервал назад
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp  # Вставляємо temp на правильне місце
        shell_sort_recursive(arr, gap // 2)  # Рекурсивний виклик із зменшеним інтервалом

    return arr  # Повертаємо відсортований масив

# Приклад використання
array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {shell_sort_recursive(array)}")
