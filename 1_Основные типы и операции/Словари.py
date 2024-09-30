#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#неупорядоченые коллекции
#представляют собой таблицы ссылок на объекты (хеш-таблицы)

D = {} # Пустой словарь
D[1] = 2 #Обращение к не существующему значению - создаёт это значение 
D[2] = 'er' 
D['z'] = 'ty' 
print(D)
#D = {1 : 2,2 : 'er','z' : 'ty'}  #Ключ:значение
print(D['z']) #Обращение к значению по ключу 'z'
print(D[2] + 'ty') #Прибавить к значению по ключу 2
print(D[1] + 2)  #Прибавить к значению по ключу 1
print(D) #Изначальный словарь не меняется
Q = {'qw' : {1 : 1, 'w' : 12},'er':['ew','we'],2 : 32} #Вложения словарь в словаре и тп.
print(Q['qw']) #Обращение к вложеному словорю
print(Q['qw']['w']) #Обращение к элементу вложеному в словарь
print(Q['er']) #Обращение к вложеному списку
print(Q['er'][1]) #обращение к элементу списка
print(Q['er'].append('qerty')) #Добавление элемента к списку
print(Q)

#Сортировка ключей
W = {2 : 'a',1 : 'b',3 : 'c'}
print(W)



for key in sorted(W):
    print(key, '=>', W[key])

#Немного о цикле
for Z in 'qwerty': #Выведет по очереди элементы строки
    print(Z)

X = 12
while X > 0: #Выведет 12 раз qwerty, вычтет их Х 1 и выведет ещё 11 и тд
    print('qwerty ' * X) #будет выполнятся пока Х > 0
    X -= 1
  
Q = {'qw' : {1 : 1, 'w' : 12},'er':['ew','we'],2 : 32}
print(Q)
print(Q['qw']) #Доступ
print('w' in Q)  #проверит есть ли ключ в словаре
list(Q.keys()) #создаст список ключей
Q['er'] = 12345678 #изминение
print(Q)
Q['ui'] = 'trewrtr' #добавление нового элемента
print(Q)
del Q[2] #удаление по ключу
print(Q)

list(Q.values()) #Вернёт список значений словаря
print(Q)
list(Q.items())
print(Q) #вернёт список кортежей(ключ;значение)
print(Q)

#Попытка извлеч не существующие значение
print(Q.get('er')) # есть такой ключ
print(Q.get('xf')) # нет ключа, выведет None
print(Q.get('xf', 'нету'))  #нет ключа, выведет значение 'нету'
print('#######','xf' in Q) #

#тоже самое
if ('xf') in Q:
    print(1)
else:
    print(0)
#ещё способ
try:
    print(Q['xf'])#попытается найти
except KeyError:
    print(0)
#ещё
print(Q['x'] if 'х' in Q else 0)


#Добавление удаление
D = {'asgdag':'weeewwewewewew'}
D.update(Q) #добавит значения из Q в D
print(D)
print(D.pop('asgdag')) #Удалит и вернёт значение того что удалил
print(D.pop('er'))
print(D.pop('qw'))
print(D.pop('ui'))
print(D)

for key in Q: #выведет ключи словаря(in альтернатива keys)
    print(key)

#генераторы словарей
print(list(zip([1,2,3],['qwe','qw3e','aef']))) #обьединение ключей и словаря(список из кортежей)
W = dict(zip([1,2,3],['qwe','qw3e','aef'])) #создание словаря
W2 = dict(name = 'arg',name2 = 'arg2' ) ##создание словаря
print(W)
print(W2)
E = {x: x ** 2 for x in range(1,10)}
print(E)
R = dict.fromkeys(['a','b','c'],0)
print(R)
T = dict.fromkeys('abc')
print(T)


#Сортировка клюей
M = list(W.keys())#
M.sort()
print('###########',M)

for x in sorted(W): #sorted принимает любой итерируемый обьект
    print(x, W[x])  

#словари являются итерируемыми объектами с методом __iter__ и __next__
it = W.__iter__()
#print([i for i in it])
print(it.__next__())
print(it.__next__())
print(it.__next__())

try:
    print(it.__next__())
except(StopIteration):
    print('По завершения обхода вызвается исключение StopIteration')


D = {}
D2 = {}
D.keys () #Методы: все ключи,
D.values() #все значения,
D.items() #все кортежи ключ+значение,
D.copy() #копирование (верхнего уровня),
D.clear() #очистка (удаление всех элементов),

D.update(D2) #объединение по ключам, если конфликт ключей перезапишет!

D.get(key, 'default') #извлечение по ключу; если отсутствует, тогда возвратить стандартное значение (или None),
print('xf' in D)

D.pop(key, 'default') #удаление по ключу вернёт значение, если отсутствует вернёт  default

D.setdefault(123, 'value') #установка по ключу отсутствует установить значение value
print(D)
D.popitem() #удаление/возвращение любой пары (ключ, значение);
print(D)

#словари похожи на множества и поддерживают схожие операции
print({12:None}.keys() & {12:None,13:None}.keys()) #пересечение ключей


def default():
    print('default')

W = {'qwe':123, 123:412}
W.get(234, default)() 
