class Dog:
    name = "MAX"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def print_name(self):
        return f"The dog name is {self.name} and breed is {self.breed}"

    def add_age(self, age):
        return f"The dog age is {age} and name is {self.name}"


d = Dog("Taison", "Labrador")

print(d.print_name())
print(d.add_age(30))


class Dawood:
    def __init__(self, name, cell_no, job):
        self.name = name
        self.cell_no = cell_no
        self.job = job

    def print_info(self):
        return f"The name of student is {self.name}, cell no is {self.cell_no}, and his job is {self.job}"


david = Dawood("Dawood", "03367482399", "Python Developer")

# print(david.job)
print(david.print_info())