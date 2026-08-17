from collections import Counter
a = [1, 1, 1, 2, 3, 3, 4]
c=Counter(a)
print(c)
b="dawood"
za=Counter(b)
xc=Counter("expert system solution")
print(za)
print(xc)
#accesing  by indexing
print(c[5])
print(za['d'])
#counter methods 
ctr = Counter([1, 1, 2,10])
ctr.update([2, 2, 3, 3,10])
print(ctr)

