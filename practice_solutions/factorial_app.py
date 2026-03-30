"""CLI utility for calculating a factorial with input validation."""

from math import factorial


def read_positive_integer() -> int:
    """Keep asking until the user enters a positive integer."""
    while True:
        raw_value = input("Введите положительное целое число: ").strip()

        if not raw_value:
            print("Ошибка: ввод не должен быть пустым.")
            continue

        try:
            number = int(raw_value)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue

        if number <= 0:
            print("Ошибка: число должно быть больше нуля.")
            continue

        return number


def main() -> None:
    number = read_positive_integer()
    result = factorial(number)
    print(f"Факториал числа {number} равен {result}.")


if __name__ == "__main__":
    main()
