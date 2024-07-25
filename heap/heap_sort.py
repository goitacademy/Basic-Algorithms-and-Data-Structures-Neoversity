from max_heap import MaxHeap
from min_heap import MinHeap

array = [12, 54, -3, 654, 2, 8, -564, 23, 235]

def heapsort(arr):  # Часова складність: O(n log n)
    # Сортування масиву за допомогою мін-купи
    heap = MinHeap(arr)  # Створюємо мін-купу з масиву
    # Витягуємо всі елементи з купи у відсортованому порядку
    return [heap.extract_min() for _ in range(len(heap.heap))]

print(heapsort(array))

def heapsort(arr):  # Часова складність: O(n log n)
    # Сортування масиву за допомогою макс-купи
    heap = MaxHeap(arr)  # Створюємо макс-купу з масиву
    # Витягуємо всі елементи з купи у відсортованому порядку
    return [heap.extract_max() for _ in range(len(heap.heap))]

print(heapsort(array))