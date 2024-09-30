#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#Принцип: Замени имена существительные на классы, а глаголы на методы и пол дела уже в шапке

class Sokr:
    def __init__(self,X):
        self.__X = X  #двойное подчёркивание изменит имя обьекта __Х на _Sokr__X Что помогает избежать конфликтов имён в дереве наследования
    def func(): #Этот метод можно получить только через имя класса
        print('получилось')
    def func1(self,q):
        print(self.__X*q)#если метод ожыдает аргумент селф то придётся явно передать имя экземпляра при вызове через имя класса
        print('Ok')
if __name__ == '__main__':
    y = Sokr(1)
    #print(X)  Выведет ошибку(такого атрибута не существует(но его легко можно создать;))
    print(y._Sokr__X)
    Sokr.func()
    Sokr.func1(y,45)
    


    y.func1(12)
class Pro(Sokr): pass
e = Pro(44)
e.func1(44)


'''
Временами проектные решения на основе классов требуют создания объектов в
ответ на условия, которые невозможно предсказать на стадии написания кода программы,
Паттерн проектирования “Фабрика”
'''

def factory(aClass, *pargs, **kargs): # Кортеж или словарь с переменным # количеством аргументов
    return aClass(*pargs, **kargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__ (self, name, job=None):
        self.name = name
        self.job = job

objectl = factory(Spam) # Создать объект Spam
object2 = factory (Person, "Arthur", "King") # Создать объект Person
objects = factory (Person, name= ' Brian')
objectl.doit('12351261346sdf3')
print(object2.name)



#Подмешивание классов
class Podmes:
    '''
    Обобщенный инструмент тестирования подмешиваемых классов вывода списков:
    он похож на средство транзитивной перезагрузки модулей из главы 25 первого
    тома, но ему передается объект класса (не функции), а в testByNames
    добавлена загрузка модуля и класса по строковым именам в соответствии с
    паттерном проектирования 'Фабрика’.
    '''
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted (obj.__dict__ ) :
            if attr.startswith('__') and attr.endswith('__ '):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                                                                    dots,
                                                                    aClass.__name__ ,
                                                                    id(aClass))
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
        for super in aClass.__bases__:
            above += self.__listclass(super, indent+4)
        return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                                                                dots,
                                                                aClass.__name__ ,
                                                                id(aClass),
                                                                here, 
                                                                above,
                                                                dots)
    def __str__ (self) :
        self.__visited = {}
        here = self.__attrnames (self, 0)
        above = self.__listclass(self.__class__ , 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
                                                        self.__class__.__name__ ,
                                                        id(self) ,
                                                        here, 
                                                        above)



from tkinter import Button # Оба класса имеют метод__str__

class MyButton(Podmes, Button): pass #но так как Podmes стоит раньше будет использовать ся его метод __str__ из него

B = MyButton(text = 'ok')
#print(B)
st = str(B)
print(st[:100])#вывести первые 100 знаков

class Pass(Podmes, Sokr):pass

V = Pass(1)
print(V)


#Собирающий модуль
from name_module_1 import name_class_1 as new_name_1
from name_module_2 import name_class_2 as new_name_2
from name_module_3 import name_class_3 as new_name_3
#объединяет их в единое пространство
#имен — импортирование только одного этого модуля открывает доступ сразу
#ко всем трем подмешиваемым классам:

#Python часто делает гибкие API-интерфейсы инструментов почти автоматическими.
