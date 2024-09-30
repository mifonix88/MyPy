#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#полиморфизмом — термин, указывающий на то, что смысл операции зависит от типа объектов, на которых она выполняется.
#т.е один и тот же метод может выполнять разные действия в зависимости от типа данных который он получил.
#при этом сам метод к типу данных строго не привязан.

#инкапсуляция — помещение операционной логики
#в оболочку интерфейсов, чтобы код каждой операции был написан только один раз в
#программе.

#Инкапсуляция означает пакетирование в Python, т.е. сокрытие деталей реализации
#за интерфейсом объекта.


'''
Наследование
Наследование основано на поиске атрибутов в Python (в выражениях X.name).
Полиморфизм
В выражении X.method смысл method зависит от типа (класса) подчиненного
объекта X.
Инкапсуляция
Методы и операции реализуют поведение, хотя сокрытие данных по умолчанию
является соглашением.
'''
'''
С этой целью программисты начали каталогизировать распространенные
структуры ООП, известные как паттерны проектирования, которые
призваны помочь в решении проблем, возникающих при проектировании.
'''


#просто замените имена существительные классами
#(скажем, Oven), а глаголы методами (например, bake), и вы получите первое приближение
#к проектному решению.

class VseImena():
    def Name(self,name):
        self.name = name
        
I1 = VseImena()
I1.Name('Nady')
I2 = VseImena()
I2.Name('Koly')
print(I1.name,I2.name)

try:
    I3 = VseImena('vasy') #чтобы гарантировать что имена будут во всех экземплярах класса нужно присваивать их на стадии создания класса(чтобы каждый раз не вызывать I1.Name....)
except(TypeError): print('ошибка')

#вот так
class VseImena1():
    def __init__(self, imy):
        self.name = imy
        
j1 = VseImena1('Vasilij')
print(j1.name)

#наследование и полиморфизм
class ZarplataBogov():
    def __init__(self,imy, none = None):
        self.name = imy
        self.none = none
    def nachislit(self,deneg):
        self.zarabotal = 100*deneg

class ZarplataRabov(ZarplataBogov):
    
    def __init__(self, arg):
        ZarplataBogov.__init__(self, arg, 123) #существующий метод с новыми входными

    def __repr__ (self): # Добавленный метод
        return '@@@Инфа %s] ' %  self.zarabotal# Строка для вывода
    
    def nachislit(self,deneg): #переопрпеделяет метод (Это плохой тон!)
        self.zarabotal = 2*deneg
    
    def nachislit(self,arg, bonus): #Правильнее вызвать существующий метод с новыми входными 
        #В будущем будет легче сопровождать
        #если переопределить то предётся переписывать везде
        '''
        Если более конкретно, то вспомните, что нормальный
        вызов метода следующего вида:
        экземпляр.метод (аргументы. . .)
        автоматически транслируется Python в такую эквивалентную форму:
        класс .метод (экземпляр, аргументы. . .)
        '''
        ZarplataBogov.nachislit(self, arg + bonus)






rab1 = ZarplataBogov('Koly')
rab2 = ZarplataBogov('Nady')

wse = [rab1,rab2]
[i.nachislit(101) for i in wse]
print(rab1.name,'получил..',rab1.zarabotal,rab2.name,'получил..',rab2.zarabotal)

Ya = ZarplataRabov('Ya')
Ya.nachislit(200, 5)
print(Ya) #результат работы__repr__
print(Ya.none)


class One():
    '''
    Класс One определяет метод fanc и ожидает его заполнения подклассами;
    он является примером модели абстрактных суперклассов
    '''
    def __init__(self,arg, arg2):
        self.arg = arg
        self.arg2 = arg2

    def process(self):
        data = self.func()
        print(data)

    def func(self):
        assert False, 'Метод не определён'

class Too(One):#pass
    def func(self):#если не определить метод вызовется исключение #assert False, 'Метод не определён'
        return self.arg, self.arg2

x = Too(1,2)
x.process()

class HTMLize(One):
    def func(self):
        return '<PRE>%s</PRE>' % self.arg
        
a = HTMLize(3,4)
a.process()
#основной логике обработки в исходном суперклассе
#One ничего не известно ни об одном, ни о другом шаге. (Пример композиции)






#Объект type генерирует классы как свои экземпляры, а классы генерируют экземпляры
#самих себя.


class A:pass
class B:pass

print(A==B) #False
a=A()
b=B()
print(a==b) #False

print(type(a)==type(b))#False
print(a.__class__, b.__class__)

#по причине того, что теперь все типы — это классы,
#каждый объект оказывается производным от встроенного класса object,
print(isinstance(A, object)) #True
print(A.__bases__)#все кдассы насдедуют  методы из object 
print(dir(object))

print(dir(A))

print(type(A)==type(B))#True
c=A()
print(a==c) #False



print(type(a)==type(c)) #True

#
