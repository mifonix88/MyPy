#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#None интерпритируется как ложь
X = 1
Y = 0
print(X and Y) #Если оба истена - вернёт значение с право)если нет вернёт значение слево
print(X or Y) #Если левое истенно - вернёт левое знаение), иначе вернёт правое
print(not Y) #Если ложь вернёт True, иначе False

Q = 4 if 'we' else '8'#Звучит как q =4 если if истинно иначе ...
print(Q)
Q = ((7 and 64) or 5)#Особый случай использования
print(Q)
Q = 0 or 0 or 0 or 4 or 0 #вернёт первое попавшееся истинное
print(Q)
Q = 0 or 0 or 0 or 0 or None #или ноне
print(Q)


#тернарное выражение 
Q = X if X else Y

#ещё примеры
q =[1,2,3,0,'','A']
print(list(filter(bool, q))) #filter вернёт все истенные
print(any(q)) #является ли истинным хоть одно? вернёт True
print(all(q)) #True только если все истенны


