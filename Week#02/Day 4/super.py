# Parent class create kar rahe hain
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):

        # Parent
        super().__init__(name)
        self.roll_no = roll_no
        
student = Student("Dawood", 101)
print(student.name)
print(student.roll_no)