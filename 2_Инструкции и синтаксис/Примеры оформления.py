#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#Часные случаи оформления инструкции
a = 1; b = 2; print(a + b) #три инструкции на одной строке
Q = [111, 
     222,
     333]   #одна инструкция на три строки
X = (2 + 3+ #Часто для переноса используется ()
     4 + 5)
if (a == 1 and #Тоже самое с составной
    b == 2 and
    X == 14):
    print('Ok')
if a > b: print('не ок))') #Такой стиль оформления не приветствуется

#Пару примеров реализации циклов
#брейк останавливает цикл
while True:
    r = input('Пиши ')
    if r == 'stop':
        break
    elif not r.isdigit(): #Проверяет число ли это(Верёт тру или фальс)
        print('11111')
    else:
        print(int(r)**2)
print('End')
#Тоже самое но иначе
while True:
    r = input('Пиши ')
    if r == 'stop':
        break
    try:
        num = int(r) #Если возникнет исключение выполнится excert
    except:          #Если нет else
        print('11111')
    else:
        print(int(r)**2)
print('End')

