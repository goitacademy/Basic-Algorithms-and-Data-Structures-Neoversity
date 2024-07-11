def selection_sort(arr):
    n = len(arr)  # Дізнаємось довжину масиву
    for i in range(n):  # Проходимо по всьому масиву
        min_idx = i  # Припускаємо, що найменший елемент на поточній позиції
        for j in range(i + 1, n):  # Шукаємо найменший елемент в невідсортованій частині
            if arr[j] < arr[min_idx]:  # Якщо знайшли елемент менший за поточний мінімум
                min_idx = j  # Оновлюємо індекс найменшого елемента
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Міняємо місцями поточний елемент і найменший елемент
    return arr  # Повертаємо відсортований масив

array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")  # Виводимо початковий масив
print(f"Sorted array is {selection_sort(array)}")  # Виводимо відсортований масив



def selection_sort_recursive(arr, index=0):
    if index == len(arr) - 1:  # Базовий випадок: якщо дійшли до останнього елемента, масив відсортований
        return

    min_index = index  # Припускаємо, що найменший елемент на поточній позиції
    for i in range(index + 1, len(arr)):  # Шукаємо найменший елемент в невідсортованій частині
        if arr[i] < arr[min_index]:  # Якщо знайшли елемент менший за поточний мінімум
            min_index = i  # Оновлюємо індекс найменшого елемента

    arr[index], arr[min_index] = arr[min_index], arr[index]  # Міняємо місцями поточний елемент і найменший елемент

    selection_sort_recursive(arr, index + 1)  # Викликаємо функцію знову для наступного елемента
    return arr  # Повертаємо відсортований масив

# Використання рекурсивного сортування вибором
array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")  # Виводимо початковий масив
print(f"Sorted array is {selection_sort_recursive(array)}")  # Виводимо відсортований масив
