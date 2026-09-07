from abc import ABC, abstractmethod

"""
As for how Python implements abstraction, it does so through the abc module.

This module provides the ABC class (standing for “abstract base class”) and the @abstractmethod decorator.

ABC is the class that is meant to be inherited from, but you cannot create direct objects from it. 
It is what defines a common interface of methods and properties that its subclasses must implement.

On the other hand, an abstract method is a method declared in an Abstract Base Class (ABC) using the @abstractmethod decorator. 
It may have no implementation or a basic default one. However, any subclass must override it to be considered concrete and instantiable, 
even if a default implementation is provided.
"""

# Define an abstract base class
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Concrete subclass that implements the abstract method
class ConcreteClassOne(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassOne')

# Another concrete subclass
class ConcreteClassTwo(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassTwo')

print("\n")#///////////////////

from abc import ABC, abstractmethod

class Animal(ABC): # Inherits from abstract base class
   @abstractmethod # Abstract method decorator
   def make_sound(self):  # The method subclasses must override
       pass

# Concrete class that will override the abstract method
class Dog(Animal):
   def make_sound(self):
       print('Woof!')

# Another concrete class that will override the abstract method
class Cat(Animal):
   def make_sound(self):
       print('Meow!')

# Another concrete class that will override the abstract method
class Monkey(Animal):
   def make_sound(self):
       print('Ooh ooh aah aah!')

# Create instances of each concrete class
animals = [Dog(), Cat(), Monkey()]

# Loop through the instances to call the make_sound method
for animal in animals:
   animal.make_sound()

# Output:
# Woof!
# Meow!
# Ooh ooh aah aah!

"""
In this example

We are importing the ABC class and abstractmethod from the abc module.
We then create an Animal class that inherits from ABC, and create an abstract method make_sound in it that each subclass of Animal must override.
We create the concrete classes Dog, Cat, and Monkey, which must override the make_sound abstract method.
We instantiate the concrete classes and call their make_sound method to show how each of them implements the make_sound abstract method in its own way.
"""

#dog = Animal() 
# TypeError: Can't instantiate abstract class Animal 
# without an implementation for abstract method 'make_sound'

class Bird(Animal):
    pass

#bird = Bird()
# TypeError: Can't instantiate abstract class Bird 
# without an implementation for abstract method 'make_sound'

print("\n")#///////////////////

from abc import ABC, abstractmethod

# The blueprint for any toy that can speak
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name
   @abstractmethod
   def speak(self):
       pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')

# Create toys
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
   toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!

"""
In this example.

We have an abstract base class TalkingToy that defines a blueprint for any toy that can speak.
The subclasses RobotToy, TeddyBearToy, and DinosaurToy implement the speak method in their own way.
When we create instances of these subclasses and call the speak method, each toy speaks in its own unique way.
"""