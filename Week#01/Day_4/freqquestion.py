z=[1,2,3,3,3,4,3,3]
y={}
for char in z:
    if char in y:
        y [char]+= 1
    else:
        y [char]=1
print(y)   

#frequency program
cities=["100","100","200","120","200","100"]
size={}
for char in cities:
    if char in size:
        size[char]+=1
    else:
        size[char]=1
print(size)





