
def decorator(F):
    # Обработка функции F или метода экзкмпляра сам экземпляр хранится в args[0]
    def func_dekor(*args):
        args = ('123 ' + args[0],)
        F(*args)
    return func_dekor
    
    
@decorator # эквивалентно func = decorator (func)
def func(arg) :
    print(arg) 
#Когда позже происходит обращение к имени func, в действительности вызывается
#функция func_dekor, возвращенная декоратором
func('Ok')




def decor(func):#как для функций так и для методов классов
    cal = 0
    def funk(arg):
        nonlocal cal
        cal  +=1 
        print(cal)
        return func(arg * 2)
    return funk
    
@decor
def funk(i):
    return i
@decor
def funk1(i):#щётчик один на всех
    return i

print(funk(12))
print(funk('qwe'))
#######################################################################
class Decor:#для декорирования функций для методов класса терпит неудачу используй вложеную функцию
    def __init__(self,func):
        self.cal = 0
        self.func = func
    def __call__(self,*arg):
        self.cal +=1
        print('cal %s' % self.cal)
        return self.func(*arg)

#Когда позже происходит обращение к имени fun, то в действительности вызывается
#метод перегрузки операций__ call__ экземпляра, созданного декоратором
#Decor; метод__ call__ затем запускает исходную функцию fun,

@Decor
def fun(*i):
    return sum(*i)
@Decor
def fun1(*i):
    return sum(*i)
print(fun([12,23,4]))
#print(fun.cal)
print(fun([12,23,6]))
print(fun1([7,9]))#у каждой функции свой счётчик

##########################################################################
#Пример использования декоратора для проверки скорости
#дикоратор принимает аргументы
import time

'''
Аргументы декораторов могут применяться при предоставлении значений для инициализации
атрибутов, сообщений с трассировкой вызовов, имен атрибутов, подлежащих
проверке допустимости, и многого другого — сюда входят конфигурационные
параметры любого вида для объектов либо их посредников И ТП.
'''
def timer(i=True):
    class Timer:#чтобы можно было использовать к методам класса нужно влоденый класс переделать в функцию
        def __init__(self,func):
            self.func = func
        def __call__(self,*arg):
            start = time.perf_counter()
            result = self.func(*arg)
            finish = time.perf_counter() - start
            if i:
                print(self.func.__name__,finish)
            else:
                print(self.func.__name__,'шиш тебе!')
            return result
    return Timer

@timer()
def onList(N):
    return [i ** 2 for i in range(N)]
@timer(i=False)
def onMap(N):
    return list(map((lambda x: x**2),range(N)))
onList(1000000)
onMap(1000000)

##########################################################################
#декорирование классов
'''
Из-за того, что декораторы классов способны перехватывать вызовы, создающие
экземпляры, они могут использоваться либо для управления всеми экземплярами класса,
либо для дополнения интерфейсов этих экземпляров.
'''

#Пример когда нужно получить только один экземпляр класса независимо от кол-ва проб создания нового
class Singleton:
    def __init__(self,aClass): #вызывается при декорировании
        self.aClass = aClass
        self.instance = None
    def __call__(self,*arg):  #при создании экземпляра
        if self.instance == None:
            self.instance = self.aClass(*arg)
        return self.instance
        
@Singleton
class One:
    def __init__(self,i):
        self.i = i
Q = One(11)
print(Q.i)
W = One(12)
print(W.i)

##########################################################################
#перехват обращения к атребутам (декоратор для классов)
#следующий декоратор вставляет объект, который
#перехватывает доступ к неопределенным атрибутам экземпляра класса:
def tracer(aClass):
    class New:
        def __init__(self,*arg): #При декорировании @
            self.new = aClass(*arg) #в new будет храниться экземпляр исходного класса
        def __getattr__(self,atrname): #При извлечении атрибутов
            print('Вызван: '+ atrname)
            return getattr(self.new, atrname)
    return New
