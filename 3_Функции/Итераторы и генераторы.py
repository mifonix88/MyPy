#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#Итератор — это объект, который позволяет обойти все элементы коллекции (список, кортеж, словарь и т.д.).
#Генератор — это специальная функция, которая возвращает итератор.

'''
Функция не хранит своё состояние между своими вызовами, 
return ВОЗВРАЩАЕТ управление вызывающему коду.
yield в свою очередь, ПЕРЕДАЁТ управление вызывающему коду, но запоминает место и состояние (значение локальных переменных и т.п.)

Это позволяет в последствии возобновить исполнение кода в генераторе.
 
Значение справа от yield возвращается функцией next вызывающему коду. 
Исполнение кода в генераторе ставится на паузу до следующего вызова функции next.

Вообще говоря, у объекта генератора есть метод send, 
который позволяет не только получать объекты из генератора, 
но и передавать объекты из вызывающего кода в код генератора. 
Вызов этого метода тоже возобновляет исполнение генератора. 
Если g — объект генератора, то выражение g.send(None) в точности эквивалентно выражению next(g).
'''

#премеры генераторов
print(list(map((lambda x: x**2),range(10))))#выведет квадраты 0...9
print([x**2 for x in range(10) if x % 2 == 0])#Выведет список квадратов чётных
print(list(filter((lambda x: x % 2 != 0),range(10)))) #не чётных (выражение x % 2 != 0 ->если деление на 2 не даёт остатка)
print(list(map((lambda x: x**2),filter((lambda x: x % 2 == 0),range(10))))) #Выведет список квадратов чётных (очевидно что списки практичнее и короче)

#оператор for  в генераторе
print([x + y for x in [1,2,3] for y in [1,2,3]])

