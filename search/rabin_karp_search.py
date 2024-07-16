# Алгоритм Рабіна-Карпа для пошуку підрядків

# Функція для обчислення хешу рядка
def calculate_hash(s, prime, base):
    hash_value = 0
    for char in s:
        hash_value = (hash_value * base + ord(char)) % prime
    return hash_value

# Функція для пошуку підрядка в тексті
def rabin_karp_search(text, pattern):
    # Константи для хешування
    prime = 101  # Просте число для модуля
    base = 256  # Кількість символів в алфавіті

    m = len(pattern)
    n = len(text)

    # Обчислюємо хеш для підрядка і початкового вікна тексту
    pattern_hash = calculate_hash(pattern, prime, base)
    current_hash = calculate_hash(text[:m], prime, base)

    result = []

    for i in range(n - m + 1):
        print(f"pattern_hash: {pattern_hash},\t current_hash: {current_hash},\t pattern: {pattern},\t current text: {text[i:i + m]}")
        # Якщо хеші співпадають, перевіряємо самі рядки
        if pattern_hash == current_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        # Оновлюємо хеш для наступного вікна
        if i < n - m:
            current_hash = (current_hash - ord(text[i]) * (base ** (m - 1))) % prime
            current_hash = (current_hash * base + ord(text[i + m])) % prime
            current_hash = (current_hash + prime) % prime  # Забезпечуємо, щоб хеш був додатнім

    return result

# Приклад використання
text = "ABAAABCDABCAB"
pattern = "ABC"
print(f"Income text: {text},\t Search pattern {pattern}")
result = rabin_karp_search(text, pattern)

if result:
    print(f"Підрядок знайдено на індексах: {result}")
else:
    print("Підрядок не знайдено")