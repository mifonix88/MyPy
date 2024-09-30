class NewErr(Exception):
    
    def __init__(self, arg):
        self.arg = arg #храним какуюто инфу при исключении
    
    def __str__(self):
        return 'Error!!!' 

    def __repr__ (self): 
        return 'Not Err' # He вызывается !
    
    def func(self):
        return 'можно и так'


class OneErr(NewErr):pass


try:
    raise OneErr('инфа')
except OneErr as arg:
    print(arg)
    print(arg.arg)
    print(arg.func())

import sys
print(sys.exc_info()) #возвращает информацию о самом недавнем исключении.


'''
BaseException: самый верхний корень со стандартным
методом вывода и конструктором
Exception: корень определяемых пользователем исключений
ArithmeticError: корень численных ошибок
LookupError: корень ошибок индексирования


указывая в try исключение ArithmeticError, вы будете перехватывать возникшую
численную ошибку любого вида;
указывая в try исключение ZeroDivisionError, вы будете перехватывать только
ошибку этого конкретного типа, но не другие.
'''
