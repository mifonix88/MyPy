import os

#zip
#map
#filter
#в отличие от range они являются собственными
#итераторами — результаты после однократного прохода по ним израсходуются

A = [1,2,3]
B = [4,5,6]
C = {1:'qet', 2:23}

print(list(zip(A,B))) #возвращает серию кортежей из параллельных элементов,


Tl, Т2, ТЗ = (1,2,3) , (4,5,6), (7,8,9)
print(list(zip(Tl, Т2, ТЗ))) # Три кортежа для трех аргументов

R = (1.2, 2.1)
T = (1.1, 2.2)
W, E = zip(*zip(R, T)) # Развертывание сжатых кортежей!
print(W,E)

print(list(enumerate(B)))  #генерирует список картежий (смещение, значение)
print(list(enumerate(C)))  #смещение, ключ

#возвращает генераторный объект — разновидность объекта, поддерживающий протокол итерации,
Q = enumerate(C)
print(next(Q))
print(next(Q))

def func(arg):
    return arg**2

print(list(map(func, B))) #применяет функцию к элементам последовательности



#os .рореп в Python также предоставляет интерфейс, подобный файлам, для чтения вывода,
# порождаемого командами оболочки.
print(os.system('systeminfo'))


#тож самое
#for i in os.popen('systeminfo'): 
#    print(i)
#a = os.popen('dir')
#print(a.readline())

'''
функкции:
zip
map
enumerate
filter #пропускает всё что не тру
import functools, operator
functooIs.reduce
возвращают итерируемый объект
'''

def mymap(func, *seqs): #аналог map возвращают генераторы, предназначенные для поддержки протокола итерации
    return (func(*args) for args in zip(*seqs))
a = mymap(abs, [-2, -1, 0, 1, 2])
print(next(a))
print(list(a))


def myzip(*args):
    iters = list(map(iter, args))
    while iters:
        try:
            res = [next(i) for i in iters]
            yield tuple(res)
        except(StopIteration):
            return None

            
print(list(myzip('qwe','shf22')))

