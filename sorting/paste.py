# Сортировка вставками
mass = list(map(int, input('Введите элементы массива(через пробел): ').split()))
# Счетчик количества иттераций
count = 0
# Перебор элементов массива коме первого
for i in range(1, len(mass)):
    # Сравнение все элементов массива
    for j in range(i, 0, -1):
        if mass[j] < mass[j-1]:
            # Перестановка элементов
            mass[j], mass[j-1] = mass[j-1], mass[j]
        else:
            break

    count += 1
print(*mass)
print(count)
