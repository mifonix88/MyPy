
#import paket
pac = 'paket'
exec(f'import {pac}')
print(paket.__name__, paket.__file__)

exec(f'from {pac} import test')
print(dir(paket))

paket.test.test()

#аналогичный вариант
#paket = __import__(pac)

'''
предпочтительный
import importlib
paket = importlib.import_module(pac)

Вызов import module принимает строку с именем модуля и необязательный 
второй аргумент, в котором указывается пакет, применяемый в качестве места поиска
'''