'''
В коде обрабатывается множество декорированных классов (каждый создает новый
экземпляр Decorator) и перехватываются вызовы, создающие экземпляры (каждый
запускает метод__ call__ ). Тем не менее, в отличие от предыдущей показанная
выше версия терпит неудачу при обработке множества экземпляров заданного класса —
каждый вызов, создающий экземпляр, переписывает ранее сохраненный экземпляр.
'''


@tracer
class Person:
    def __init__(self, kl,zn):
        self.kl = kl
        self.zn = zn
    def pay(self,i):
        return self.kl * i

#эквивалент A = tracer(Person)(12,67)
A = Person(12,67) #В действительности вызывается New(12,67) 
B = Person(1,78)
print(A.kl)

A.rty = 10
print('@@@@@@@',A.rty)

print(A.zn)
print(B.pay(99))

print('#####',A.new) #Отдельная область памяти!!
print('#####',A.new.kl)


##############################################################
def anatacy(text):
    def decor(fun):
        fun.anatace = text
        return fun
    return decor
    
@anatacy('Можно добавить чё нить')
def R():
    return 'Ok'
print(R(),R.anatace)
#итп....

##############################################
#можно хранить входные параметры
def anat(fun):
    def decor(text):
        print(text)
        decor.anatace[decor.call] = text
        decor.call +=1
        return fun
    decor.call = 0
    decor.anatace = {}
    return decor

@anat
def R(arg):
    return 'Ok'
R('qwertyuiop')
R('poiuytrewq')
print(R.anatace)


class Methods (object) : # Для методов установки свойств в Python 2.Х # необходим object
    def imeth(self, x) : # Нормальный метод экземпляра: передается self
        print([self, x])
    
    @staticmethod #staticmethod и родственные инструменты по-прежнему являются функциями!
    def smeth(x) : # Статический метод: экземпляр не передается
        print([x])
    #можно было сделать и такЖ
    #smeth = staticmethod(smeth(x))
        
    @classmethod
    def cmeth(cis, x): # Метод класса: получает класс, не экземпляр
        print([cis, x])
        
    @property # Свойство: значение вычисляется при извлечении
    def name(self):
        return 'Bob ' + self.__class__.__name__
    

a = Methods()
a.imeth(1)
a.smeth(2)
a.cmeth(3)
print(a.name)

#Вложение декораторов
'''
@А
@В
@С
def f(. . .) :

выполняется аналогично такому синтаксису:

f = А (В (С (f) ) )

'''

#в качестве промежуточного состояния можно использовать Атрибуты функций
#как пример, подсчёт количества вызова функции
def decor_sl(func):
    def func_dec(*args):
        func_dec.sl += 1
        return func(*args)
    func_dec.sl = 0
    return func_dec

@decor_sl
def a():pass
@decor_sl
def b():pass

a()
a()
print(a.sl)
[a() for i in range(10)]
print(a.sl)
print(b.sl)


#можно использовать и для классов и их методов
@decor_sl
class Test():
    @decor_sl #счётчик один для всех екземпляров!! доступен self.name_atrebut.sl
    def a(self):
        pass
    @decor_sl
    def r(self):
        pass
        
a = Test()
a.a()
a.a()
print('.r. вызванно раз ',a.r.sl)

b = Test()
b.a()
print('.a. вызванно раз ',b.a.sl)

c = Test()
c.a()
c.r()
c.r()

print('.a. вызванно раз ',c.a.sl)
print('.r. вызванно раз ',c.r.sl)

print('создано экземпляров',Test.sl)

