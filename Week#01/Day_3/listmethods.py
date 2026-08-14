vip = [1,2,3,4,5,6,7,8]
print(vip)
#we will practice all methods in this list
#accessing
print(vip[7])
reverse_list= vip [::-1]
print(reverse_list)
#Adding Element
vip.append(9)
print(vip)
#inserting
vip.insert(9,10)
print(vip)
#extend
vip.extend([11,12,13])
print(vip)
#updating
vip[0]=200
vip[1]=100
print(vip)
#remove
vip.remove(200) #value
print(vip)
#pop
vip.pop()# koi index ni dia to last wala 13 out
print(vip)
print("List will be clear if you press 0 ")
n1=int (input())
if n1==0:
    vip.clear()
    print(vip)
else:    
    
  print("Now Nested List")
n2=[[1,2],[3,4],[4,5]]
print(n2[0][1])







    
    
