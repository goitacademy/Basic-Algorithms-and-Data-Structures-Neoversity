import heapq

class PriorityQueueWithHeapq:
    def __init__(self):
        self.queue = []  # Ініціалізуємо порожній список для черги

    def enqueue(self, element):  # Часова складність: O(log n)
        heapq.heappush(self.queue, -element)  # Використовуємо мін-купу heapq для макс-черги (використовуючи негативні значення)

    def peek(self):  # Часова складність: O(1)
        return -self.queue[0] if self.queue else None  # Повертаємо найбільший елемент (перший у черзі)

    def dequeue(self):  # Часова складність: O(log n)
        return -heapq.heappop(self.queue) if self.queue else None  # Видаляємо і повертаємо найбільший елемент

    def is_empty(self):  # Часова складність: O(1)
        return len(self.queue) == 0  # Перевіряємо, чи черга порожня

    def change_priority(self, old, new):  # Часова складність: O(n)
        try:
            index = self.queue.index(-old)  # Знаходимо індекс старого значення
            self.queue[index] = -new  # Оновлюємо значення
            if new > old:
                heapq._siftup(self.queue, index)  # Застосовуємо siftup, якщо нове значення більше
            else:
                heapq._siftdown(self.queue, 0, index)  # Застосовуємо siftdown, якщо нове значення менше
        except ValueError:
            pass  # Якщо старе значення не знайдено, нічого не робимо

# Тестова функція для черги з пріоритетами
def test_priority_queue():
    pq = PriorityQueueWithHeapq()

    # Додаємо елементи в чергу
    pq.enqueue(5)
    pq.enqueue(3)
    pq.enqueue(8)
    pq.enqueue(1)

    # Перевіряємо вміст черги
    print([-elem for elem in pq.queue])  # Очікуємо [8, 3, 5, 1]

    # Перевіряємо найбільший елемент
    assert pq.peek() == 8, "Test failed: peek"

    # Виймаємо найбільший елемент
    assert pq.dequeue() == 8, "Test failed: dequeue"
    print([-elem for elem in pq.queue])  # Очікуємо [5, 3, 1]

    # Перевіряємо чергу на порожність
    assert not pq.is_empty(), "Test failed: is_empty"

    # Зміна пріоритету за значенням
    pq.change_priority(5, 7)  # Зміна пріоритету елемента зі значенням 5 на 7
    print([-elem for elem in pq.queue])  # Очікуємо [7, 3, 1]

    # Виймаємо всі елементи по черзі
    assert pq.dequeue() == 7, "Test failed: dequeue"
    assert pq.dequeue() == 3, "Test failed: dequeue"
    assert pq.dequeue() == 1, "Test failed: dequeue"
    assert pq.is_empty(), "Test failed: is_empty"

    print("All tests passed.")

# Виконання тестової функції
test_priority_queue()
