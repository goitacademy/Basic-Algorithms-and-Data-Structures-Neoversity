def interpolation_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high and array[low] <= target <= array[high]:
        # Використовуємо формулу інтерполяції для знаходження орієнтованого середнього
        mid = low + int(((high - low) / (array[high] - array[low])) * (target - array[low]))

        print(f"Шукаємо {target} в діапазоні [{low}, {high}]")
        print(f"Обчислений індекс mid: {mid}")

        if array[mid] == target:
            return mid  # Повертаємо індекс, де знайдено цільовий елемент
        elif array[mid] < target:
            low = mid + 1  # Якщо цільовий елемент більший, шукаємо праворуч від mid
        else:
            high = mid - 1  # Якщо цільовий елемент менший, шукаємо ліворуч від mid

    return -1  # якщо елемент не знайдено


# Основний відсортований масив
main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

target = 15
result = interpolation_search(main_array, target)

if result != -1:
    print(f"Елемент {target} знайдено на позиції {result}")
else:
    print(f"Елемент {target} не знайдено")
