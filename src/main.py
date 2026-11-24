"""План тренировки на Python. Автор: allagardo."""

REPETITIONS_INCREMENT = 2


def read_integer(prompt, minimum, maximum=None):
    """Показывает подсказку и возвращает целое число в заданных границах."""
    while True:
        text = input(prompt).strip()
        if text.startswith("+"):
            text = text[1:]

        if text.isdecimal():
            value = int(text)
            if value >= minimum and (maximum is None or value <= maximum):
                return value

        if maximum is None:
            print(f"Введите целое число не меньше {minimum}.")
        else:
            print(f"Введите целое число от {minimum} до {maximum}.")


def load_category(total):
    """Возвращает категорию нагрузки по сумме повторений."""
    if total < 30:
        return "Небольшая"
    elif total <= 60:
        return "Средняя"
    else:
        return "Высокая"


def print_sets(set_count, first_repetitions):
    """По числу подходов и повторов в первом печатает таблицу и возвращает сумму."""
    print(f"{'Подход':>11}  {'Повторения, раз':>16}  {'Выполнено суммарно, раз':>29}")
    print("-" * 60)
    total = 0

    for set_number in range(1, set_count + 1):
        repetitions = first_repetitions + (set_number - 1) * REPETITIONS_INCREMENT
        total += repetitions
        set_label = f"{set_number:02d}"
        print(f"{set_label:>11}  {repetitions:>16d}  {total:>29d}")

    return total


def ask_for_new_workout():
    """Спрашивает про новую тренировку. Для ответа «да» возвращает True."""
    while True:
        answer = input("Составить новую тренировку? (да/нет) ").strip().lower()
        if answer == "да" or answer == "нет":
            return answer == "да"

        print("Введите «да» или «нет».")


def main():
    """Запрашивает данные и выводит отчёт для каждой тренировки."""
    new_workout = True
    while new_workout:
        exercise = input("Название упражнения: ").strip()
        set_count = read_integer("Количество подходов (1–5): ", 1, 5)
        first_repetitions = read_integer("Повторения в первом подходе: ", 1)

        print()
        print(f"{'План тренировки':^60}")
        print("-" * 60)
        total = print_sets(set_count, first_repetitions)
        average = total / set_count
        print("-" * 60)
        print(f"{'Упражнение':<34}{exercise:>26}")
        print(f"{'Количество подходов, шт.':<34}{set_count:>26d}")
        print(f"{'Всего повторений, раз':<34}{total:>26d}")
        print(f"{'Среднее за подход, раз':<34}{average:>26.2f}")
        print(f"{'Категория нагрузки':<34}{load_category(total):>26}")
        print("-" * 60)
        new_workout = ask_for_new_workout()
        print()

    print("Работа программы завершена")


if __name__ == "__main__":
    main()
