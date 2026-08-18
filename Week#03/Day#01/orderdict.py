from collections import OrderedDict

od=OrderedDict()
od['apple']=1
od['mango']=2

print(list(od.items()))

print("dict")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, val in d.items():
    print(key, val)
    
    
print ("ordered dict")
ad=OrderedDict()
ad['a']=2
ad['b']=1
ad['c']=3
ad['d']=4

for key,val in ad.items():
    print(key,val)
    