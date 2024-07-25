from max_heap import MaxHeap

class PriorityQueue:
    def __init__(self):  # Часова складність: O(1)
        # Ініціалізація черги з пріоритетами за допомогою макс-купи
        self.queue = MaxHeap()  # Створюємо порожню макс-купу

    def enqueue(self, element):  # Часова складність: O(log n)
        # Додаємо елемент у чергу
        self.queue.insert(element)  # Вставка елемента в макс-купу

    def peek(self):  # Часова складність: O(1)
        # Повертаємо найбільший елемент (корінь купи) без видалення
        return self.queue.get_max()  # Отримання найбільшого елемента з макс-купи

    def dequeue(self, element):  # Часова складність: O(log n)
        # Видаляємо і повертаємо найбільший елемент з черги
        return self.queue.extract_max()  # Витяг найбільшого елемента з макс-купи

    def is_empty(self):  # Часова складність: O(1)
        # Перевіряємо, чи черга порожня
        return len(self.queue.heap) == 0  # Повертаємо True, якщо купка порожня, інакше False

    def change_priority_by_index(self, i, new):  # Часова складність: O(log n)
        # Зміна пріоритету елемента за індексом
        self.queue.update_by_index(i, new)  # Оновлення значення елемента в макс-купі за індексом

    def change_priority(self, old, new):  # Часова складність: O(n)
        # Зміна пріоритету елемента за старим значенням
        self.queue.update(old, new)  # Оновлення значення елемента в макс-купі за старим значенням

if __name__ == '__main__':
    # Тести для PriorityQueue
    print("Testing PriorityQueue:")
    priority_queue = PriorityQueue()  # Створюємо чергу з пріоритетами

    # Додаємо елементи в чергу
    priority_queue.enqueue(5)
    priority_queue.enqueue(3)
    priority_queue.enqueue(8)
    priority_queue.enqueue(1)

    # Перевіряємо вміст черги
    print(priority_queue.queue.heap)  # Очікуємо [8, 3, 5, 1]

    # Перевіряємо найбільший елемент
    print(priority_queue.peek())  # Очікуємо 8

    # Виймаємо найбільший елемент
    print(priority_queue.dequeue(None))  # Очікуємо 8
    print(priority_queue.queue.heap)  # Очікуємо [5, 3, 1]

    # Перевіряємо чергу на порожність
    print(priority_queue.is_empty())  # Очікуємо False

    # Зміна пріоритету за індексом
    priority_queue.change_priority_by_index(1, 6)  # Зміна пріоритету елемента з індексом 1 на 6
    print(priority_queue.queue.heap)  # Очікуємо [6, 5, 1]

    # Зміна пріоритету за значенням
    priority_queue.change_priority(5, 7)  # Зміна пріоритету елемента зі значенням 5 на 7
    print(priority_queue.queue.heap)  # Очікуємо [7, 6, 1]

    # Виймаємо всі елементи по черзі
    print(priority_queue.dequeue(None))  # Очікуємо 7
    print(priority_queue.dequeue(None))  # Очікуємо 6
    print(priority_queue.dequeue(None))  # Очікуємо 1
    print(priority_queue.is_empty())  # Очікуємо True

    # Додаткові тести з початковим масивом
    print("\nTesting PriorityQueue with initial array:")
    initial_array = [9, 4, 7, 1, 3, 6, 2]
    priority_queue_from_array = PriorityQueue()
    for elem in initial_array:
        priority_queue_from_array.enqueue(elem)

    print(priority_queue_from_array.queue.heap)  # Очікуємо [9, 4, 7, 1, 3, 6, 2]

    # Перевіряємо найбільший елемент у черзі з початковим масивом
    print(priority_queue_from_array.peek())
