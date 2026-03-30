"""Console game where the player guesses a random number."""

from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7


def ask_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"да", "д", "yes", "y"}:
            return True
        if answer in {"нет", "н", "no", "n"}:
            return False
        print("Введите 'да' или 'нет'.")


def read_guess() -> int:
    while True:
        raw_value = input(
            f"Введите целое число от {MIN_NUMBER} до {MAX_NUMBER}: "
        ).strip()

        try:
            guess = int(raw_value)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(
                f"Ошибка: число должно быть в диапазоне от {MIN_NUMBER} до {MAX_NUMBER}."
            )
            continue

        return guess


def play_game() -> None:
    secret_number = randint(MIN_NUMBER, MAX_NUMBER)

    print("Игра 'Угадай число'")
    print(
        f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}. "
        f"У вас есть {MAX_ATTEMPTS} попыток."
    )

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\nПопытка {attempt} из {MAX_ATTEMPTS}.")
        guess = read_guess()

        if guess == secret_number:
            print(f"Поздравляю, вы угадали число {secret_number}!")
            return

        if guess < secret_number:
            print("Слишком маленькое число.")
        else:
            print("Слишком большое число.")

        remaining_attempts = MAX_ATTEMPTS - attempt
        if remaining_attempts:
            print(f"Осталось попыток: {remaining_attempts}.")

    print(f"\nПопытки закончились. Было загадано число {secret_number}.")


def main() -> None:
    while True:
        play_game()
        if not ask_yes_no("\nСыграть еще раз? (да/нет): "):
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    main()
