#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#Более реалистичный пример
class Proverka:
    def func(self):
        return ', '.join(['%s = %s' % (i,self.__dict__[i]) for i in sorted(self.__dict__)])
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__,self.func())
        
class Person(Proverka):
    def __init__(self,name,job = None,pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def fomile(self):
        return self.name.split()[-1]

    def premiy(self,proz = 0):
        return int(self.pay * (1 + proz))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)

    def premiy(self, proz = 0, bonus = .50):
        return Person.premiy(self, proz + bonus)        

if __name__ == '__main__':

    import shelve
    baza = shelve.open('baza_dannyh')
    print(len(baza),'записи')
    print(list(baza.keys()))
    Michail_Popov = baza['Michail Popov']
    print(Michail_Popov)
    for i in baza:
        print(baza[i])
    '''
    mika = Person('Michail Popov',job = 'Rabochii',pay = 10000)
    lika = Manager('Viktoriy Lomakina',10000)
    sue = Person('Nekto')
    print('...All_person...')
    for i in (mika,lika,sue):
        print(i.name)
    print('...All_infa...')
    for i in (mika,lika,sue):
        i.pay = i.premiy(.30)
        print(i)
    
#инструменты интроспекции
    print(mika.__class__)#Выведет класс экземпляра
    print(mika.__class__.__name__)
    print(list(mika.__dict__.keys()))#Атребуты это ключи словаря
    [print(i,mika.__dict__[i]) for i in mika.__dict__]#Атрибуты экземпляра
    print(dir(mika))#Все атребуты включая методы типа класса
    '''
