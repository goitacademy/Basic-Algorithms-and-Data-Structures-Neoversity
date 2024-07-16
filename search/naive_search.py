def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    results = []

    # Проходимося по тексту
    for i in range(n - m + 1):
        match = True
        # Перевіряємо співпадіння зразка з тексти починаючи з позиції i
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        # Якщо знайдено співпадіння, додаємо індекс початку співпадіння до результатів
        if match:
            results.append(i)

    return results

# Приклад використання
text = "AABAACAADAABAAABAA"
pattern = "AABA"
matches = naive_search(text, pattern)
if matches:
    print(f"Знайдено зразок '{pattern}' в тексті '{text}' на позиціях: {matches}")
else:
    print(f"Зразок '{pattern}' не знайдено в тексті '{text}'")
