# Ввод данных
start_amoebas = int(input("Введите начальное количество амеб: "))
hours = int(input("Введите время наблюдения в часах: "))
division_period = int(input("Введите период деления в часах: "))

# Расчет
divisions = hours // division_period
final_amoebas = start_amoebas * (2 ** divisions)

# Вывод результата
print(f"Через {hours} часов будет {final_amoebas} клеток амебы")