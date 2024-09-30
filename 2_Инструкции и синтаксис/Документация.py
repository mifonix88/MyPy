#C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe -m pydoc -b #из консоли
#можно выбрать и в меню пуск
#документация достаточно подробная

#http: //www.python.org #оф сайт

#Иерархия документации
'''
Module documentation
'''
def square(x):
    '''
    function documentation
    can we have your liver then?
    '''
    return x ** 2 # квадрат

class Employee:
    "class documentation"
    pass
print(square (4))
print(square.__doc__)

help() #справка по методу и т.п
dir() #все атрибуты, методы, доступные для обьекта
name.__doc__() #аналог хелп
