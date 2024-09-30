#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
class Decor:
    def __init__(self,fun):
        self.nom = 0
        self.fun = fun
    def __call__(self,*arg):
        self.nom +=1
        print('%s,%s' % (self.nom,self.fun.__name__))
        self.fun(*arg)
@Decor#декоратор реалезует дополнительную логику
def func(*arg):
    print(arg)
func('1','d')
func(1,2,3)
func('Оп)')