#дискриптор для декорирования
'''
Вспомните из нашего обсуждения в той главе, что дескриптор обычно представляет
собой атрибут класса, которому присваивается объект с методом__ get__ , автоматически
запускаемым всякий раз, когда производится ссылка и извлечение атрибута.
'''
class tracer(): # Декоратор + дескриптор
    def __init__ (self, func) : 
        self.calls = 0 # При декорировании 0
        self.func = func # Сохранение функции для вызова в будущем
    def __call__ (self, *args, **kwargs) : # При обращении к исходной функции
        self.calls += 1
        print('вызвано раз %s метод %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__ (self, instance, owner) : # При извлечении атрибутов методов
        return Wrapper(self, instance)

class Wrapper:
    def __init__ (self, desc, subj): # Сохранение обоих экземпляров
        self.desc = desc # Направление вызовов декоратору/дескриптору
        self.subj = subj
    def __call__ (self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)

@tracer
class Test():
    @tracer 
    def a(self):
        pass
    @tracer 
    def r(self):
        pass

c = Test()
c.a()
c.a()
c.r()
d = Test()
d.a()
print('экземпляров',Test.calls)
print('вызовов .a.',d.a.desc.calls)



################Аргументы декоратора
def fun_arg(arg=0):
    def decor_sl(func):
        def func_dec(*args):
            func_dec.sl += 1
            return func(*args)
        func_dec.sl = arg
        return func_dec
    return decor_sl
    
@fun_arg()
class Test():
    @fun_arg(100) #счётчик один для всех екземпляров!! доступен self.name_atrebut.sl
    def a(self):
        pass
    @fun_arg()
    def r(self):
        pass
        
a = Test()
a.a()
a.a()
print('.a. вызванно раз ',a.a.sl)


###############################
#Закрытые атребуты через декоратор
traceMe = False

#Декоратор Private объявляет атрибуты экземпляров класса, которые нельзя
#извлекать или присваивать им значения кроме как внутри кода методов класса.

def Private(*privates) : # privates в объемлющей области видимости
    def onDecorator(aClass): # aClass в объемлющей области видимости
        class onlnstance: # wrapped в атрибуте экземпляра
            def __init__ (self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__ (self, attr): # Для собственных атрибутов
                if attr in privates:
                    raise TypeError(f'невозможно получить доступ к "{attr}"')
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__ (self, attr, value): # Операции доступа извне
                if attr == 'wrapped' : # Разрешить доступ к собственным
                    # а трибутам
                    self.__dict__[attr] = value # Избежать зацикливания
                elif attr in privates:
                    raise TypeError(f'невозможно получить доступ к "{attr}"')
                else:
                    setattr (self .wrapped, attr, value) # Атрибуты внутреннего объекта
        return onlnstance # Либо использовать __diet__
    return onDecorator
'''
Аргументы декоратора
Реализованный здесь декоратор класса принимает любое количество аргументов
для указания имен закрытых атрибутов. Тем не менее, в действительности эти аргументы
передаются функции Private, которая возвращает декораторную функцию,
предназначенную для применения к целевому классу. То есть аргументы используются
даже до того, как происходит декорирование; Private возвращает декоратор, который
в свою очередь “запоминает” список закрытых атрибутов как ссылку из объемлющей
области видимости.



А теперь, когда потрачено столько усилий для реализации объявлений атрибутов
Private и Public в коде Python, я обязан снова напомнить вам о том, что такое
добавление в классы средств контроля доступа совершенно не соответствует стилю
программирования на Python. На самом деле большинству программистов на Python
данный пример покажется почти или вообще полностью неуместным, не считая демонстрации
декораторов в действии. Большинство крупных программ на Python успешно
обходятся вообще без средств контроля доступа подобного рода.
'''


@Private('arg','a')
class Test():

    def __init__(self):
        arg = 123

    def a(self):
        print(123)
q = Test()

try:
    q.arg = 12
except(TypeError) as arg:
    print(arg)
#########################################################################
#Управляет классом, не экземпляром
#Эквивалентно методу__init__ метакласса

def func_123(self):
    print('123 Добавлен!!! Ok')

@staticmethod
def func_321():
    print('321 Добавлен!!! Ok')

def Extender(aClass) :
    aClass.func_123 = func_123
    aClass.func_321 = func_321
    return aClass

@Extender
class Pass:
    pass

a = Pass()
a.func_123()
a.func_321()
