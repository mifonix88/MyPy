#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
#Классы теперь являются типами, а типы — классами. Это синонимы
class I:pass

print(type(I) == I.__class__)



def tt():
    return True
print(tt()+1, 'Ахуеть') #bool
print(dir(object)) #все классы наследуют класс object
class Q:
    __slots__ = ['a']#не возможно добавить отребет если его нет в списке (отсутсвует __dict__)
q = Q()
q.a = 1
print(q.a)


'''
Функции преобразования типов вроде list, str, dict и tuple
стали именами встроенных типов — несмотря на прозрачность для вашего сценария,
вызов преобразования типа (скажем, list (’ spam')) теперь на самом деле представляет
собой обращение к конструктору объектов типа.
'''

class MyList(list):
    '''
    меняет линию поведения списков
    расширяет только метод индексирования__ getitem__
    '''
    def __getitem__ (self, offset):
        return list.__getitem__(self, offset - 1)

SL = MyList([1,2,3])
print('первое', SL[1])
print(MyList('первое')[3])
