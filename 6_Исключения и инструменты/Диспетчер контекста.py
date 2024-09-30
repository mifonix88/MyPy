class TraceBlock:
    
    def message(self, arg) :
        print('running ' + arg) # выполнение
        
    def __enter__ (self) :
        print('starting with block') # начало блока
        return self
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print ('exited normallyXn') # нормальный выход
        else:
            print ('raise an exception! ' + str (exc_type) ) # генерация исключения
        return False # Распространение

if __name__ == '__main__' :
    
    with TraceBlock () as action:
        action.message('test 1')
        print('reached') # достигнуто

    with TraceBlock () as action:
        action.message('test 2')
        raise TypeError
        print('not reached') # не достигнуто

'''
1. Выражение вычисляется, давая в результате объект диспетчера контекста, который
обязан иметь методы__enter__ и___exit__ .
2. Вызывается метод__ enter__ диспетчера контекста. Возвращаемое им значение
присваивается переменной в конструкции as при ее наличии либо попросту отбрасывается.
3. Выполняется код во вложенном блоке with.
4. Если в блоке with возникает исключение, тогда вызывается метод
__ exit__ (type, value, traceback] с передачей ему деталей исключения. Это
те же самые значения, которые возвращает функция sys .exc_info, описанная
в руководствах по Python и позже в данной части книги. Если метод__ exit__
Глава 34. Детали обработки исключений 351
возвращает значение False, тогда исключение генерируется повторно; иначе
оно заканчивается. Обычно исключение должно быть сгенерировано заново,
чтобы оно распространилось за пределы оператора with.
5. Если в блоке with исключение не возникало, то метод_ exit__ все равно вызывается,
но для всех его аргументов type, value и traceback передаются None.
'''

#Допускается указывать любой количество диспетчеров контекстов и множество
#элементов работают аналогично вложенным операторам with.
'''
with А () as а, В () ash:
    операторы

with А() as а :
    with В () as Ь:
        операторы
'''
