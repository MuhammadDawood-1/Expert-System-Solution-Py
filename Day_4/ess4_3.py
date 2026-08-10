check = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

print(5)
print(-5)
print(0)


my_list=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,my_list))
print(even)
