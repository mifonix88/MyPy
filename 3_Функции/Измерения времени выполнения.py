
'''
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время 
'''

import time
timer = time.perf_counter


def total(reps, func, *pargs, **kargs):
    '''
    Суммарное время выполнения функции func() reps раз 
    Возвращает (суммарное время, последний результат)
    '''
    start = timer() 
    for i in [i for i in range(reps)]:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    '''
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат)
    '''
    best = 2 **32 #136 лет представляется достаточным
    for i in range(reps): # Использование range при измерении времени не учитывается 
        start = timer() 
        ret = func(*pargs, **kargs) 
        elapsed = timer() - start # Или вызвать total () c reps=l
        if elapsed < best: 
            best = elapsed # Или добавить в список и найти min() 
    return best



print(total(1000 , pow, 2, 1000)[0])
print(total(1000, str.upper, 'spam'))
print(bestof(1000, str.upper, 'spam'))



#Функция time .perf__counter () возвращает значение в дробных секундах счетчика производительности, 
#определенного как часы с наивысшим доступным разрешением для измерения коротких промежутков времени.
# Она включает время, истекшее в состояниях сна, и действует в масштабе всей системы.


#Функция time.process_time () возвращает значение в дробных секундах суммы системного 
#и пользовательского процессорного времени текущего процесса. 
#Она не включает время, истекшее в состояниях сна, и по определению действует в масштабе процесса.
reps = 1000
repslist = list(range(reps))
#abs - модуль числа
def listComp():
    return [abs(i) for i in repslist]

def genExpr():
    return list(abs(i) for i in repslist) 

def genFunc():
    def gen():
        for x in repslist: 
            yield abs(x) 
    return list(gen())

def mapCall():
    return list(map(abs, repslist))


for i in (listComp, genExpr, genFunc, mapCall):
    print(i.__name__, bestof(10000, i))





import timeit
#вызов repeat модуля timeit возвращает список, дающий суммарное время, 
#которое заняло выполнение теста number раз для каждого из прогонов repeat.

arg = "L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] +=1"

print(min(timeit.repeat(number=10000, stmt=arg, repeat=3)))

def testcase () :
    у = [x ** 2 for x in range (1000)] # Вызываемые объекты или строки кода

print(min(timeit.repeat(stmt=testcase, number=1000, repeat=3)))
#детали ищите в руководстве по библиотеке Python
