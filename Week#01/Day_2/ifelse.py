n1 = int(input())

if n1 % 2 == 0 and 2 <= n1 <= 5:
    print("Not Weird")

elif n1 % 2 == 0 and 6 <= n1 <= 20:
    print("Weird")

elif n1 % 2 == 0 and n1 > 20:
    print("Not Weird")

else:
    print("Weird")