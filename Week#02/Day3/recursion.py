def print_x(n):
    if n<=0:
        return
    else:
        print_x(n-1)
        print("0"*n) 
print_x(6)

def print_y(n):
    if n<=0:
        return
    else:
        print("O"*n)
        print_y(n-1)
        
print_y(6)
