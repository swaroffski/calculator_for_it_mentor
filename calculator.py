def calculate(expression):
    try:
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError(
                "throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

        a, operator, b = parts
        a = int(a)
        b = int(b)

        if operator not in ['+', '-', '*', '/']:
            raise ValueError(
                "throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("throws Exception //т.к. числа должны быть в диапазоне от 1 до 10 включительно")

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
    try:
        while True:
            user_input = input("Input:\n")
            if len(user_input.split()) == 1:
                raise ValueError("throws Exception //т.к. строка не является математической операцией")
            result = main(user_input)
            print("Output:\n", result)
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
    except ValueError as e:
        print("Output:\n", e)
