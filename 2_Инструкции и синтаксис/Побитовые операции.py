
x = 1 #Десятичное значение 1 в битах выглядит как 0001

print(bin(x << 2)) #Сдвиг влево на 2 бита: 0100

print(bin(x | 2)) #Побитовое ИЛИ (один из битов = 1) : 0011

print(bin(x & 1)) #Побитовое И (оба бита = 1) : 0001

print(x ^ 3)#Побитовое исключающее ИЛИ: один из битов = 1, но не оба