#оператор if в генераторе списков
print([(x,y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 == 1])

#матрицы(многомерные масивы) и генераторы
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

n = [[2,2,2],
     [3,3,3],
     [4,4,4]]
print([i[1] for i in m]) #вертикальный столбец
print([m[i][i] for i in range(len(m))]) #обращение к диагонале
print([[m[x][i] * n[x][i] for i in range(3)] for x in range(3)]) #Умножение элементов

#функция мап работает быстрее чек цикл фор и немного медленние чем генератор списков
#readlines возвращает строки с символом конца строки 'aaa\n'
'''
>>>open('myfile').readlines()
['aaa\n,']
'''
#авот с помощью генератора списков
'''
>>>[line.rstrip() for line in open('myfile')]
['aaa']
'''
#или с мап
'''
>>>list(map((lambda line: line.rstrip()),open('myfile')))
['aaa']
'''

#функции-генераторы:инструкция yield вместо return
#yield приостанавливает работу функции и передаёт значение вызывающей проге а потом продолжает работать с места где она остановилась а ретурн останавливает работу функции
def fungen(x):
    for i in range(x):
        yield i**3
print([i for i in fungen(100) if i % 2 == 0])

#методы send и next
def gen():
    for i in range(10):
        s = yield i
        print(s)
        
G = gen()
print(next(G))#К следующей итерации
print(next(G))
print(next(G))
print(next(G))
print(G.send(99)) #передаёт значение yield
print(G.send(88))

#выражения генераторы: итераторы, генераторы списков
print([i**2 for i in range(10)]) #генератор списков возвращает целиком список
print((i**2 for i in range(10)))   #выражение генератор возвращает итерируемый обьект
print(list((i**2 for i in range(10)))) #нужно присвоить или обернуть в лист()эквивалент генератора списков

#Функции и выражения генераторов
G = (i * 2 for i in 'qwerty')
print(G)
print(list(G)) #Автоматом всесь список
G = (i * 2 for i in 'qwerty') #в ручную
R = iter(G)
print(next(R))
print(next(R))
R2 = iter(G) 
print(next(R2))#чтобы обойти список заново нужно создать новый  генератор, присваивание ничего не меняет лишь продалжает итерации
print(next(R))
#как только любая итерация доходит до завершения, 
#все результаты оказываются израсходованными — чтобы начать сначала, 
#нам придется создать новый генератор

#То же самое остается справедливым для генераторных функций


#функции генераторы действуют точно также как выражения
def it(x):
    for i in x:
        yield i * 2
G = it('qwerty')
R,R2 = iter(G),iter(G)
print(next(R))
print(next(R))
print(next(R2))
print(next(R))

#некоторые типы имеют отличное поведение и отражают изменения обьекта во всех итераторах
L = [1,2,3,4]
R,R2 = iter(L),iter(L)
print(next(R))
print(next(R))
print(next(R2))
print(next(R))

#имитация функций zip map  помощью инструментов итерации
S = 'abc'
S1 = 'zxc123'
print(list(zip(S,S1))) #обьединяет элементы итерируемых последовательностей
print(list(zip([1,2,3]))) #одномерная последовательность
print(list(zip([1,2,3],[1,2,3,4,5]))) #N-мерная последовательность

#тоже самое но с map
print(list(map(abs, [1,2,3]))) #одномерная
print(list(map(pow,[1,2,3,4],[1,2,3,4,3])))#N-мерная

#реализация  функции map
def mymap(fun,*X):
    res = []
    for i in zip(*X):
        res.append(fun(*i))
    return res
print(mymap(abs,[1,2,3,4,5]))
#можно и с генератором списка бут компактнее и быстрее
def mymapp(fun,*X):
    return [fun(*i) for i in zip(*X)]
print(mymapp(abs,[1,2,5,6]))

#Однако эти два варианта возвращает весь список,
#А ниже возвращают обьект итерации
def myymap(fun,*X): #С яилд возвращает обьект
    res = []
    for i in zip(*X):
        yield fun(*i)
print(list(myymap(abs,[2,4,5,6])))

def myyymap(fun,*X):
    return (fun(*i) for i in zip(*X))
print(list(myyymap(pow,[8,9,0],[5,7,8,9,0])))

#Словари имеют свой итератор воспроизводящий за каждую итерацию ключ
D = {'a':1,'b':2}
x = iter(D)
print(next(x))
print(next(x))

for i in D:
    print(i,D[i])
#Кратка сводка по синтаксису генераторов
print([i for i in range(10)]) #генератор словарей list
print((i for i in range(10))) # выражение-генератор 
print({i for i in range(10)}) #генератор мнодеств set
print({i: i for i in range(10)})#генератор словарей dict

print([x+y for x in [1,2,3] for y in [2,3,4]])#упорядоченная коллекция
print({x+y for x in [1,2,3] for y in [2,3,4]}) #множества не упорядоченная и удаляет дубликаты



#хронометраж итерационных альтернатив
import time,sys  ###
reps = 1000
repslist = range(reps)

def timer(func, *pargs, **kargs):
    start = time.perf_counter()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.perf_counter() - start
    return (elapsed, ret)###

def onefor():
    res = []
    for i in repslist:
        res.append(abs(i))
    return res
def onelist():
    return [abs(i) for i in repslist]
def onemap():
    return list(map(abs,repslist))
def oneex():
    return list(abs(i) for i in repslist)
def onegen():
    def fun():
        for i in repslist:
            yield abs(i)
    return list(fun())


print(sys.version)
for i in (onefor,onelist,onemap,oneex,onegen):
    elapsed, result = timer(i)
    print('-' * 33)
    print(i.__name__, elapsed)

#типичные ошибки
#Пространством имён для интерактивной обольчки является модуль __main__
X = 11
import __main__
print(__main__.X)
def fun():
    X = 22
    print(X)
    print(__main__.X) #Обращение к переменной с такимже именем но в глобальном модуле
fun()

def sev(X=[]):
    X.append(1)
    print(X)
sev()
sev()
sev()#Значение по умолчанию меняется с каждым вызовом
#если необходимо лучше использовать более явную форму, хотя и не обязательно
def sevv():
    sevv.x.append(2)
    print(sevv.x)
sevv.x = []
sevv()
sevv()
#функции без return  и yield возвращают None
lis = [1,2]
lis = lis.append(3)
print(lis)#вернёт ноне а не новый список!


#Любая функция в Python, в теле которой встречается ключевое слово yield, называется генераторной функцией — при вызове она возвращает объект-генератор.
#Объект-генератор реализует интерфейс итератора, соответственно с этим объектом можно работать, как с любым другим итерируемым объектом.
#при вызове функции создается объект-генератор
#for вызывает iter() с этим объектом и получает итератор этого генератора
#в цикле вызывает функция next() с этим итератором пока не будет получено исключение StopIteration
#при каждом вызове next выполнение в функции начинается с того места где было завершено в последний раз и продолжается до следующего yield


def gen(arg):
    for i in range(arg):
        yield i*2

print(list(gen(3)))

for i in gen(3):
    print('##',i)



###########
'''
Метод send можно применять, например, для написания генератора, 
который разрешает прекращать свою работу за счет отправки кода 
завершения либо изменять направление путем передачи новой позиции в данных, 
обрабатываемых внутри генератора.
'''
def gen():
    for i in range (10) :
        X = yield i 
        print(X) #Когда используется такой расширенный протокол, значения отправляются генератору G
G = gen()
next(G)
print(G.send(22))
print(G.send(33))
#close, который инициирует специальное исключение GeneratorExit внутри генератора
G.close()

try:
    print(G.send(33))
except(StopIteration):
    print('StopIteration')

G = gen()
A , B = iter(G), iter(G)
print(next(A))
print(next(B))#B находится в тойже позиции что и А
print(next(A))
print(next(B))

#Встроиные типы ведут себя иначе (поддерживают более одной активной итераци)
L = [10,20,30,40]
a, b = iter(L), iter(L)

print(next(a))
print(next(b))
print(next(a))
print(next(b))

###########yield from
def both(N) :
    for i in range (N) : yield i
    for i in (x ** 2 for x in range (N)) : yield i
    
def both(N) :#тоже самое но в новой записи с версии 3.3 ПРОЧИТАТЬ в документации
    yield from range (N)
    yield from (x ** 2 for x in range (N))


#перемешивание последовательностей
def permute2(seq): 
    if not seq: 
        yield seq 
    else:# 
        for i in range(len(seq)): 
            rest = seq[:i] + seq[i+1:]
            for j in permute2(rest): #рекурсивно вызывает себяже
                yield seq[i:i+1] + j 
q = permute2('qwer')
print(list(q))
q = permute2([1,2,3])
print(list(q))

a = [1,2,3,4,5,6,7,8,9,10]#количество перестановок равно факториалу,
import math
print('@@@@',math.factorial(10))

q = permute2(a)#3,6 миллиона элементов, но функция permute2 может начать возвращение результатов незамедлительно:
print(next(q))
print(next(q))
print(next(q))

import random
seq = list(range(20))
random.shuffle(seq)#Предварительно перетасовать последовательность
q = permute2(seq)
print(next(q))
print(next(q))
print(next(q))
#Суть здесь в том, что генераторы иногда способны производить результаты из крупных наборов решений,
# тогда как построители списков — нет.


def mymap(func, *seqs): #аналог map возвращают генераторы, предназначенные для поддержки протокола итерации
    return (func(*args) for args in zip(*seqs))
a = mymap(abs, [-2, -1, 0, 1, 2])
print(next(a))
print(list(a))


q = 99
[q for q in range(5)]#генераторы и включения множеств, словарей и списков локализуют имена переменных
print('q1',q)

for q in range(5): #for не локализует
    pass
print('q2',q)

#Обратите внимание, что хотя включения множеств и словарей принимают и просматривают итерируемые объекты, 
#в них отсутствует понятие генерации результатов по запросу — обе формы строят сразу полные объекты.
#Если вы намереваетесь выпускать ключи и значения по запросу, тогда больше подойдет генераторное выражение:
    
#Генераторы представляют собой итерируемые объекты, автоматически поддерживающие протокол итерации
