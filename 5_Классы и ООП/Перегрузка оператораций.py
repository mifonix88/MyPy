#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#Если не определить действия по умолчанию то они будут не доступны для этого класса

#по сути перегрузка операций это перехват встроенных операций в методах класса
class InitClass:
    '''Конструктор'''
    def __init__(self,nomer=0):
        self.nomer = nomer

class AddClass:
    '''Сложение''' 
    def __add__(self,i): #смотри также __radd___
        return self.nomer + i

class SubClass:
    '''Вычитание'''
    def __sub__(self, num):
        return self.nomer - num

class GetitemClass: #для итераций предпочтитедльнее использовать __iter__ или другие альтернативы(но не обязательно)
    '''Извлечение среза'''
    def __getitem__(self,index):
        return self.nomer[index]

class SetitemClass:
    '''Присваивание по срезу'''
    def __setitem__(self,znachenie):
        return self.data[znachenie] 
        
class GetattrClass:
    '''Получение ссылки на атрибут'''
    def __setattr__(self, arg, name):
        if arg == 'nomer': #если атрибут не 'номер' вызовет исключение
            self.__dict__[arg] = name
        else:
            raise AttributeError( arg +' не предусмотрено')
            
class ReprClass:
    '''вывод обьектов на экран'''
    def __repr__(self): #аналог __str__
        return str(self.nomer) 
        
class CallClass:
    '''Вызывается при обращении к экземпляру как к функции'''
    def __call__(self, *arg, **gum):#принимает любые аргументы(используется в графических интерфейсах)
        return arg ,gum #__ call__ реализует интерфейс вызова функций для экземпляров класса.
        
        
class OneClass(InitClass,AddClass,SubClass,GetitemClass,SetitemClass,GetattrClass,ReprClass,CallClass): pass

if __name__ == '__main__':
    print(OneClass(1)+1)
    nomer = OneClass() 
    print(nomer + 22) 
    print(nomer - 22) 
    one = OneClass('qwerty')
    print(one[:2])
    too = OneClass()
    too.nomer = 'QWERT'
    print(too[:5])
    print([i for i in too])
    #one.qweg = 1
    print(too(1,2,3, x = 4))

'''
наиболее часто используемые
__init__ Конструктор Создание объекта: X = Class(args)
__del__ Деструктор Уничтожение объекта х
__add__ Операция + х + Y, х += Y, если отсутствует __iadd__
__or__ Операция | (побитовое “ИЛИ”) х | Y, х I = Y, если отсутствует __ior__
__repr__ ,__ str__ Вывод, преобразования print(X), repr(X), str(X)
__call__ Вызовы функций X(*args, **kargs)
__getattr__ Извлечение атрибута X.undefined
__setattr__ Присваивание атрибута X.any = value
__delattr__ Удаление атрибута del X.any
__getattribute__ Извлечение атрибута X.any
__getitem__ Индексирование, нарезание, итерация X[key], X [ i: j ], циклы for и другие итерационные конструкции, если отсутствует_ iter__
__setitem__ Присваивание по индексу и срезу X[key] = value, X[i: j] = iterable
__delitem__ Удаление по индексу и срезу del X[key], del X[i:j]
__len__ Длина len (X), проверки истинности, если отсутствует_ bool_
__bool__ Булевские проверки bool (X), проверки истинности (в Python 2.Х называется __nonzero__ )
__It__ ,__ gt__ , Сравнения X < Y, X > Y,
__le__ ,__ ge__ , X <= Y, X >= Y, X == Y,
__eq__ ,__ ne__ х ! = Y (либо иначе __стр__ только в Python 2.Х)
__radd__ Правосторонние операции Other + X
__iadd__ Дополненные на месте операции х += Y (либо иначе_ add__ )
__iter__ , Итерационные контексты I=iter(X), next (I); циклы
__next__   for, in, если отсутствует __contains__ , все включения, map (F,X), остальные (__next__ в Python 2.X называется next)
__contains__ Проверка членства item in X (любой итерируемый объект)
__index__ Целочисленное значение hex(X), bin(X), oct(X), 0[Х], 0 [ х: ] (заменяет__oct__ , __ hex__ из Python 2.Х)
__ enter__ , Диспетчер контекста (глава 34) with obj as var:
__ exit__

__ get__ ,__ set__ , Атрибуты дескриптора (глава 38) X.attr, X.attr = value, del X.attr
__ delete__

__ new__ Создание (глава 40) Создание объекта, перед
__ init__
'''
