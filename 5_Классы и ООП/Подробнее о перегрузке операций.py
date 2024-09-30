
'''
метод__ герг__ , если присутствует, то часто используется, чтобы предоставить низкоуровневое
отображение объекта как в коде, а метод__ str__ зарезервирован для более информативного
отображения, дружественного к пользователям.

операция вывода запускает__ str__ , 
а интерактивная подсказка автоматически выводит результаты с помощью__ герг__ ,
'''

#перегрузка операций — обеспечение линии поведения для встроенных операций
#вроде вывода;

class KlassIm():
    def __init__(self,im, arg):
        self.name = im
        self.zarabotal = arg

    def lastName(self,new_name):
        self.name = new_name

class ZarplataRabov(KlassIm):

    def __repr__ (self):
        '''
        Метод __repr__  удобно перегружать при тестировании. Дабы не выводить поимённо все 
        атребуты экземпляра, можно раз перегрузить этот метод
        Если не перегрузить выведет <__main__.ZarplataRabov object at 0x0000017263E6B1F0>
        '''
        return '@@@Инфа: name: %s, ЗП: %s' %  (self.name, self.zarabotal)    # Строка для вывода


    def __str__(self):
        #по сути аналог __repr__ (хотя __str__ предпочтительнее)
        #То есть__ герг__ используется везде, исключая print и str
        #В действительности__ str__ просто переопределяет___repr__
        #__ str__ и___repr__ обязаны возвращать строки'
        return '@@@Инфа: name: %s, ЗП: %s' %  (self.name, self.zarabotal)

    def nachislit(self,new_arg):
        self.zarabotal = new_arg

rab1 = ZarplataRabov('Name1', 50)
rab2 = ZarplataRabov('Name2', 100)

print(rab1, rab2)


class Indexer():
    def __getitem__(self, index):
        return index **2

X = Indexer()
X[4] # Для X[i] вызывается X.__getitem__ (i)

for i in range(10):
    print(X[i], end = ' ') # Каждый раз выполняется__getitem__ (X, i)

print(end = '\n')


class IndexSetter:
    def __init__(self):
        self.data = {}
        
    def __str__(self):
        return 'self.data: %s' %  self.data
        
    def __setitem__ (self, index, value): # Перехватывает присваивание# по индексу или срезу
        self.data[index] = value # Присваивает по индексу или срезу

S = IndexSetter()
S['name']='arg'
print(S)


class InGet:
    def __getitem__(self, index): 
        return self.data[index]

F = InGet()
F.data = "1234"
for i in F:   #циклы for на каждом проходе вызывают метод __getitem__ с новым смещением
    print(i, end=' ')

print(end = '\n')
print([i for i in F])
print(tuple(F), list(F)) #... и так далее

#Если метод определён до он становится автоматически поддерживает все итерационные контексты


#пердпочтительнее использовать __iter__ для таких целей

class SkipObject:
    def __init__ (self, wrapped) : # Сохранить объект для использования
        self.wrapped = wrapped
    def __iter__ (self) :
        return SkipIterator (self .wrapped) # Каждый раз новый итератор

class SkipIterator:
    def __init__ (self, wrapped):
        self .wrapped = wrapped # Информация о состоянии итератора
        self.offset = 0

    def __next__ (self) :
        if self.offset >= len(self.wrapped): # Прекратить итерацию
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # Иначе возвратить и пропустить
            self.offset += 2
        return item


'''
Альтернативный способ
def gsquares(start, stop) :
    for i in range (start, stop + 1):
        yield i ** 2
'''

alpha = 'abcdef'
skipper = SkipObject(alpha) # Создать объект контейнера
I = iter(skipper)           #Создать на нем итератор
print(next (I), next(I), next(I)) #Посетить смещения 0,2, 4

for x in skipper:
    for y in skipper:
        print(x + y, end=' ')
print(end = '\n')

# Генератор на основе__ iter__ + yield
'''
Вспомните, что любая функция, которая содержит оператор yield, превращает^
ся в генераторную функцию. При вызове она возвращает новый генераторный объект
с автоматическим предохранением локальной области видимости и позиции в коде,
автоматически созданным методом__ iter__ , просто возвращающим сам объект, и
автоматически созданным методом__ next__ 
'''
class Squares: 
    def __init__ (self, start, stop): 
        self.start = start
        self.stop = stop

    def __iter__ (self) :  #Метод__ next__ является автоматическим/подразумеваемым
        '''
        всякий раз, когда такой метод вызывается инструментом
        итерационного контекста, он будет возвращать новый генераторный объект с
        необходимым методом__ next__
        '''
        for value in range(self.start, self.stop + 1):
            yield value**2

