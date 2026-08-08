#2d list 
'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])#1
print(matrix[0][1])#2
print(matrix[2][2])#9

for i in range(3):
    for j in range(3):
        print(matrix[i][j]) '''
        
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for i in range(3):
    for j in range(3):
        if matrix[i][j] == 50:
            print(matrix[i][j])
            
            
for i in matrix:
    for j in i:
            print()            
            
