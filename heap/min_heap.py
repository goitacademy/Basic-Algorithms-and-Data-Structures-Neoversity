class MinHeap:
    def __init__(self, arr=None):  # Часова складність: O(n)
        # Ініціалізація мін-купи, створюючи порожній список
        self.heap = []
        if type(arr) is list:  # Якщо переданий масив
            self.heap = arr.copy()  # Копіюємо масив у купу
            for i in range(len(self.heap))[::-1]:  # Перебираємо всі елементи у зворотньому порядку
                self._siftdown(i)  # Застосовуємо siftdown до кожного елемента

    def _siftup(self, i):  # Часова складність: O(log n)
        # Операція siftup для підтримки властивості купи
        parent = (i-1)//2  # Обчислення індексу батьківського вузла
        # Поки елемент менший за батьківський
        while i != 0 and self.heap[i] < self.heap[parent]:
            # Міняємо місцями елемент і батька
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent  # Перехід до батьківського вузла
            parent = (i-1)//2  # Оновлення індексу батьківського вузла

    def _siftdown(self, i):  # Часова складність: O(log n)
        # Операція siftdown для підтримки властивості купи
        left = 2*i + 1  # Лівий дочірній вузол
        right = 2*i + 2  # Правий дочірній вузол
        # Поки елемент більший за будь-який з дочірніх
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            # Визначення найменшого дочірнього вузла
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            # Міняємо місцями елемент і найменший дочірній вузол
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest  # Перехід до дочірнього вузла
            left = 2*i + 1  # Оновлення лівого дочірнього вузла
            right = 2*i + 2  # Оновлення правого дочірнього вузла

    def insert(self, element):  # Часова складність: O(log n)
        # Вставка нового елемента в купу
        self.heap.append(element)  # Додаємо елемент у кінець купи
        self._siftup(len(self.heap)-1)  # Застосовуємо siftup до нового елемента

    def get_min(self):  # Часова складність: O(1)
        # Повернення найменшого елемента (кореня купи)
        return self.heap[0] if len(self.heap) > 0 else None  # Перевірка на порожність і повернення кореня

    def extract_min(self):  # Часова складність: O(log n)
        # Витяг найменшого елемента з купи
        if len(self.heap) == 0:  # Якщо купа порожня
            return None  # Повертаємо None
        minval = self.heap[0]  # Збереження найменшого елемента (кореня)
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # Міняємо місцями корінь і останній елемент
        self.heap.pop()  # Видаляємо останній елемент (колишній корінь)
        self._siftdown(0)  # Застосовуємо siftdown до нового кореня
        return minval  # Повертаємо найменший елемент

    def update_by_index(self, i, new):  # Часова складність: O(log n)
        # Оновлення значення елемента за індексом
        old = self.heap[i]  # Збереження старого значення
        self.heap[i] = new  # Оновлення значення
        if new < old:  # Якщо нове значення менше старого
            self._siftup(i)  # Застосовуємо siftup
        else:  # Якщо нове значення більше або рівне старому
            self._siftdown(i)  # Застосовуємо siftdown

    def update(self, old, new):  # Часова складність: O(n)
        # Оновлення значення елемента за старим значенням
        if old in self.heap:  # Якщо старе значення є в купі
            # Знаходимо індекс старого значення і оновлюємо
            self.update_by_index(self.heap.index(old), new)


if __name__ == '__main__':
    # Тести для MinHeap
    print("Testing MinHeap:")
    min_heap = MinHeap()  # Створюємо порожню мін-купку
    min_heap.insert(5)  # Додаємо елемент 5
    min_heap.insert(3)  # Додаємо елемент 3
    min_heap.insert(8)  # Додаємо елемент 8
    min_heap.insert(1)  # Додаємо елемент 1
    print(min_heap.heap)  # Очікуємо [1, 3, 8, 5]

    print(min_heap.get_min())  # Очікуємо 1, найменший елемент

    print(min_heap.extract_min())  # Очікуємо 1, видалення найменшого елемента
    print(min_heap.heap)  # Очікуємо [3, 5, 8]

    min_heap.update(5, 2)  # Оновлюємо значення 5 на 2
    print(min_heap.heap)  # Очікуємо [2, 3, 8]

    # Додаткові тести для MinHeap з початковим масивом
    print("\nTesting MinHeap with initial array:")
    initial_array = [9, 4, 7, 1, 3, 6, 2]
    min_heap_from_array = MinHeap(initial_array)  # Створюємо мін-купку з початковим масивом
    print(min_heap_from_array.heap)  # Очікуємо [1, 3, 2, 4, 9, 6, 7]



