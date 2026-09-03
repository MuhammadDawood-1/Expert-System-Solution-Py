arr=[10,20,1,2,34,45,56]
n=len(arr)

for i in range(n):
    min=i
    for j in range(i+1,n):
        if arr[j] < arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
    
print(arr)
        