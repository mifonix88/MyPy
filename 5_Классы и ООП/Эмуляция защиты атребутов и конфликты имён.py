
class ErrAtr(Exception):
    pass


class Privacy:
    
    def __setattr__ (self, attrname, value) : #метод___setattr__ перехватывает все присваивания значений атрибутам.
        if attrname in self.privates:
            raise ErrAtr(attrname + ' не доступно')
        else:
            self.__dict__ [attrname] = value #self.age = x приведёт к зацикливанию!!!
            

class Test1(Privacy):
    privates = ['age']

class Test2(Test1):
    
    privates = ['name', 'pay']
    
    def __init__ (self) :
        self.__dict__['name'] = 'Tom' #self.age = x приведёт к зацикливанию!!!


x = Test1 ()
x.name = 'Bob'
print(x.name)
#x.age = 40

y = Test2 ()
y.qwerty = 123

print(y.name)
#y.name = 'No name' #выведет ошибку

#Псевдо закрытые атрибуты
class Test4:
    def __privates(self):
        print('Закрытый')

a = Test4()
#a.__privates()#выведет ошибку
#все имена начинающиеся с двух символов подчеркивания, но не заканчиваются ими принемают вид _Имя класса + __атрибут
a._Test4__privates()


#можно использовать чтобы избежать конфликта имён
#Когда есть одноимённый атрибут или метод в разных классах но унаследовать нужно оба
class C1:
    def __privates(self):
        print('С1')
        self.__atr = 'atrC1' 

class C2:
    def __privates(self):
        print('С2')
        self.__atr = 'atrC2' 

class C3(C1,C2):pass

a = C3()
a._C1__privates()
a._C2__privates()
print(a._C1__atr)
print(a._C2__atr)
#Если метод предназначен для использования только внутри класса, который может
#смешиваться с другими классами, тогда префикс в виде двух символов подчеркивания
#фактически гарантирует, что снабженный им метод не будет служить препятствием
#другим именам в дереве, особенно в сценариях с множественным наследованием:

'''
Присваивая последовательность строковых имен атрибутов специальному атрибуту
__ slots__ класса, мы можем позволить классу нового стиля ограничивать набор
допустимых атрибутов, которые будут иметь экземпляры этого класса,
'''
#Лучше не использовать без острой необходимости
class Slots():
    __slots__ = ['arg']
    
    #def __init__(self):
        #self.x = None
a = Slots()
a.arg = None
print(a.arg)
try:
    a.arg2 = 20
except:
    print('a.arg2 = 20 не прошло')
#Но есть нюанс
#a.__dict__ отсутствует
#def __init__(self):
    #self.x = None
#так же терпит неудачу 
#Чтобы работало нужно добавлять в __slots__ = ['__dict__']
'''
Если подкласс унаследован от суперкласса без__ slots__ , то атрибут__ dict__
экземпляра, созданный для суперкласса, будет всегда доступен, делая атрибут
__ slots__ в подклассе по существу бессмысленным.

Слоты в суперклассах бессмысленны, когда они отсутствуют в подклассах.
Аналогично, поскольку объявление__ slots__ ограничено классом, в котором
оно появляется, подклассы будут создавать__ dict__ экземпляра,
'''



#встроеннуя функция property и принимает обьект и три метода доступа (обработчики
#операций получения, установки и удаления, документацию)
#если переданно None то не поддерживаются
class Prop():
    data = None
    
    def func1(self):
        return self.data-100
    
    def func2(self, arg):
        self.data = arg+100
        print(self.data)


    arg = property(func1, func2, None, None)

a = Prop()
a.arg = 2 #запускает func2
print(a.arg) #запускает func1


'''
Python поддерживает понятие дескрипторов
атрибутов — классов с методами__ get__ и___set__ , которые присваиваются атрибутам
класса, наследуются экземплярами и предназначены для перехвата доступа по
чтению и записи к специфическим атрибутам.
'''
class AgeDesc():
    def __get__ (self, instance, owner): 
        return 40
        
    def __set__ (self, instance, value) : 
        instance._age = value
    
class Descriptors():
    age = AgeDesc ()

x = Descriptors()
print(x.age) # Запускается AgeDesc.__get__

x.age = 42 # Запускается AgeDesc.__set__
print(x._age)
