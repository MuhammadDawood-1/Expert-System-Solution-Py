# List methods
ess = ["Chai", "Pani", "Coffee", "Tissue", "Salary"]

ess.append("nouman")
print(ess)

ess.insert(4, "David")
print(ess)

ess.pop(1)
print(ess)

ess.sort()
print(ess)


# Sorting and extending a list
travel = ["abdullah", "zeymal", "sara", "fatima", "areeba"]

travel.sort()
print(travel)

travel.extend(["nouman bhai", "dawood bhai"])
print(travel)

travel.append("abuzar bhai")
print(travel)


# sorted() creates a new sorted list
numbers = [1, 4, 2, 34, 6, 7]

temp = sorted(numbers)
print(temp)


# Basic dictionary
nouman = {
    "Name": "vs code",
    "info": "sssa",
}

print(nouman)

# extend() needs a list/iterable
number = [1, 4, 5, 6, 7, 8, 10]
number.extend([20, 30])
print(number)

# Loop through a list
products = ["Apple", "Mango", "Banana"]

for product in products:
    print(product)
    print(products)
    
    

        