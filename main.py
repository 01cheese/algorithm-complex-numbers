import re




def which_format_number(number):
    # Убираем пробелы
    number = number.replace(' ', '')

    # Проверка на формат "a+bi" или "a-bi"
    if re.match(r'^([+-]?\d+)([+-]\d*)i$', number):
        print(re.findall(r'^([+-]?\d+)', number))
        return "a+bi", "a -> ", re.findall(r'^([+-]?\d+)', number), "b -> ", (re.findall(r'([+-]\d*)i$', number))
    # Проверка на формат "bi"
    elif re.match(r'^([+-]?\d*)i$', number):
        return "bi", "b -> ", number[:-1]
    # Проверка на формат "a"
    elif re.match(r'^[+-]?\d+$', number):
        return "a -> ", number
    else:
        return "Unknown format"


# Тесты
number = '-12+2i'
format_number = which_format_number(number)
print(f"The format of the number is: {format_number}")
