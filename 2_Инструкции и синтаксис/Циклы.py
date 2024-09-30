#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#while и for используют
#pass #Пустая инструкция (типо None) 
#continue #немедленный переход в начало цикла
#break #немедленно Завершит цикл
#else #Будет выполнятся если цикл завершился не брейком, или цикл не выполнялсяя вовсе

Q = {'qw':1,'mh':2,'ut':3}
print(Q)
for key in Q:
    print(key, '=>', Q[key]) #Обход ключей словаря

list(Q.items()) #преобразует словарь в кортеж
print(Q)
for(key, name) in Q.items():
    print(key, '=>', name) #Ещё пример обхода словаря(одновременно и ключей и значений)
    
#Пример использования сравнение последовательности
W = 'wert'
E = 'werrwr'
T = []
for i in W: #Выполнит обход первой последовательности
    if i in E: #проверит наличие общих элементов
        T.append(i)
print(T)

#Сканирование файлов по средствам цикла
file = open('123.txt', 'r') #Прочитаать содержимое файла в одну строку
print(file.read())

#Читать по одному символу
file = open('123.txt')
while True:
    Q = file.read(1) 
    if not Q:
        break
    print(Q)

for Q in open('123.txt').read(): #аналог предыдущему
    print(Q)

#Чтение блоками или строками
file = open('123.txt')
while True:
    Q = file.readline() #readline - читать строку за строкой
    if not Q: break
    print(Q, end='')

file = open('123.txt', 'rb')
while True:
    Q = file.read(10) #блоками по 10 юайтов
    if not Q: break
    print(Q)

for Q in open('123.txt').readlines(): #Загружается весь файл в список строк
    print(Q, end='')

for Q in open('123.txt'): #загружает по одной строке (лучший для чтения текста)
    print(Q, end='')


#Использование функции рэнж в цикле
for i in range(30):
    print(i, end=',')

S = '1234567891'
list(range(0,len(S),2)) #выведет указаные смецения
for i in range(0,len(S),2):
    print(S[i], end=' ')
print('\n')
for i in S[::2]: #Простой способ
    print(i, end=' ')
print('\n')
    
S=[1,2,3,4,5]
print(S)
for i in range(len(S)): #Обход и замена значений списка
    S[i] +=1
print(S)

#Обход нескольких последовательностей одновременно
a = [1,2,3,4]
b = [2,3,4,5]
c = [3,4,5,6]
print(list(zip(a,b,c))) #Вернёт список кортежей

for (A,B,C) in zip(a,b,c):
    print(A,'+',B,'+',C,'=', A+B+C)

#Конструктор словарей
D = {}
for (Q,W) in zip(a,c):
    D[Q] = W
print(D)

#или так
E = dict(zip(a,c))
print(E)

#
S = 'werty'
for (T,y) in enumerate(S): #Возвращает кортеж значение\смещение
    print(T,'Смещение =>',y)
