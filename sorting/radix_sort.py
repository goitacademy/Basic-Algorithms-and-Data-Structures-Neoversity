# Функція сортування Радікс (ітеративний підхід)
def radix_sort(nums):
    RADIX = 10  # Базова система числення (десяткова система)
    placement = 1  # Початковий розряд
    max_digit = max(nums)  # Максимальне число у масиві для визначення кількості розрядів

    # Продовжуємо сортувати, поки розряд менший за максимальне число
    while placement <= max_digit:
        # Створюємо "кошики" для кожного розряду
        buckets = [[] for _ in range(RADIX)]
        # Розподіляємо числа по кошикам відповідно до поточного розряду
        for i in nums:
            temp = (i // placement) % RADIX
            buckets[temp].append(i)
        # Оновлюємо масив, об'єднуючи числа з кошиків
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                nums[a] = i
                a += 1
        # Переходимо до наступного розряду
        placement *= RADIX
    return nums

# Приклад використання
nums = [3, 89, 67, 254, 9, 21, 185, 4, 62]
print("Відсортований масив:", radix_sort(nums))


# Допоміжна функція сортування за допомогою підрахунку для певного розряду
def counting_sort(arr, position):
    size = len(arr)  # Розмір масиву
    output = [0] * size  # Вихідний масив, ініціалізований нулями
    count = [0] * 10  # Масив підрахунку для розрядів (0-9)

    # Підрахунок кількості входжень кожної цифри у поточному розряді
    for i in range(size):
        index = (arr[i] // position) % 10
        count[index] += 1

    # Оновлення count[i] для визначення позиції наступної цифри у вихідному масиві
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Побудова вихідного масиву
    i = size - 1
    while i >= 0:
        index = (arr[i] // position) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Копіювання відсортованих чисел до початкового масиву
    for i in range(size):
        arr[i] = output[i]

# Функція сортування Радікс (рекурсивний підхід)
def radix_sort_recursive(arr):
    max_num = max(arr)  # Визначення максимального числа у масиві
    position = 1  # Початковий розряд

    # Виконання сортування за допомогою підрахунку для кожного розряду
    while max_num // position > 0:
        counting_sort(arr, position)
        position *= 10  # Переходимо до наступного розряду

# Приклад використання
arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
radix_sort_recursive(arr)
print("Відсортований масив:", arr)  # Відсортований масив: [3, 4, 9, 21, 62, 67, 89, 185, 254]
