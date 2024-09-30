#!/usr/bin/evn python
# -*- coding: utf-8 -*-
class NovoeIskluchenie(Exception):
    #def __init__(self,line):
        #self.line = line
        
    def __str__(self):
        return 'Здесь может быть то сообщение об ошибке которое вы захотите видеть'

try:
    raise NovoeIskluchenie('Инфа переданная экземпляру класса исключения') 
except NovoeIskluchenie as X: #перехватить и записать в переменную экземпляр
    print(X, X.args)#,X.line)

