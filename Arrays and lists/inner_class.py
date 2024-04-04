
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.rollno)
 # Accessing Inner Class Instance Methods

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)
if __name__ == '__main__':
 s1 = Student("Atif", 1)
 s2 = Student("Aqib", 2)
 s1.show()
 # Accessing Inner Class
 s1.lap.show()
 laptop1 = Student.Laptop()
 laptop1.show()
 print(laptop1.__class__.__name__)
 print(s1.lap)