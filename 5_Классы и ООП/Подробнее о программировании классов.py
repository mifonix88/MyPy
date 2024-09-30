#!/usr/bin/evn python
# -*- coding: utf-8 -*-
class ObjectOne:
    one = 11
    text = 123456
    def metod(self, text):
        self.text = text
        print('метод один')
    def metod3(self):
        self.metod2()#ожидаемый метод
x = ObjectOne()
y = ObjectOne()
print(y.one,x.one,ObjectOne.one)#обращение к атребутам класса через экземпляр и через класс
ObjectOne.one = 99
print(y.one,x.one,ObjectOne.one)
x.one = 11
print(y.one,x.one,ObjectOne.one)
print(x.text)

x.metod('оп')#вызов метода через экземпляр и через класс
print(x.text)
ObjectOne.metod(x, 'ля')
print(x.text)
'''строки документации'''
class ObjectToo(ObjectOne):
    '''Можно размещать'''
    def metod(self):
        '''в разных местах'''
        print('о-ля-ля метод два вызвал')
        ObjectOne.metod(x,'Xoxo')#Всегда можно обратится к методу суперкласса нужно лишь явно передать экземпляр
    def metod2(self):
        print('Вызван ожидаемый метод')
x = ObjectToo()
x.metod3()


print(x.__dict__)#Пространство имён атрибута
print(x.__class__)#предоставляет ссылку из экземпляра на класс, из которого экземпляр был создан.
print(x.__class__.__name__) #Имя класса
print(ObjectToo.__bases__)#суперклас класса
print(ObjectOne.__bases__)#
print(ObjectToo.__doc__,ObjectToo.metod.__doc__)#вывод коментариев


######################################
print('####################')
#Особенности
class A:
    arg = 1
    ls = []

a = A()
print(a.arg)
a.arg = 2
print(a.arg)#изменяется только для экземпляра 
print(A.arg)

A.arg = 123 #Изменится для всех вновь создаваемых!

b = A()
print(b.arg)
print(a.arg) 

#если атребут ссылается на изменяемый объект его изменение отразится на всех экземплярах!!
b.ls.append(321)
print(b.ls)
print(a.ls)
