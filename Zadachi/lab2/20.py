# Ввод двух чисел
x = int(input("Введите первое число x: "))
y = int(input("Введите второе число y: "))

print(f"Исходные значения: x = {x}, y = {y}")

# Вычисляем необходимые значения
half_sum = (x + y) / 2
double_product = 2 * x * y

# Меняем значения в зависимости от того, какое число меньше
x, y = (half_sum, double_product)
if x < y:
    x, y = (half_sum, double_product)
else:
    x,y = (double_product, half_sum)

print(f"После преобразования: x = {x}, y = {y}")