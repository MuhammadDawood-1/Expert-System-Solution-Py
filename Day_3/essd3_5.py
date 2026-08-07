# ----------------------------------------
# Python Loops Practice
# ----------------------------------------

# 1. Print numbers from 1 to 100
for j in range(1, 101):
    print(j)


# 2. Print even numbers from 1 to 100
for i in range(2, 101, 2):
    print(i)


# 3. Calculate the sum of numbers from 1 to 100
total = 0

for k in range(1, 101):
    total += k

print("Sum:", total)


# 4. Reverse a number using while loop
number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)


# 5. Find the largest number in a list
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)