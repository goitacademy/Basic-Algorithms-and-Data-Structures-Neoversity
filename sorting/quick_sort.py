# Ця функція однакова для обох ітеративної та рекурсивної реалізацій
def partition(array, left, right):
    i = (left - 1)
    pivot = array[right]

    for j in range(left, right):
        if array[j] <= pivot:
            # збільшити індекс меншого елемента
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return (i + 1)


# Функція для виконання ітеративного QuickSort
def quick_sort_iterative(array, left, right):
    # Створити допоміжний стек
    size = right - left + 1
    stack = [0] * size

    # ініціалізувати верхівку стеку
    top = -1

    # додати початкові значення left та right до стеку
    top = top + 1
    stack[top] = left
    top = top + 1
    stack[top] = right

    # Продовжувати витягувати зі стеку, поки він не порожній
    while top >= 0:

        # Витягнути right і left
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1

        # Встановити опорний елемент на його правильну позицію у відсортованому масиві
        pivot_position = partition(array, left, right)

        # Якщо є елементи з лівого боку від опорного елемента,
        # додати ліву частину до стеку
        if pivot_position - 1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = pivot_position - 1

        # Якщо є елементи з правого боку від опорного елемента,
        # додати праву частину до стеку
        if pivot_position + 1 < right:
            top = top + 1
            stack[top] = pivot_position + 1
            top = top + 1
            stack[top] = right



array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
quick_sort_iterative(array, 0, len(array) - 1)
print(f"Sorted array is {array}")


def quicksort(arr):
    # Якщо довжина масиву менше або дорівнює 1, повертаємо масив як є (він вже відсортований)
    if len(arr) <= 1:
        return arr
    # Вибираємо опорний елемент (у цьому випадку середній елемент масиву)
    pivot = arr[len(arr) // 2]
    # Створюємо три підмасиви: лівий, середній та правий
    # Лівий підмасив містить елементи менші за опорний елемент
    left = [x for x in arr if x < pivot]
    # Середній підмасив містить елементи, рівні опорному елементу
    middle = [x for x in arr if x == pivot]
    # Правий підмасив містить елементи більші за опорний елемент
    right = [x for x in arr if x > pivot]
    # Рекурсивно сортуємо лівий та правий підмасиви, і об'єднуємо їх разом із середнім підмасивом
    return quicksort(left) + middle + quicksort(right)



# def quicksort_verbose(arr):
#     print(f"Calling quicksort on {arr}")
#     if len(arr) <= 1:
#         print(f"returning {arr}")
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     print(f"left: {left}; ", end="")
#     middle = [x for x in arr if x == pivot]
#     print(f"middle: {middle}; ", end="")
#     right = [x for x in arr if x > pivot]
#     print(f"right: {right}")
#     to_return = quicksort_verbose(left) + middle + quicksort_verbose(right)
#     print(f"returning: {to_return}")
#     return to_return


array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {quicksort(array)}")
# print(f"Sorted array step by step is {quicksort_verbose(array)}")


# data = [1, 6, 5, 5, 2, 6, 1]
# print(quicksort(data))
#
# # for challenge
# data = [5, 4, 3, 2, 1]  # print(quicksort_verbose(data))
