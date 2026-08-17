class David:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        return f"THE NAME IS {self.name} and age is {self.age} years old"


muhammad = David("Papa", 100)
dawood = David("Daddy", 200)

print(muhammad.output())
print(dawood.output())