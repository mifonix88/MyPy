#!/usr/bin/evn python
# -*- coding: utf-8 -*-
class NovoeIskluchenie(Exception):#создать новое исключене
    pass

def fun():
    raise NovoeIskluchenie #Вызвать исключение

try:
    fun()
except NovoeIskluchenie: #перехватить
    print('Оппа')



try:
    print(1+1)
except NovoeIskluchenie: #перехватить
    print('Оппа')
else:
    print('выполнено Исключений не вызвано!')

'''
raise
Генерирует исключение вручную в коде.
assert
Генерирует исключение условно в коде.
'''

