#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import sys

#рекурсия в функции
def mSum(X):
    print(X)
    if not X:
        return 0
    else:
        return X[0] + mSum(X[1:]) #Вызывает саму себя
print(mSum([]))
print(mSum([1,2,3,4,5,6]))

#Альтернативный способ рекурсии
def summ(X):
    return 0 if not X else X[0] + summ(X[1:])
print(summ([1,2,3,4,5,6]))

#Рекурсия не эфективна! лучше использовать циклы
X = [1,2,3,4,5,6]
summa = 0
for i in X: summa += i
print(summa,'Вот')

#однако они подходят для случаев с произвольной глубиной вложения
def sumree(L):
    tot = 0
    for i in L:
        if not isinstance(i, list):
            tot += i
        else:
            tot += sumree(i)
    return tot
L = [1,2,[3,4,[5],[6]]]
print(sumree(L))

#!!!Python ограничивает глубину своего стека вызовов
#Для расширения стека используйте модуль sys:
print(sys.getrecursionlimit()) # По умолчанию глубина составляет 1000 вызовов
sys.setrecursionlimit(10000) # Делает возможным более глубокое вложение
#help(sys.setrecursionlimit) # Дополнительные сведения об этой настройке


#Функции можно присваивать и передовать как любой другой обьект
def echo(op):
    print(op)

x = echo
x('Вот как!')

#передача функции функции
def lyly(qwe,rty):
    qwe(rty)
lyly(echo,'во хня))')

#и даже так
spis = [(echo,'бля'),(echo,'ёпт')]
for (fun, arg) in spis:
    fun(arg)

#и совсем странный пример
def ma(le):
    def echo(mes):
        print(le + ':' + mes)
    return echo
F = ma('хуй')
F('нахуй')
F('похуй')

#Интроспекция функций (Атрибуты, локальные переменные и  аргументы)
print(ma.__name__)
print(dir(ma))
print(ma.__code__)
print(dir(ma.__code__))
print(ma.__code__.co_varnames)
print(ma.__code__.co_argcount)

#присоединение атрибута 'arg' к функции
ma.arg = 12
print(ma.arg)
ma.arg = 'хобанна'
print(ma.arg)
print(dir(ma))

#Анатации в функциях
def funn(a:'нечто'=10,b:'Что нужно знать'=11)->int:
    return a + b
print(funn.__annotations__)

for arg in funn.__annotations__:
    print(arg,'=>',funn.__annotations__[arg])

#lambda выражения не возвращают результат они возвращают функцию, поиск имён у лямбда такойде как и у деф
H = lambda x=11, y=12 : x + y
print(H(13,44))
print(H(),'а вот значение по умолчанию')


#Пример использования лямбда выражения
U = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]
for i in U:
    print(i(4),'это **')
print(U[2](14))

key = 'qwe'
print({'qwe': (lambda: 4**4),
 'wer': (lambda: 6**6)}[key]())#обоащение по ключу генерирует функцию

O = (lambda x, y: x if y > x else y) #Выведет наименьший из аргументов
print(O(44,23))

cykl = (lambda x: [i**3 for i in x]) #использование циклов
print(cykl([1,2,3,4,5]))

#инструкция map вызывает функцию для каждого обьекта(map быстрее чем for) мап работает только с функциями
X = [1,2,3,4,5,6]
def inc(x): return x + 10
print(list(map(inc, X)))

#или
print(list(map((lambda x: x + 10),X)))

pow(3,4)# эквивалент 3**4
print(list(map(pow,X,[1,2,3,4,5,6]))) #обход двух последовательностей pow получает по очереди элементы из списков 1**1,2**2 ипт

#Функция filter
print(list(filter((lambda x: x > 0),range(-100,100)))) #фильтрует посредствам функции


#аналог фильтра редуце
X = [1,2,3,4,5,6]
from functools import reduce
print(reduce((lambda x, y: x + y),X),'reduce')#редуце может принимать третий аргумент который в случаи пустого списка будет принят по умолчанию
#эквивалент с помощью for
res = X[0]
for i in X[1:]:
    res = res + i
    print(res)
    print(X)
