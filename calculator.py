def calculate(expression):
    try:
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("Неверный формат математической операции")

        a, operator, b = parts
        a = int(a)
        b = int(b)

        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Недопустимая операция")

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно")

        if operator == '+':
            return str(a + b)
        elif operator == '-':
            return str(a - b)
        elif operator == '*':
            return str(a * b)
        elif operator == '/':
            return str(a // b)

    except ValueError as e:
        raise e


def main(input_str):
    return calculate(input_str)


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите выражение (например, 2 + 3): ")
            result = main(user_input)
            print("Результат:", result)
        except KeyboardInterrupt:
            print("\nПрограмма завершена.")
            break
        except ValueError as e:
            print("Ошибка:", e)
            break