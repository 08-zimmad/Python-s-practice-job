class Student:
    university="Bahria University"
    def __init__(self) -> None:
        self._name="" # public variable
        self._class="" # protected has 1 underscore
        self.__cgpa=0.0

    @property
    def name(self):
        return self._name
    
    @property
    def cgpa(self):
        return self.__cgpa
    
    @property
    def _class_(self):
        return self._class
    
    @name.setter
    def name(self,value):
        self._name=value

    @_class_.setter
    def _class_(self,value):
        self._class=value


    @cgpa.setter
    def cgpa(self,value):
        self.__cgpa=value


if __name__=="__main__":
    
    obj1=Student()
    obj1._class_="IG1"
    obj1.name='zimmad'
    obj1.cgpa=3.2

    print(f"Name: {obj1.name} \n class: {obj1._class}\n cgpa: {obj1.cgpa}")

