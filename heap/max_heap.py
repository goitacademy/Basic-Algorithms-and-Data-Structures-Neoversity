class MaxHeap:
    def __init__(self, arr=None):  # Часова складність: O(n)
        # Ініціалізація макс-купи, створюючи порожній список
        self.heap = []
        if type(arr) is list:  # Якщо переданий масив
            self.heap = arr.copy()  # Копіюємо масив у купу
            for i in range(len(self.heap))[::-1]:  # Перебираємо всі елементи у зворотньому порядку
                self._siftdown(i)  # Застосовуємо siftdown до кожного елемента

    def _siftup(self, i):  # Часова складність: O(log n)
        # Операція siftup для підтримки властивості купи
        parent = (i-1)//2  # Обчислення індексу батьківського вузла
        # Поки елемент більший за батьківський
        while i != 0 and self.heap[i] > self.heap[parent]:
            # Міняємо місцями елемент і батька
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent  # Перехід до батьківського вузла
            parent = (i-1)//2  # Оновлення індексу батьківського вузла

    def _siftdown(self, i):  # Часова складність: O(log n)
        # Операція siftdown для підтримки властивості купи
        left = 2*i + 1  # Лівий дочірній вузол
        right = 2*i + 2  # Правий дочірній вузол
        # Поки елемент менший за будь-який з дочірніх
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            # Визначення найбільшого дочірнього вузла
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            # Міняємо місцями елемент і найбільший дочірній вузол
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest  # Перехід до дочірнього вузла
            left = 2*i + 1  # Оновлення лівого дочірнього вузла
            right = 2*i + 2  # Оновлення правого дочірнього вузла

    def insert(self, element):  # Часова складність: O(log n)
        # Вставка нового елемента в купу
        self.heap.append(element)  # Додаємо елемент у кінець купи
        self._siftup(len(self.heap)-1)  # Застосовуємо siftup до нового елемента

    def get_max(self):  # Часова складність: O(1)
        # Повернення найбільшого елемента (кореня купи)
        return self.heap[0] if len(self.heap) > 0 else None  # Перевірка на порожність і повернення кореня

    def extract_max(self):  # Часова складність: O(log n)
        # Витяг найбільшого елемента з купи
        if len(self.heap) == 0:  # Якщо купа порожня
            return None  # Повертаємо None
        maxval = self.heap[0]  # Збереження найбільшого елемента (кореня)
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # Міняємо місцями корінь і останній елемент
        self.heap.pop()  # Видаляємо останній елемент (колишній корінь)
        self._siftdown(0)  # Застосовуємо siftdown до нового кореня
        return maxval  # Повертаємо найбільший елемент

    def update_by_index(self, i, new):  # Часова складність: O(log n)
        # Оновлення значення елемента за індексом
        old = self.heap[i]  # Збереження старого значення
        self.heap[i] = new  # Оновлення значення
        if new > old:  # Якщо нове значення більше старого
            self._siftup(i)  # Застосовуємо siftup
        else:  # Якщо нове значення менше або рівне старому
            self._siftdown(i)  # Застосовуємо siftdown

    def update(self, old, new):  # Часова складність: O(n)
        # Оновлення значення елемента за старим значенням
        if old in self.heap:  # Якщо старе значення є в купі
            self.update_by_index(self.heap.index(old), new)  # Знаходимо індекс старого значення і оновлюємо

if __name__ == '__main__':
    # Тести для MaxHeap
    print("\nTesting MaxHeap:")
    max_heap = MaxHeap()  # Створюємо порожню макс-купку
    max_heap.insert(5)  # Додаємо елемент 5
    max_heap.insert(3)  # Додаємо елемент 3
    max_heap.insert(8)  # Додаємо елемент 8
    max_heap.insert(1)  # Додаємо елемент 1
    print(max_heap.heap)  # Очікуємо [8, 3, 5, 1]

    print(max_heap.get_max())  # Очікуємо 8, найбільший елемент

    print(max_heap.extract_max())  # Очікуємо 8, видалення найбільшого елемента
    print(max_heap.heap)  # Очікуємо [5, 3, 1]

    max_heap.update(3, 6)  # Оновлюємо значення 3 на 6
    print(max_heap.heap)  # Очікуємо [6, 5, 1]

    # Додаткові тести для MaxHeap з початковим масивом
    print("\nTesting MaxHeap with initial array:")
    initial_array = [9, 4, 7, 1, 3, 6, 2]
    max_heap_from_array = MaxHeap(initial_array)  # Створюємо макс-купку з початковим масивом
    print(max_heap_from_array.heap)  # Очікуємо [9, 4, 7, 1, 3, 6, 2]
