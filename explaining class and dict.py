##__dict__ is a special attribute that acts as a namespace
##python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog("Rex", "Collie")
print(my_dog.__dict__)