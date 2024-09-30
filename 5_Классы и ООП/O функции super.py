# super иногда можно использовать когда используется очень длинный путь ссылки на суперклассы через пакет модуля
#но лучше 2 раза подумать перед использованием


'''
Изменение деревьев классов во время выполнения. Когда суперкласс способен
изменяться во время выполнения, то невозможно жестко закодировать его
имя в выражении вызова, но вызовы можно координировать с помощью super.
'''
#С.__bases__ = (Y,) # Изменить суперкласс во время выполнения'.

class A:
    def __getitem__(self, arg):
        print('A index')
    
    def func(self):
        print('A')

    def func2(self):
        print('A2')
    
class B:
    def func(self):
        print('B')

class C(A):
    def func(self):
        super().func()


x = C()
x.func()


class C(B, A): 
    def func(self):
        super().func() #Сначало будет искать в крайнем левом (согласно MRO) суперкласе 'В'
        #A.func(self) лучше вызывать по имени если это возможно (явное лучше неявного)

x = C()
x.func()
x.func2()



class C(A): 
    def __getitem__(self, arg):
        A.__getitem__(self, arg)
        super().__getitem__(arg)
        #super()[arg] #такая форма не работает
        '''
        Поскольку промежуточный
        объект, возвращаемый super, использует__ getattribute__ для захвата и
        маршрутизации последующих вызовов методов, ему не удается перехватывать автоматические
        обращения к методам формата __ X__
        '''

x = C()
x[2]


############################
print('############################')
class A():
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        A.__init__(self)

class C(A):
    def __init__(self):
        print('C')
        A.__init__(self)

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

x = D() #A - будет вызываться дважды!
#эту задачу решает super


print('############################')

class A():
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class D(B, C):
    def __init__(self):
        super().__init__()
        
x = D()
#Реальной магией, стоящей за этим, является линейный список MRO
print(D.__mro__)

#с super связано много проблем гугли перед использованием

'''
p.s
Если реализацию сложно объяснить, то она считается плохой идеей.
'''
