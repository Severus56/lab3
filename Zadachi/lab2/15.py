def digit_to_english(digit):
    """Преобразует цифру в английское название используя match-case"""
    match digit:
        case '0': return 'zero'
        case '1': return 'one'
        case '2': return 'two'
        case '3': return 'three'
        case '4': return 'four'
        case '5': return 'five'
        case '6': return 'six'
        case '7': return 'seven'
        case '8': return 'eight'
        case '9': return 'nine'
        case _: return None

digit = input("Введите цифру от 0 до 9: ")

result = digit_to_english(digit)
if result:
    print(f"{digit} - {result}")
else:
    print("Ошибка! Введите цифру от 0 до 9.")