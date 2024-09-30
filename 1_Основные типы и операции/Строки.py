#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#строка -  упорядоченая коллекция символов
'''
три строковых типа: str применяется для текста Unicode (в том числе ASCII), 
bytes используется для двоичных данных (включая закодированный текст), 
a bytearray является изменяемым вариантом типа bytes.
'''

D = 'qwertyuiop'
print(D)
print(len(D)) # Длинна
print(D[0] + ' - первый')   # Первый элемент D
print(D[5] + ' - Шестой')   # шестой элемент D
print(D[-1] + ' - Последний')   #Последний элемент D
print(D[2:7] + ' - С третий по седьмой') # Срез D с 3 по 7
print(D[:] + ' - всё содержимое') # всё содержимоеСрез D с 3 по 7
print(D[:-1] + ' - Всё кроме последнего')   #Всё кроме последнего
print(D[:3] + ' - тоже что и D[0:3]')   #тоже что и D[0:3]
print(D.find('wer')) #Поиск смещения
print(D.replace('wer', '123')) #Поиск с заменой
S =  D.replace('wer', '123') # Создаёт новую переменную
print(S + ' - Новый обьект в переменной S')
print(D + ' - Старый обьект в переменной D') #Строка не изменилась
D = '123' + D[:] # Создаёт новую удаляет старую
print(D + ' - Новый обьект в переменной D')
Q = 'qqq,www,eee'
print(Q.split(',')) #Разбивает строку по разделителю и создаёт список строк
s = 'a\nb\tc' #знак \n конец строки,\t табуляция
print(s)
print(len(s))


#Получение помощи
#print(dir(S)) #Список всех доступных отребутов заданного обьекта(S)
#print(help(S.replace)) #Можно узнать назначение того или иного элемента Справка по встроенной функции replace:
'''матрица,перезагрузка'''
r = 'qwerty''''
for p in r * 100: #опертор for присваевает переменной P поочерёдно каждый элемент строки R
    print(p, end='_')#и выполняет для каждого инструкцию'''

print('n' in r) #есть ли n в строке r(in выполняет функцию поиска)

r = 'modqwerty'
print(r[::-1]) #вернёт перевёрнутое значение
print(r[0:7:2])#вернёт в деапазоне от 0 до 7 с шагом 2
print(r)
print(r[2::-1]) #при отрицательных значениях счёт с право на лево

print(int('21')) #перобразует строку в число
print(str(21))   #преобразует число в строку
print(int('21') + 21)#сложение
print(str(21) + '21')#канкатинация

r = 'aabbcc'
r = r.replace('aa', '11')#Поиск с заменой
print(r)
e = 'aa1bb1cc1'
print(e)
e = e.replace('1','A')#Глобальный поиск с заменой(заменяет всё найденое)
print(e)
q = e.find('A') #Поиск смещения подстроки
print(q)        #    найдино смещение
e = e[:q] + 'QWERTY' + e[(q+1):] #замена подстроки(ищит слево на право заменяет только 1 подстроку) 
print(e)

#другой способ
e = list(e) #преобразуем строку в список
print(e)
print(e[2:8])
e[2:8] = 'A'#меняем
print(e)
e = ''.join(e)#Обратно список в строку(Встовляет между элементами списка разделитеть
print(e)      #В данном случае '' - ничего)

#разбитее строки на подстроки по разделителю(результат список)
w = 'qwerty qwerty, qwerty'
v = w.split() #по пробелу
print(v)
b = w.split(',') #по запятой
print(b)
c = w.split('ty') #по буквам
print(c)

print(r.upper()) #изменяет регистр

#Форматирование строк
Q = 'qwerty, %d, %s' %(12345, 'ytrewq') #Подстоновка разных типов за одну подстоновку(число и подстрока)
print(Q)
Q = Q + ', %s, fgjk' % 4352 #Для одного элемента скобки не нужны
print(Q)

#Пример форматирования со словорём(По ключам)
H = '%(q)d %(x)s' % {'q':123, 'x':'qwerty'}
print(H)

qwer = ''' 
Хай %(name)s
Из края %(tam)s
'''
ty = {'name':'Конь','tam':'грёз'}
print(qwer % ty) #Часто используется при постройки html разметки

print(vars())
#vars, возвращающей словарь, который содержит все переменные, существующие в месте ее вызова:
W = '%(qwer)s %(ty)s %(Q)s' % vars() #С помощью vars() Можно форматировать из словаря обращаясь по ключам
print(W)

#Метод форматирования format
M = '{1}, {0}{q}' #Форматируется по ключу или по смещению
M = M.format('qwer', 1234 , q='ty' )
print(M)
M = '{}{}{}'.format('qwerty',' qwerty',' qwerty') 
print(M) #Допускается не указывать порядковый номер(по порядку)

e = list(e)
print(e)
t = 'wer1={0[0]},wer2{0[3]}'.format(e) #Добавление из списка e" в строку "t по смещению({0[0]})
print(t)
P = 13490870987.976587659765
P1 = '{:.2f}'.format(P) #Выведет указаное число знаков после запятой(округлит)
print(P1)
P2 = format(P,'.2f') #Аналог предъидущего
print(P2)
p = '{:,.2f}'.format(P) #групирует значение целого по 3(,) 
print(p)

str_ = b'xgnjxdfgjfxjgf'
by = bytearray(str_) #гибрит байтов / списка(когда нужно изменить страку напрямую) По сути это bytes
print(by)
by.extend(b'123')
#Тип bytearray поддерживает изменения на месте для текста, 
#но только в отношении символов, которые имеют ширину не более 8 битов (скажем, ASCII).

print(by.decode()) #преобразование в обычную строку


sr = '123    1321 132 132 1321   '
print([sr.split()])
print('@@@@@@@',sr.isdigit()) #возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False

print([sr.rstrip()])#удалить пробелы справо strip cобеих сторон
#можно комбинировать sr.split().rstrip()
#Вы также можете использовать lstrip для удаления пробелов только с начала строки, а rstrip удалить пробел из конца строки.
a = r'С:\text\new*'#не форматируемая строка r'' удобно для путей
b = 'С:\text\new*'
print(b, a)

import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
#В примере производится поиск подстроки, начинающейся со слова Hello,
# за которым следует ноль или более табуляций либо пробелов, 
# затем произвольные символы, подлежащие сохранению в качестве группы совпадения,
 # и завершаются они словом world.

a = ['agf','wtrueu','__wete']
for i in a:
    if i.startswith ('__'):
        print('startswith#####',i)


#str для представления декодированного текста Unicode (в том числе ASCII);
#bytes для представления двоичных данных (включая декодированный текст);
#bytearray, изменяемая разновидность типа bytes. 


import re
S = '123 _ 476' 
В = '123 252' 

x = re.match('(.*) _ (.*)', S).groups() # Сопоставление строки с образцом


print(x)
text = '<title>Ok</title>'

x = re.findall('<title>(.*)</title>', text)
print(x)


