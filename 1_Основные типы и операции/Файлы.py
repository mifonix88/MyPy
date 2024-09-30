#!/usr/bin/evn python
# -*- coding: utf-8 -*-

#содержимое файла всегда строка

X = open('myfile.txt', 'w') #сли не указать путь создастся в тойже дериктории
#w - открывает для записи/очищает
#t - для чтения
#a - для записи в конец
#+ - для чтения и записи одновременно
#b - в двоичном представлении
print(X.write('Записывает строку\n')) #Возвращает количество записаных символов
print(X.write('Ещё строка\n'))
#Следует добавлять \n, или продолжется запись одной строки
print(X.write('Записывает строку '))
print(X.write('Ещё строка\n'))
X.close() #Выталкивает буферы на диск(закрывает файл)

X = open('myfile.txt') #Открывает по умолчанию режим 't'(чтение)
print(X.readline()) #читает строку
print(X.readline()) #читает следующию
print(X.readline())
print(X.readline()) #Пустая строка,конец файла

print(open('myfile.txt').read())#Прочитать весь файл целиком как одну строку 

for line in open('myfile.txt'): #Читает строку за строкой(итератор)
    print(line, end='')

    
#Сохранение разных типов в файл
Q,W,E = 12,13,14
S = 'qwerty'
D = {'q':'e','w':'r'}
L = [1,2,3]

F = open('myfile.txt', 'w')
F.write(S + '\n')  #Запись строки + \n
F.write('%s,%s,%s\n' % (Q,W,E))#Преобразует числа в строки
F.write('%s,%s,%s\n' % (Q,W,E))#Преобразует числа в строки
F.write('%s,%s,%s\n' % (Q,W,E))#Преобразует числа в строки

F.write(str(L) + '$' + str(D) + '\n') # преобразует и разделяет символом $
F.close()

#Обратное преобразование
F = open('myfile.txt')
r = F.readline() #Читает строку
print(r.rstrip()) #Удаляет символ конца строки

t = F.readline() #Читает следующию строку
t = t.split(',') #разбивает строку по разделителю
t = [int(x) for x in t] #преобразует строки в числа
print(t)

y = F.readline()#Читает следующею
y = y.split('$') #разбавает по символу $
y = [eval(x) for x in y] # Преобразует в список(eval интерпритирует строку как програмный код !!! может удалить всё при правах и инструкциях)
print(y)

F.close()

F = open('myfile.txt')
F.seek(5) #переместиться на Х символов в строке
print('#########',F.readline()) #чтение начнётся с этой позиции


#ещё способ
D = {'q':'e','w':'r'}
F = open('myfile.txt', 'wb')
import pickle
pickle.dump(D,F) #Запишит любой обьект в файл
F.close()

F = open('myfile.txt', 'rb')
D = pickle.load(F) #Прочитает любой файл
print(D)
#Однако надо заметить
print(open('myfile.txt', 'rb').read())


import struct
packed = struct.pack('@i',1) #аргументы (формат, арж, арж .....)
print('@@@@@',packed) #упаковка двоичных данных также можно записать в файд

#сериализация объектов (преобразование объектов в строки байтов и обратно),

W = {'name':'Bob', 'arg':[None,15]}

import json
JS = json.dumps(W)
#A = json.load(file_name)
print(JS)


#диспетчер контекста гарантирует закрытие файла
with open('myfile.txt', 'wb') as file_name:
    for i in file_name:
        pass
