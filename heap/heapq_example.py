import heapq


# Min-Heap
print("Min-Heap")
# Створення порожньої мін-купи
min_heap = []

# Додавання елементів до мін-купи
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

# Вміст мін-купи
print(min_heap)  # Очікуємо [1, 3, 8, 5]

# Витягування найменшого елемента
min_element = heapq.heappop(min_heap)
print(min_element)  # Очікуємо 1

# Вміст мін-купи після витягування
print(min_heap)  # Очікуємо [3, 5, 8]

# Max-Heap
print("Max-Heap")
# Створення порожньої макс-купи
max_heap = []

# Додавання елементів до макс-купи (використовуючи негативні значення)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)

# Вміст макс-купи (позитивні значення)
print([-x for x in max_heap])  # Очікуємо [8, 3, 5, 1]

# Витягування найбільшого елемента
max_element = -heapq.heappop(max_heap)
print(max_element)  # Очікуємо 8

# Вміст макс-купи після витягування (позитивні значення)
print([-x for x in max_heap])  # Очікуємо [5, 3, 1]



# Finding k Smallest Elements
print("Finding k Smallest Elements")
# Список елементів
data = [5, 3, 8, 1, 2, 7]

# Знаходження 3 найменших елементів
k_smallest = heapq.nsmallest(3, data)
print(k_smallest)  # Очікуємо [1, 2, 3]

# Finding k Largest Elements
print("Finding k Largest Elements")

# Список елементів
data = [5, 3, 8, 1, 2, 7]

# Знаходження 3 найбільших елементів
k_largest = heapq.nlargest(3, data)
print(k_largest)  # Очікуємо [8, 7, 5]

# Merging Multiple Sorted Inputs
print("Merging Multiple Sorted Inputs")

# Список відсортованих входів
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

# Об'єднання відсортованих входів
merged_list = list(heapq.merge(list1, list2, list3))
print(merged_list)  # Очікуємо [1, 2, 3, 4, 5, 6, 7, 8, 9]