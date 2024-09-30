import os
for i in os.walk('.'): # Генератор инструмента прохода по каталогам (os.walk является нормальной генераторной функцией)
    for j in i[2]: # Операция 'поиска' в Python
        #if name.startswith('call'): #str.startswith возвращает True, если строка str начинается указанным префиксом 
        print(j)
