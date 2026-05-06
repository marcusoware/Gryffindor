

class School:
    def __init__(self, name, population, city):
        self.name = name
        self.population = population
        self.city = city




class Student(School):
    def __init__(self, name, age, school):
        super().__init__()
        self.name = name
        self.age = age
        self.school = school








Hackman = Student("Kwesi Edutwem", 23, "Japass")
# Newton = Student("joe hart", 19, "University of Manchester")
# Esther = Student()


print(Hackman.city)