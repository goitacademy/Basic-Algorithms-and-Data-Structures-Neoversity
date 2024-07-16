class HashTable:
    def __init__(self, size):
        self.size = size  # Розмір хеш-таблиці
        self.hash_table = [[] for _ in range(size)]  # Ініціалізація порожньої хеш-таблиці

    def hash_function(self, key):
        return key % self.size  # Проста функція хешування, наприклад, залишок від ділення на розмір таблиці

    def insert(self, key, value):
        hash_key = self.hash_function(key)  # Обчислення хешу для ключа
        self.hash_table[hash_key].append((key, value))  # Додавання пари (ключ, значення) до відповідного списку

    def search(self, key):
        hash_key = self.hash_function(key)  # Обчислення хешу для ключа
        print(f"Хеш індекс для пошуку {hash_key}")
        # Пошук у списку, який відповідає обчисленому хешу
        for item in self.hash_table[hash_key]:
            if item[0] == key:  # Якщо ключ співпадає, повертаємо відповідне значення
                return item[1]

        return None  # Якщо ключ не знайдено, повертаємо None

    def display(self):
        # Вивід хеш-таблиці з усіма елементами
        for i in range(self.size):
            print(f"Індекс {i}: {self.hash_table[i]}")

# Приклад використання хеш-таблиці для пошуку
hash_table = HashTable(10)  # Створення хеш-таблиці розміром 10

# Додавання елементів у хеш-таблицю
hash_table.insert(10, 'A')
# print("Хеш-таблиця після вставки:")
# hash_table.display()
hash_table.insert(25, 'B')
# print("Хеш-таблиця після вставки:")
# hash_table.display()
hash_table.insert(34, 'C')
# print("Хеш-таблиця після вставки:")
# hash_table.display()
hash_table.insert(45, 'D')
# print("Хеш-таблиця після вставки:")
# hash_table.display()
hash_table.insert(54, 'E')

# Виведення всієї хеш-таблиці
print("Хеш-таблиця після вставки:")
hash_table.display()

# Пошук елемента за ключем
key_to_search = 34
result = hash_table.search(key_to_search)
if result:
    print(f"Знайдено елемент з ключем {key_to_search}: {result}")
else:
    print(f"Елемент з ключем {key_to_search} не знайдено")

