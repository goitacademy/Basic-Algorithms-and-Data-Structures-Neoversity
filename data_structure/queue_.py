print("Basic queue")
# from queue import Queue
# # Ініціалізуємо чергу з максимальним розміром 3
# q = Queue(maxsize=3)
# # Додаємо елементи 'a' і 'b' до черги
# q.put('a')
# q.put('b')
# # Перевіряємо, чи черга повна (повертає True або False)
# print(q.full())  # Виведе False, оскільки черга ще не заповнена
# # Додаємо елемент 'c' до черги
# q.put('c')
# # Знову перевіряємо, чи черга повна
# print(q.full())  # Виведе True, оскільки черга тепер заповнена
# # Виводимо всі елементи черги як рядок, розділений пробілами
# print(' '.join(list(q.queue)))  # Виведе 'a b c'
# # Якщо черга не повна, додаємо елемент 'd'
# if not q.full():
#     q.put('d')
# else:
#     # Якщо черга повна, вилучаємо один елемент і додаємо 'd'
#     el = q.get()  # Вилучаємо перший елемент з черги
#     q.put('d')  # Додаємо елемент 'd' до черги
# # Виводимо всі елементи черги як рядок, розділений пробілами
# print(' '.join(list(q.queue)))  # Виведе 'b c d'


print("Bank queue")
# from queue import Queue
# import random
# # Клас, який представляє клієнта банку
# class Client:
#     def __init__(self, name):
#         self.name = name  # Ім'я клієнта
#         self.operations = random.randint(1, 5)  # Випадкова кількість операцій для клієнта
# # Клас, який представляє банк
# class Bank:
#     def __init__(self):
#         self.clients = Queue()  # Ініціалізуємо порожню чергу для клієнтів
#     # Метод для додавання нового клієнта до черги
#     def add_client(self, client):
#         self.clients.put(client)  # Додаємо клієнта до черги
#     # Метод для обслуговування клієнтів у черзі
    def serve_clients(self):
        while not self.clients.empty():  # Поки черга не пуста
            current_client = self.clients.get()  # Отримуємо клієнта з початку черги
            print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій")
            # Тут можна додати час обслуговування та іншу логіку
        else:
            print("Всі клієнти обслуговані, черга пуста")  # Повідомлення, що черга пуста

# if __name__ == '__main__':
#     # Створюємо банк
#     bank = Bank()
#     # Додаємо клієнтів до банку
#     for i in range(5):
#         bank.add_client(Client(f"Клієнт-{i}"))  # Створюємо нових клієнтів і додаємо їх до черги
#     # Обслуговуємо клієнтів
#     bank.serve_clients()  # Викликаємо метод для обслуговування клієнтів

print("Deque")
# from collections import deque
#
# # Масив чисел, який ми будемо обробляти
# initial_numbers = [23, 11, 12, 32, 10, 25, 65, 43, 42, 89, 100, 3]
#
# # Функція для обробки масиву чисел
# def process_numbers(numbers: list) -> list:
#     dq = deque()  # Ініціалізуємо порожню двосторонню чергу
#     dq.append(0)  # Додаємо 0 до черги (початковий елемент)
#     for number in numbers:  # Проходимося по кожному числу в масиві
#         if number % 2 == 0:  # Перевіряємо, чи є число парним
#             dq.append(number)  # Додаємо парне число до кінця черги
#         else:  # Якщо число непарне
#             dq.appendleft(number)  # Додаємо непарне число на початок черги
#     return dq  # Перетворюємо чергу назад у список і повертаємо його
#
# # Виклик функції для обробки масиву чисел і збереження результату
# processed_numbers = process_numbers(initial_numbers)
# # Виведення результату
# print(processed_numbers)
# processed_numbers.popleft()
# print(processed_numbers)