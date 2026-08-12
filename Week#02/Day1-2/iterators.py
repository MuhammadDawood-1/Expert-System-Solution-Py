numbers = [10, 20, 30]
my = iter(numbers)

print(next(my))
print(next(my))
print(next(my))

ess=["Interns","Developers","Bussiness Developer"]
office=iter(ess)

print(next(office))


student = {
    "name": "David",
    "age": 20,
    "course": "Python"
}

iterator = iter(student.items())

print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator = iter(student.values())
print (next(iterator))

