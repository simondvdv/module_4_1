def divide(first, second):
    if not (isinstance(first, (int, float)) and isinstance(second, (int, float))):
        return 'Вы ввели не числа('
    if second == 0:
        return 'ошибка'
    return round(first / second, 2)




