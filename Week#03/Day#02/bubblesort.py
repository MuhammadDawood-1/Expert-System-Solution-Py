arr=[100,22,1,500,21,21]
n = len(arr)
print(len(arr))
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)
