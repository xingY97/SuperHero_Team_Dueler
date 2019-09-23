class Dog:
    #required properties are defined inside the __init__ constructor method
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    # methods are definded as their own named functions insie the class
    def bark(self):
        print("woof!")
my_dog = Dog ("Rex","superDog")
#my_dog.bark()
#print(my_dog.name)
#print(my_dog.breed)
