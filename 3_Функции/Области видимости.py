#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#global переменная может не существовать до обьявления, создастся на уровне модуля
#nonlocal переменная должна существовать до обьявления, в глобальной области искать не будет


X = 99 # X с глобальной областью видимости (модуль)
#присваивания имен по умолчанию создают либо изменяют локальные имена;
#ссылки на имена производят поиск самое большее в четырех областях видимости — в локальной области видимости,
# затем в областях видимости объемлющих функций (если есть), далее в глобальной области видимости и, наконец, во встроенной области видимости;
def func():
    X = 88 # X с локальной областью видимости (функция) : другая переменная



#злоупотребление глобальными переменными считается дурным тоном
Q = ['qwe',2]
print(Q)
def test(w,e):
    x = w * e 
    Q.append(x) #Изменит глобальную переменную без обьявления
    return x
print(test(12,23))
print(Q)

#Пример облости видимости
X = 11 # X и fun Глобальная потому что присвоено значение на верхнем уровне
def fun():
    #локальная область существует только во время выполнения
    Z = X + 11 #X глобальная
    return Z
print(fun())


def func1(P):
    #Глобальные имена — это переменные, присвоенные на верхнем уровне включающего их файла модуля.
    #глобальные имена должны объявляться, только если им выполняются ПИСВАИВАНИЯ внутри функции.
    global Z #глобальная переменная, До её обьявления в модуле её не было
    Z = X + 22
    return Z

print(func1(4))
print(Z)

'''
#1.py
X = 99
def setX(Q):
    global X
    X = Q
#2.py
import 1
1.setX(88)
'''
def f1():
    X = 88
    def f2():
        f3(X)#опережающие ссылки допустимы
    return f2 #возвращает функцию но не вызывает её
def f3(X):
    print(X) #88
f4 = f1()#создаёт функцию
print(f4())

#лямбда создаёт новую функцию
def funk():
    x = 4
    op = (lambda n: x ** n) #х запоминается из обемлющей инструкции def
    return op
x = funk()
print(x(4)) #выведет результат


#лямбда в циклк
def funcc():
    asd = []
    for i in range(10):
        asd.append(lambda x, i=i: i ** x) #i=i явное указание на переменную
    return asd
asd = funcc()
print(asd[0](2))
print(asd[5](2))

#инструкция nonlocal (пропустить локальную облость видимости при поиске имён)

def tester(st):  #создаёт и возвращает функцию
    start = st
    def nest(lab):#Изменит и сохранит значение старт в функции которая уже завершила работу
        nonlocal start# по сути ищи старт этажом выще но не в глобальных
        print(lab, start)
        start += 1
    return nest
f = tester(0)
f('ёпт')
f('ёпт')
f('ёпт')
g = tester(55) #начнёт счёт с 55
g('ёпт')
g('ёпт')
g('ёпт')
f('ёпт') #Здесь хранится старое значение(Каждая новая функция получает свой экземпляр start)
#def nest():
    #   nonlocal start #!!!переменная должна быть доступна ещё до инструкции нонлокал
    #   start = 1
    
#Альтернативное решение спомощью классов
class tester:
    def __init__(self, st): #Конструктор обьекта
        self.start = st     #Сохранит состояние о новом обьекте
    def nest(self, lab):
        print(lab, self.start)
        self.start += 1    #Изменения всегда доступны
R = tester(11) #Создаст экземпляр класса, вызовет инит
R.nest('qwerty') #ссылка на R будет передана в аргумент селф
R.nest('reqe')
E = tester(77)
E.nest('popo')
R.nest('wep')

#Можно и так
class tester1:
    def __init__(self, st): 
        self.start = st     
    def __call__(self, lab): #Вызывается при вызове экземпляра
        print(lab, self.start)
        self.start += 1  
N = tester1(99)
N('Вот') #Вызывает метод call
N('Так')

#И ещё пример с атрибутами
def tester3(st):  
    def nest(lab):
        print(lab, nest.start)
        nest.start += 1 #изменит атрибут а не значение имени nest
    nest.start = st
    return nest
f = tester3(0)
f('ёпт') #f это функция nest с присоединённым атрибутом start
f('ёпт')
f('ёпт')
print(f.start)
g = tester3(55) 
g('ёпт')
g('ёпт')
g('ёпт')



import builtins #Встроенная область видимости
print(dir(builtins))



#патерн проектирования
'''
Фабричные функции (они же замыкания) иногда применяются в программах, 
которым необходимо генерировать обработчики событий на лету в ответ на условия,
 сложившиеся во время выполнения. Например, представим себе графический пользо
вательский интерфейс, где нужно определять действия согласно данным, введенным 
пользователем, которые невозможно предугадать на этапе построения интерфейса.
'''
def maker (N):
    def action(X): # Создание и возвращение функции action
        return X ** N # action сохраняет N из объемлющей области видимости 
    return action

f = maker(2)# Передача 2 аргументу N
print(f(3)) #Передача 3 аргументу X, в N запоминается 2: 3 ** 2
'''
Пожалуй, самой необычной частью следует считать запоминание вложенной функцией целого числа 2, 
т.е. значения переменной N в maker, хотя к моменту вызова action уже произошел возврат из ф
ункции maker, и она закончила работу. По существу N из локальной области видимости
 объемлющей функции сохраняется как информация о состоянии, присоединенная к 
 сгенерированной функции action — вот почему в результате ее вызова мы получили 
 значение аргумента, возведенное в квадрат.
Не менее важен и тот факт, что если мы снова вызовем внешнюю функцию, то получим 
обратно новую вложенную функцию с другой присоединенной информацией о состоянии.
Так, при вызове новой функции значение аргумента возводится в куб, а не в квадрат, 
но предыдущая функция по-прежнему возводит в квадрат, как и ранее:
'''
#тоже самое но с lambda
def maker(N) :
    return lambda X: X ** N


#когда один оператор def функции вложен в другой, то вложенная функция способна 
#ссылаться на любые имена, определенные присваиваниями в области видимости объемлющего оператора def,
# но не может изменять их.nonlocal дает возможность вложенным функциям выполнять присваивание и тем самым изменять такие имена.
#То есть nonlocal также означает “полностью пропустить мою локальную область видимости”

#nonlocal переменные должны существовать в области видимости объемлющей функции в момент обьявления
#объявление nonlocal не разрешено на уровне модуля



#иерархия
Встроеная #библиотека builtins
    Глобальная #на уровне модуля
        Охватывающие #до def но не на уровне модуля(между def ами)(nonlocal)
            Локальные #после def и т.п
