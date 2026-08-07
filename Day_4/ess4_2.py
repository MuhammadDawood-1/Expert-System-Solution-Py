z=[1,2,3,3,3,4,3,3]
y={}
for char in z:
    if char in y:
        y [char]+= 1
    else:
        y [char]=1
print(y)   


