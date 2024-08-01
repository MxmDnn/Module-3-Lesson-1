# Создаем переменную calls = 0 вне функции
calls = 0
# Создаём функцию count_calls и изменяем в ней значение переменной calls
# с использованием оператора global
def count_calls ():
    global calls
    calls+=1
# Создаём функцию string_info с параметром string
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
# Создаём функцию is_contains с двумя параметрами string и list_to_search
# Проверяем логику - входит ли строка string в список list_to_search,без учета регистра букв
def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [l.lower() for l in list_to_search]
# Вывод на консоль
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)