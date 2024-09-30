#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#функция является способом группирования набора операторов

#def исполняемый програмный код, создаёт обьект и присваивает имя
#lambda создаёт обьект и возвращает его в виде результата
#return передаёт обьект результата вызывающей программе
#yield передаёт обьект результата вызывающей программе и запоминает где был произведён возврат
#global объявляет переменные уровня модуля, предназначенные для присваивания. По умолчанию все имена, присваиваемые в функции, являются локальными для функции и существуют только во время ее выполнения.
#nonlocal обьявляет переменные в облости видимости без присваивания значений


#*позиционные_аргурменты и • **ключевые_аргурменты.

def test(x, y): #Создаст функцию и свяжет её с именем
    return x * y # тело выполнится при вызове

print(test(2, 4)) #Аргументы в скобках
print(test('wer ', 5))

def qwe(q,w,e):
    return(q * w * e) - w
x = qwe(2,3,3)
print(x)

def func(one,too): #поиск пересечения тоже что и [x for x in one if x in too]
    res = []
    for i in one:
        if i in too:
            res.append(i)
    return res
print(func([1,2,3],[4,3,1]))

#можно и так
if test:
    def func():
        pass
else:
    def func():
        pass


#lambda может применяться в местах, где оператор def не допускается, скажем, внутри списковых и словарных литералов.
