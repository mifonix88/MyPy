#1159
#тип экземпляра это класс  из которого он был получен
#Все классы в пайтон это экземпляры класса type
#print(type([]))
#print(type(''))
#print(type(type))
##########################################################
#основы
#[Метаклассы] — это более темная магия, которая не касается 99% пользователей.
'''
Хотя
механизм метаклассов сильно напоминает декораторы классов, он не привязывает
имя класса к результату, возвращенному вызываемым объектом декоратора, а взамен
поручает процедуру создания самого класса специализированной логике.

Чтобы взять на себя контроль над созданием либо инициализацией нового объекта
класса, в метаклассе обычно переопределяется метод__ new__ или__ init__ класса
type, который в нормальных условиях перехватывает данный вызов.



Другими словами, мы
бы хотели иметь возможность вставлять какой-то код, подлежащий автоматическому
запуску в конце оператора class для дополнения класса.



Поскольку интерпретатор Python автоматически активизирует метакласс в конце
оператора class, когда новый класс создан, он может необходимым образом дополнять,
регистрировать или по-другому управлять классом. Кроме того, единственное
требование для клиентских классов заключается в том, что они объявляют метакласс;
каждый класс, который так поступает, автоматически получит любое дополнение,
предоставляемое метаклассом, и теперь, и в будущем, если метакласс изменится.
'''

#• type является классом, который генерирует классы, определяемые пользователем;
#• метаклассы представляют собой подклассы класса type;
#• объекты классов являются экземплярами класса type или какого-то из его подклассов;
#• объекты экземпляров генерируются из класса.
#Другими словами, для управления способом создания классов и дополнения их поведения
#нам необходимо лишь указать, что определяемый пользователем класс должен создаваться
#из определяемого пользователем метакласса, а не нормального класса type.
#Обратите внимание, что такое отношение между типом и экземпляром не вполне

'''
Говоря формально, чтобы это произошло, интерпретатор Python следует стандартному
протоколу: в конце оператора class и после выполнения всего вложенного в него
кода в словаре пространств имен, соответствующем локальной области видимости
класса, Python обращается к объекту type для создания объекта класс:
класс = type {имя_класса, суперклассы, словарь_а трибутов)
'''
#сначало вызывается __call__
#он вызывает __new__ и __init__ ###Метод__ new__ создает и возвращает новый объект класс, после чего метод __ init__ инициализирует вновь созданный объект.

#инструкция class по сути представляет собой вызов функции type
#х = type( 'func' , () , { 'data' : 1, 'meth' : (lambda x, y: x.data + y)})
#где класс = type {имя_класса, суперклассы, словарь_а трибутов)

class Meta(type):
    def __new__(meta, classname, supers, classdict):#вызывается методом __call__ унаслежованым от type
        print('итак', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):#тоже автоматом вызывается
        print('и ещё', classname, supers, classdict, sep='\n...')
        print(Class.__dict__.keys())
class One(metaclass=Meta):
    op = 'Ok'
    def onOp(self):pass 

Q = One()
print(Q.op)

#рольметакласса может играть и функция
#def Meta(classname, supers, classdict):
#    return type(classname, supers, classdict)
#######################################################################
#Если нужно добавить во все классы нечто 
test = True#False
def func(self):
    print('А вот и метод')
    return self.arg * 3

class MetaKL(type):
    def __new__(meta, classname, supers, classdict):#вызывается методом __call__ унаслежованым от type
        if test == True:
            classdict['arg'] = 'Добавлен атрибут '
            classdict['func'] = func
        else:
            classdict['arg'] = 'Всяко бывает'
            classdict['func'] = lambda *arg:'нет такого метода'
        return type.__new__(meta, classname, supers, classdict)

class Op(metaclass=MetaKL):pass

class Op1(Op):pass 

Q = Op1()
print(Op.arg)
print(Q.arg)
print(Q.func())
###################################################################
#Некая логика при обращении к атрибутам (выводит сообщения)
def metaOne(classname, supers, classdict):
    aClass  = type(classname, supers, classdict)
    class Too:
        def __init__(self,*arg):
            self.op = aClass(*arg)
        def __getattr__(self, atrname):
            print('Сообщение от',atrname)
            return getattr(self.op, atrname)
    return Too

class Opa(metaclass=metaOne):
    def __init__(self,i):
        self.i = i
    def fun(self):pass

class Opa1(Opa):pass 

QW = Opa1('Hi')
QW.e = 13
print(QW.i)
print(QW.fun())
#####################################################################
#Применение произвольного декоратора ко всем методам класса
from types import FunctionType
import time

def decor(func):
    def one(*arg):
        print('Получилось декорировать все методы по средствам метокласса')
        return func(*arg)
    return one

def timer(func):
    def Timer(*arg):
        start = time.perf_counter()
        result = func(*arg)
        finish = time.perf_counter() - start
        print(func.__name__,'проработала:','%.4f' % finish)#%.4f количество знаков после запятой
        return result
    return Timer

def MetaAll(decorat):
    class MetaDecor(type):
        def __new__(meta, classname, supers, classdict):
            for atr,atrv in classdict.items():
                print(atr,atrv)
                if type(atrv) is FunctionType:#Метод?
                    classdict[atr] = decorat(atrv)#Декорировать
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecor

class Test(metaclass=MetaAll(decor)):
    def fun(self):pass
    def fun1(self):pass 
ABC = Test()
ABC.fun()
ABC.fun1()

class Test1(metaclass=MetaAll(timer)):
    def fun(self):
        [i**2**2**2 for i in range(100000)]
    def fun1(self):
        U = []
        for i in range(100000):
            U.append(i**2**2**2)
ABC = Test1()
ABC.fun()
ABC.fun1()

'''
• Поскольку декораторы запускаются после создания класса, в ролях с созданием
классов они влекут за собой дополнительный шаг во время выполнения.
• Поскольку метаклассы должны создавать классы, в ролях с управлением экземплярами
они влекут за собой дополнительный шаг на этапе реализации.
'''
