# Ввод натурального числа N
N = int(input("Введите натуральное число N: "))

# Проверка на корректность ввода
if N <= 0:
    print("Ошибка: N должно быть натуральным числом (больше 0)")
else:
    print(f"Простые делители числа {N}:")

    # Создаем копию N для обработки
    temp = N
    divisor = 2

    # Перебираем возможные делители
    while temp > 1:
        # Проверяем, является ли divisor делителем temp
        if temp % divisor == 0:
            # Проверяем, является ли divisor простым числом
            is_prime = True
            for i in range(2, int(divisor ** 0.5) + 1):
                if divisor % i == 0:
                    is_prime = False
                    break

            # Если divisor простой, выводим его
            if is_prime:
                print(divisor)

            # Делим temp на divisor
            temp //= divisor
        else:
            # Переходим к следующему возможному делителю
            divisor += 1