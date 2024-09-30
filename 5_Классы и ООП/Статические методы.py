
'''
Иногда программы должны обрабатывать данные, ассоциированные с классами,
а не экземплярами. Подумайте об отслеживании количества экземпляров, созданных
из класса, или ведении списка всех экземпляров класса, которые в текущий момент
находятся в памяти. Информация подобного рода и ее обработка связаны с классом,
но не с его экземплярами. То есть такая информация, как правило, хранится в самом
классе и обрабатывается отдельно от любого экземпляра.
'''

class Spam:
    numinstances = 0
    def __init__ (self) :
        Spam.numinstances = Spam.numinstances + 1

    def printNumlnstances():
        print("Number of instances created: %s" % Spam.numinstances)
        
a = Spam()
b = Spam()
c = Spam()

Spam.printNumlnstances()#можно обратиться через имя класса но не через экземпляр
#a.printNumlnstances()#терпит неудачу


class Spam:
    numinstances = 0
    def __init__ (self) :
        Spam.numinstances = Spam.numinstances + 1

    @staticmethod  #За счет применения встроенной функции staticmethod в коде становится возможным вызов метода без self
    def printNumlnstances():
        print("Number of instances created: %s" % Spam.numinstances)
        
a = Spam()
b = Spam()
c = Spam()

a.printNumlnstances()#а тут работет



class Methods (object) : # Для методов установки свойств в Python 2.Х # необходим object
    def imeth(self, x) : # Нормальный метод экземпляра: передается self
        print([self, x])
    
    @staticmethod #staticmethod и родственные инструменты по-прежнему являются функциями!
    def smeth(x) : # Статический метод: экземпляр не передается
        print([x])
    #можно было сделать и такЖ
    #smeth = staticmethod(smeth(x))
        
    @classmethod
    def cmeth(cis, x): # Метод класса: получает класс, не экземпляр
        print([cis, x])
        
    @property # Свойство: значение вычисляется при извлечении
    def name(self):
        return 'Bob ' + self.__class__.__name__
    

a = Methods()
a.imeth(1)
a.smeth(2)
a.cmeth(3)
print(a.name)
