from person import Manager,Person

mika = Person('Michail Popov',job = 'Rabochii',pay = 10000)
lika = Manager('Viktoriy Lomakina',10000)
sue = Person('Nekto')

import shelve
baza = shelve.open('baza_dannyh')
for i in (mika,lika,sue):
    baza[i.name] = i 
baza.close()

        
