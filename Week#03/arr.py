# Largest
arr = [10, 20, 130, 40, 50]

largest = arr[0]

for i in range(len(arr)):
    print(arr[i])
    print(arr)

    if arr[i] > largest:
        largest = arr[i]

print("Largest:", largest)


# Smallest
arr2 = [10, 2, 1, 33, 45, 66]

smallest = arr2[0]

for i in range(len(arr2)):
    if arr2[i] < smallest:
        smallest = arr2[i]

print("Smallest:", smallest)


# Sum
arr = [10, 20, 130, 40, 50]

total = 0

for i in range(len(arr)):
    print(len(arr))

    total = total + arr[i]

print("Sum:", total)


# Average
average = total / len(arr)

print("Average:", average)