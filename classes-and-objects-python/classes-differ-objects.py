class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):               
        print(f"Name: \"{self.name.upper()}\", and Age is: \"{self.age}\"")

classmate = ClassName("ver", 15)
classmate.sample_method()

print("\n")

class Dog_met1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof!")
        print(f"and {self.name.upper()} is {self.age} years old.")

dogs = Dog_met1("white", 5)
dogs.bark()

print("\n")

#object_1 = ClassName(attribute_1, attribute_2) // With this Dog class, you can create an object. Here's the basic syntax for creating objects from a class 
#object_2 = ClassName(attribute_1, attribute_2)

#object_1.method_name() // You can also call any of the methods defined in the class from each object
#object_2.method_name()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!