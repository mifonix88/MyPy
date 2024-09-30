
print(bool(1))
print(bool('qae'))
print(bool(None))
print(bool({}))


#тернарное выражение 
Q = X if X else Y

#ещё примеры
q =[1,2,3,0,'','A']
print(list(filter(bool, q))) #filter вернёт все истенные
print(any(q)) #является ли истинным хоть одно? вернёт True
print(all(q)) #True только если все истенны
