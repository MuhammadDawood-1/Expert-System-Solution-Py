from itertools import cycle
count = 0
for x in cycle(["A", "B", "C"]):
    print(x)
    count += 1

    if count == 9:
        break