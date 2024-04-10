def calculate(expression):
    a, operator, b = expression.split()
    a, b = int(a), int(b)
    if operator not in {'+', '-', '*', '/'} or not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("Неверный формат математической операции или числа должны быть в диапазоне от 1 до 10 включительно")
    return str(eval(expression))

if __name__ == "__main__":
    try:
        while True:
            user_input = input("Введите выражение (например, 2 + 3): ")
            result = calculate(user_input)
            print("Результат:", result)
    except (KeyboardInterrupt, ValueError) as e:
        print("\nПрограмма завершена.")