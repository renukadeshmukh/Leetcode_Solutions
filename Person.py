
#Object Oriented Programming


#Class : Bundles perperties and functionality together
#Object: One instance of a class 
class Person:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def print_person(self):
        print(self.first_name, self.last_name, self.age)



p1 = Person("Harry", "Potter", 15)
p1.print_person()
print(p1.__dict__)
print("Person p1 details are : ", p1.first_name, p1.last_name, p1.age)

p2 = Person("Hermoine", "Granger", 16)
p2.print_person()

p3=Person("Ron", "Weasley", 17)
p3.print_person()

