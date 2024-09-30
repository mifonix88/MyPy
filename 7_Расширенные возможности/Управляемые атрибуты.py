


#1045
class One:
    def __init__(self,one):
        self._one = one
    def getFun(self):
        return self._one ** 2
    def setFun(self,one):
        self._one = one *8
    def delFun(self):
        print('а ума у тя ни много?')
    one = property(getFun,setFun,delFun,'Документацыя тут')
    
Q = One(2)
print(Q.one) #вызовет getFun
Q.one = 2 #вызовет setFun
print(Q.one)
print(One.one.__doc__)
del Q.one #вызовет delFun
print(Q.one)
    
    
    
#альтернативный способ
class Too:
    def __init__(self,one):
        self._one = one
    @property
    def one(self):#one = property(one)
        'сдесь документация'
        return self._one** 2
    @one.setter
    def one(self,one):#one = one.setter(one)
        self._one = one*8
    @one.deleter
    def one(self):#one = one.deleter(one)
        print('не удалю)))')
        
Q = Too(2)
print(Q.one) 
Q.one = 2 
print(Q.one)
print(Too.one.__doc__)
del Q.one 
print(Q.one) 



#тоже самое но с дискриптором
class FreeDis:
    '''
    С функциональной точки зрения дескрипторный протокол позволяет направлять
    операции извлечения, установки и удаления конкретного атрибута методам объекта
    экземпляра отдельного класса, которые мы предоставляем. В итоге мы получаем возможность
    вставлять код, подлежащий автоматическому запуску во время операций
    извлечения и присваивания, перехватывать операции удаления атрибутов и при желании
    снабжать документацией по атрибутам.
    '''
    #Классы с любым таким методом считаются дескрипторами,
    def __get__(self,instance,owner):
        return instance._one ** 2
    def __set__(self,instance,one):
        instance._one = one * 8  
    def __delete__(self,instance):
        print('Уже достал))')
        #del instanca._one
class Free:
    def __init__(self,one):
        self._one = one
    one = FreeDis()


Q = Free(2)
print(Q.one) 
Q.one = 2 
print(Q.one)
print(Too.one.__doc__)
del Q.one 
print(Q.one)



    
#def __getattr__(self,name):pass Обращения к неопределённому атрибуту
#def __getattribute__(self,name):pass Обращения к любому атрибуту
#def __setattr__(self,name,value):pass Операции присваивания любому атр
#def __delattr__(self,name)pass Удаление любого атрибута
'''
Метод__ getattr__ запускается для неопределенных атрибутов — поскольку он
выполняется только для атрибутов, которые не хранятся в экземпляре или не
наследуются от одного из его классов, используется он прямолинейно.
• Метод__ getattribute__ запускается для каждого атрибута — поскольку он
включает все, вы должны соблюдать осторожность при его применении, чтобы
избежать рекурсивных циклов из-за передачи суперклассу операций доступа к
атрибутам.
'''






class Property:
    #Связь между свойствами и дескрипторами
    def __init__ (self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel # Сохранить несвязанный метод
        self.__doc__ = doc # или другие вызываемые объекты
        
    def __get__ (self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError ("can't get attribute") # нельзя извлечь атрибут
        return self.fget(instance) # Передать instance экземпляру self
                                    # в методах доступа к свойствам
                    
    def __set__ (self, instance, value):
        if self.fset is None:
            raise AttributeError ("can't set attribute") # нельзя установить атрибут
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError ("Удалять нельзя!") # нельзя удалить атрибут
        self.fdel(instance)

class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName) # Использовать подобно property ()

x = Person()
x.name
x.name = ' Bob'
x.name = 123
#x.getName()
del x.name
