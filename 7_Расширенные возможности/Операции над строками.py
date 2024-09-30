# в функции open значения ключей
#rb , wb ,rb+ (bytes)
#r, w+ ,rt (str)
import sys
print(sys.platform)
print(sys.getdefaultencoding())#кодировка по умолчанию
Q = b'ABC'
print(type(Q))
print([chr(i) for i in Q])
Q = 'ABC'
print(type(Q))
print(list(Q.encode('latin-1')))#перекодирует утф8 в латин1#decode() преобразует последовательность байтов в str а encode str в bytes
print([ord(i) for i in Q])
print(bytearray(Q, 'utf-8'))#изменяемый тип bytes

import re
S = '123 op 456 la 789'
print(re.match('(.*) op(.*) la(.*)', S).groups())#поиск по шаблону (для xml итп)
'''
import struct
a = struct.pack('>i4sh', 1,'qwe', 4)#упаковать в двоисные данные
print(struct.unpack('>i4sh',a))#распоковать 
print(a)
'''
print(Q.find('B'))#поиск смещения # Q.replace(‘A’, ‘SPAM’) замена всех вхождений
import string
print(string.whitespace)#пробельные символы
