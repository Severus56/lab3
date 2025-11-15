def calculate_insurance_premium(age, insurance_amount):
    """
    Расчет страхового взноса в зависимости от возраста и страховой суммы.

    Параметры:
    age - возраст застрахованного (в годах)
    insurance_amount - страховая сумма

    Возвращает:
    Размер страхового взноса
    """

    if age < 1:
        rate = 0.10  # 10%
    elif 1 <= age < 5:
        rate = 0.08  # 8%
    elif 5 <= age < 20:
        rate = 0.05  # 5%
    elif 20 <= age < 45:
        rate = 0.03  # 3%
    elif 45 <= age < 50:
        rate = 0.05  # 5%
    elif 50 <= age < 65:
        rate = 0.08  # 8%
    else:  # 65 лет и старше
        rate = 0.10 + (age - 65) * 0.01  # 10% + 1% за каждый год после 65
        # Ограничиваем максимальную ставку 100%
        rate = min(rate, 1.0)

    premium = insurance_amount * rate
    return premium


# Примеры использования:
if __name__ == "__main__":
    # Тестовые примеры
    test_cases = [
        (0.5, 100000),  # младше 1 года
        (3, 100000),  # от 1 до 5
        (15, 100000),  # от 5 до 20
        (30, 100000),  # от 20 до 45
        (47, 100000),  # от 45 до 50
        (55, 100000),  # от 50 до 65
        (65, 100000),  # ровно 65
        (70, 100000),  # старше 65
        (80, 100000),  # значительно старше 65
    ]

    print("Расчет страховых взносов:")
    print("-" * 50)

    for age, amount in test_cases:
        premium = calculate_insurance_premium(age, amount)
        print(f"Возраст: {age:4} лет | "
              f"Страховая сумма: {amount:8} руб. | "
              f"Взнос: {premium:8.2f} руб. | "
              f"Ставка: {premium / amount * 100:5.1f}%")