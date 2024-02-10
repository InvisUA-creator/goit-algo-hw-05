from functools import reduce
from typing import Callable
import re


def generator_numbers(text: str):
    numbers = map(                                                            #Застосовуємо функцію float до кожного з відфільтрованих слів.
        float, filter(lambda x: re.match(r"\d+[\.,]{0,1}\d+.", x), text.split(" "))   #Фільтруємо слова, залишаючи лише ті,
                                                                                      # які відповідають шаблону регулярного виразу
    )
    for number in numbers:                                                     #Перебираємо числа, генерувані попереднім рядком.
        yield number                                                           #Повертає кожне число, роблячи функцію генератором


def sum_profit(text: str, func: Callable):
    return reduce(lambda x, y: x + y, func(text)) #reduce застосовує задану функцію до послідовності значень, накопичуючи результат.


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