A = Squares(1,5)
print(list(A))


class Iters:
    '''
    Специфический метод__ contains__ перехватывает
    операцию проверки членства, универсальный метод__ iter__ перехватывает итерационные
    контексты, такие как вызываемый многократно метод__ next__ (будь они
    записаны явно или подразумеваются оператором yield), а метод__ getitem__ никогда
    не вызывается
    '''
    def __init__ (self, value):
        self.data = value

    def __getitem__ (self, i):
        print('getitem[%s] : ' % i, end=' ')
        return self.data[i]

    def __iter__ (self) :
        print('iter=> next:', end=' ')
        for x in self.data:
            yield x
            print('next:', end=' ')

    def __contains__ (self, x) :
        print('contains : ', end=' ')
        return x in self.data

IT = Iters([41,42,43])
print(5 in IT)
print([i for i in IT])
print(IT[2:])


#Доступ к атрибутам: __ getattr__ и___ setattr__


class Empty:
    def __getattr__ (self, attrname) : #перехват обращения к не существующему атребуту

        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)
X = Empty ()
print(X.age)
try:
    print(X.name)
except AttributeError:
    print(f'Вызван: raise AttributeError')


class Accesscontrol:
    '''
    Если данный метод определен или унаследован, тогда выражение
    self, атрибут = значение становится self.__ setattr__ ('атрибут', значение).
        
    это позволяет классу перехватывать изменения атрибутов и
    выполнять желаемые проверки достоверности или преобразования.
    Тем не менее, использовать метод__ setattr__ несколько сложнее, т.к. присваивание
    значения любому атрибуту в self внутри__ setattr__ снова вызывает
    __ setattr__ , что потенциально может стать причиной бесконечного цикла рекурсии
        
    Если вы хотите использовать метод__ setattr__ , то можете избежать циклов,
    реализуя присваивания значений атрибутам экземпляра в виде присваиваний ключам
    словаря атрибутов. То есть применяйте self.__ dict__ [ attrname ] = х, или object._ setattr__(self, attr, value + 10) (последний предпочтительнее)
    
        '''
    #self.age = x приведёт к зацикливанию!!!
    def __setattr__ (self, attr, value) : #метод___setattr__ перехватывает все присваивания значений атрибутам.
        if attr == 'age' :
            self.__dict__ [attr] = value + 10 # He self .имя = значение
        else:
            raise AttributeError(attr + ' not allowed')

X = Accesscontrol()
X.age = 30
print(X.age)
X.age = 50
print(X.age)

try:
    X.name = 10
except AttributeError:
    print('Вызван: raise AttributeError')



#метод__ call__ вызывается при вызове вашего экземпляра.
class Callee:
    def __init__(self, val=0):
        self.val = val

    def __call__(self, *pargs, **kargs): # Перехватывает вызовы экземпляра 
        '''
        можно реализовать поддержку вызова без аргументов def __call__(self):
        '''
        
        print('Вызван __call__ c аргументами: ' , pargs, kargs)
        print(f"Старое: {self.val} Новое: {kargs['x']}")
        self.val = kargs['x'] #Запоминаем новое состояние, может быть полезно

X = Callee()
X(1,2,32, x=12)
X(1,x = 22)



#сначала пробует получить
#прямое булевское значение с помощью метода__ bool__ ; если данный метод
#отсутствует, то Python посредством__ len__ пытается вывести значение истинности
#из длины объекта
class Bool():
    def __bool__(self):
        return True
    def __len__(self):
        return 1
x=Bool()
if x: print(True)


#Следующий пример плохой из зи непредсказуемого поведения 
#сборщик мусора не всегда тутже удаляет!!!
#исключения также могут доставить проблемы
#см документацию перед использованием!

class Life:
    
    def __init__ (self, name= ' unknown ') :
        print ('Hello ' + name)
        self.name = name
        
    def live(self):
        print(self.name)
        
    def __del__ (self) :
        '''
        метод деструктора__ del__ , запускается автоматически
        при возвращении пространства памяти, занимаемого экземпляром (т.е. во время
        “сборки мусора”
        '''
        print('Goodbye ' + self.name)
        
brian = Life ('Brian')
brian.live()
brian = 'loretta'

'''
???
def GetAttr():
    data = {}
    def __getattribute__(self, name, arg):
        self.data[name] = arg

a = GetAttr()
a.arg = 10
'''
        
