# Виконує сортування злиттям знизу вгору
def merge_sort_bottom_up(array):
    width = 1  # Починаємо з мінімального розміру підмасиву, 2^0 = 1
    length = len(array)
    while width < length:  # Поки розмір підмасиву менший за загальну довжину масиву
        left = 0
        while left < length:  # Проходимо по масиву зліва направо
            right = min(left + (width * 2 - 1), length - 1)  # Визначаємо праву межу для об'єднання
            middle = min(left + width - 1, length - 1)  # Визначаємо середню межу для об'єднання
            merge(array, left, middle, right)  # Злиття двох підмасивів
            left += width * 2  # Переходимо до наступного підмасиву
        width *= 2  # Збільшуємо розмір підмасиву вдвічі на кожній ітерації
    return array  # Повертаємо відсортований масив


# Функція злиття підмасивів
def merge(array, left, middle, right):
    n1 = middle - left + 1  # Довжина першого підмасиву
    n2 = right - middle  # Довжина другого підмасиву

    left_array = [0] * n1  # Тимчасовий масив для першого підмасиву
    right_array = [0] * n2  # Тимчасовий масив для другого підмасиву

    # Копіюємо дані в тимчасові масиви
    for i in range(0, n1):
        left_array[i] = array[left + i]
    for i in range(0, n2):
        right_array[i] = array[middle + i + 1]

    i, j, k = 0, 0, left
    # Злиття двох тимчасових масивів у основний масив
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Додавання залишкових елементів з першого та другого підмасивів
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


# Функція сортування злиттям рекурсивно
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_recursive(left_half)
    right_half = merge_sort_recursive(right_half)

    return merge(left_half, right_half)  # Виклик функції злиття для двох підмасивів


# Приклад використання
array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {merge_sort_recursive(array)}")



# Функція сортування злиттям
def merge_sort(arr):
    # Якщо довжина масиву менше або дорівнює 1, повертаємо масив як є
    if len(arr) <= 1:
        return arr

    # Визначаємо середину масиву
    mid = len(arr) // 2
    # Ділимо масив на ліву і праву половини
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Зливаємо дві відсортовані половини
    return merge(left_half, right_half)


# Функція злиття двох відсортованих масивів
def merge(left, right):
    result = []  # Результуючий масив
    left_index, right_index = 0, 0  # Індекси для лівого і правого масивів

    # Зливаємо масиви, порівнюючи елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з обох масивів
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  # Повертаємо злитий масив


# Приклад використання
array = [12, 11, 13, 5, 6, 7]

print(f"Given array is {array}")
print(f"Sorted array is {merge_sort(array)}")

