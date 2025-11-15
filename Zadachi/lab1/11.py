import math

# Ввод данных
a = float(input("Введите длину первой стороны a: "))
b = float(input("Введите длину второй стороны b: "))
g_degrees = float(input("Введите угол между сторонами в градусах g: "))

# Преобразование угла из градусов в радианы
g_radians = math.radians(g_degrees)

# Вычисление площади треугольника
# Площадь = (1/2) * a * b * sin(угол)
area = 0.5 * a * b * math.sin(g_radians)

# Вывод результата
print(f"Площадь треугольника: {area}")