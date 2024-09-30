#!/usr/bin/evn python
# -*- coding: utf-8 -*-
'''
Каждый объект также содержит
два стандартных заголовочных поля: обозначение типа, применяемое для пометки
типа объекта, и счетчик ссылок, используемый для определения, когда можно освободить
память, которую занимает объект.
'''

a = 1
b = a
a = 'qwr'
print(b)#b всё ещё ссылается на 1
#так как объект (1) не изменяемый новое присваевание создаёт новую область в памяти
#в то время как b всё ещё ссылается на 1

#если бы тип был изменяемый то и b бы изменился
a = [1,2,3]
b = a
a[0]=100
print(b)

a = [12]
b = a
print(b==a)#True
print(b is a)#True Один и тотже обьект

a = [12]
b = [12]

print(b==a)#True
print(b is a) #False Разные обьекты

#Операция присваивания
a, *b = 'qwerty' #оператор со звездой получает все что не присвоены[всгда список]
print(a) #переменной присвоится первая буква 'q'
print(b) # А эта получит список из оставшихся букв[w,e,r,t,y]
*a, b = [1,2,3,4,5]
print(a)
print(b)
#или так
a,*b,c = [1,2,3,4,5]
print(b)

wer = 1
rew = 2
a, b = wer, rew #Присваивание кортежий
print(a,b)
[c,d] = [wer,rew]
print(c,d) #результат кортеж(1,2)

[a,b,c] = (1,2,3)#Списку присвоены переменные кортежа 
print(a,c)
(a,b,c) = 'ABC' #Строка символов присваевается кортежу переменных
print(a,c)

#Колво обьектов  справо должно быть равно колву слева
Q = 'qwer'
q,w,e,r = Q
print(q,w,e,r)

A,B,C,D,E = list(range(5)) #присвоит последовательности целые числа
print(A,D)
print(list(range(5)))

L = [1,2,3,4]  #Стёк также можно (append,pop)
while L:
    front = L[0] #
    L = L[1:]    #можно заменить front = L.pop(0)
    print(L)
Q = 'qwerty'
*a, = Q
print(a)    

#Присваевание в цикле
for (a,b,c) in [(1,2,3),(4,5,6)]:
    print(a,b,c)

#Комбинированые инструкции присваивания
Q = 'qwe'
Q += 'QWE' #Эквивалент Q = Q + 'QWE'

L = [1,2,3]
L = L.append(4)#Теряется ссылка
print(str(L) + ' - теряется ссылка (print по умолчанию')

#Операция принт
#аргументы вводятся, после то что надо вывести(если нет то все по умолчанию)
#print(L [object, ...][. sep =' '][. end='\n'][. file=sys.stdout]) - Вид по умолчанию
#sep - строка между обьектами
#end  - Символ на конце
print(Q, sep='...', end='Of\n')
print(Q, file=open('123.txt', 'a'))#Создаст файл вывода(Для единичного случия потом все по умолчанию)
print('Все как и було')
import sys
sys.stdout.write('ONO{IN{OIN\n') #Тоже что и принт

#import sys
temp = sys.stdout 
sys.stdout = open('123.txt', 'a')#Создаст файл вывода
print(90)
sys.stdout.close()  #Выталкивает буферы
sys.stdout = temp #Вернёт назат как було

#Если необходимо по очереди выводить то  в файт то в ...
R = open('123.txt', 'a')
print('В файл', file=R)
R.close()
print(23)

#Если нужно достать из 123
print(open('123.txt').read())


((a,b),c) = ('ab','c') #попарное присваивание
print(a,b,c)


a,b,*c,d ='abc' # там где * всегда список
print(a,b,c,d) #пограничный случай

#имя co звездочкой должно находиться в списке или кортеже
# *a = 'qwr' вызовет ошибку

#дополнительные методы присваивания
'''
X += Y #аналог extend
X &= Y
X -= Y
X 1= Y
X *= Y
X А= у
X /= Y
X »= Y
X %= Y
X «= Y
X **= у
X //= Y
'''
import sys
temp = sys.stdout
sys.stdout.write ('hello world\n') #print вызывает метод write объекта sys. stdout
sys.stdout = open('log.txt', 'a') # Перенаправление вывода в файл
sys.stdout.write ('hello world\n')
print('hello world\n') # Отправляется в log.txt
sys.stdout = temp #восстановление
print('ok')


#аналогичный способ
log = open('log.txt', 'a') 
print(a, b, c, file=log) 
print(a, b, c)
log.close()

'''
class FileFaker:
    def write(self, string, flush):
        # Делать что-то с выводимым текстом в строке

import sys
sys.stdout = FileFaker()

print('Прием работает, потому') # Отправка методу write класса
'''
