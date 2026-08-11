## List Comprehension
numbers=[i for i in range(5)]
print (numbers)
#sq
sq=[i*i for i in range(10)]
print(sq)
#table5
table5=[5*(i+1) for i in range(10)]
print (table5)
#sq  of 4
sq4=[4**(2+i) for i in range(5)]
print(sq4)

# even 
even=[i for i in range(10) if i % 2 == 0]
print(even)
 # odd
odd=[o for o in range(10) if o % 2 != 0]
print(odd)
#String Example 
Name="David"
Name=[i for i in Name]
print(Name)

RollNo="F2024SE037"
RollNo=[j for j in RollNo]
print(RollNo)

#uper lower
names=["Dawood","Zaigham","Abuzar"]
upper=[name.upper() for name in names]
print(upper)
lower=[name.lower() for name in names]
print(lower)

#Greater than 5
greater=[i for i in range(10) if i>5]
print(greater)
#less than 5 
less=[i for i in range(4) if i < 5] 
print(less)


