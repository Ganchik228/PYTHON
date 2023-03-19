#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
if month<1 or month>12:
    print('Некорректный номер месяца')
elif month==2:
    print('28 дней')
elif month in (1, 3, 5, 7, 8, 10, 12):
    print('31 день')
else:
    print('30 дней')