def bubble_sort(lst):
    n = len(lst)  # Дізнаємось довжину масиву
    for i in range(n-1):  # Повторюємо процес n-1 разів
        for j in range(0, n-i-1):  # Проходимось по масиву, не заходячи за відсортовану частину
            if lst[j] > lst[j+1]:  # Якщо елемент більший за наступний
                lst[j], lst[j+1] = lst[j+1], lst[j]  # Міняємо їх місцями
    return lst  # Повертаємо відсортований масив

array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {bubble_sort(array)}")



def bubble_sort_recursive(arr, n):
    if n == 1:  # Якщо масив має лише один елемент, він вже відсортований
        return

    for i in range(n - 1):  # Проходимо по всьому масиву
        if arr[i] > arr[i + 1]:  # Якщо поточний елемент більший за наступний
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Міняємо їх місцями

    bubble_sort_recursive(arr, n - 1)  # Викликаємо функцію знову, але для меншого масиву
    return arr  # Повертаємо відсортований масив

# Використання рекурсивного сортування
array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {bubble_sort_recursive(array, len(array))}")