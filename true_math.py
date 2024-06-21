from math import inf


def divide(first, second):
    if not (isinstance(first, (int, float)) and isinstance(second, (int, float))):
        return 'Вы ввели не числа('
    if second == 0:
        return inf
    return round(first / second, 2)
