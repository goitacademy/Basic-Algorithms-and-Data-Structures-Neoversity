def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    print(f"Побудова lps масиву")
    print(f"Шаблон: {pattern}")
    print(f"lps: {lps}")
    print()

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        print(f"i: {i}, length: {length}, lps: {lps}")

    print("\nГотовий lps масив:")
    print(f"lps: {lps}")
    return lps


def kmp_search(text, pattern):
    print(f"Вхідний масив: {text}\n")
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    print("\nПроцес пошуку:")

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print(f"Знайдено підрядок на індексі {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        print(f"i: {i}, j: {j}, поточний текст: {text[:i]}, поточний шаблон: {pattern[:j]}")


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)
