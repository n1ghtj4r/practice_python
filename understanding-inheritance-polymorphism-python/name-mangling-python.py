class Example:
    def __init__(self):
        self._internal = 'I can be accessed from outside the class, but should not'
        self.__private = 'You cannot access me directly from outside the class'

obj = Example()

print(obj._internal) # I can be accessed from outside the class, but should not
#print(obj.__private)  # AttributeError: 'Example' object has no attribute '__private'

"""
Prefixing an attribute with a double underscore triggers Python's name mangling process, 
in which Python internally renames the attribute by adding an underscore and the class name as a prefix, 
turning __attribute into _ClassName__attribute.
"""

"""
To see this in action, you create an instance of the class and use the __dict__ 
special attribute of that instance, which is a dictionary containing the object's attributes
"""

print("\n")#////////////////////

class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example1.__dict__)

#result:

"""
{
  '_internal': 'I can be accessed from outside the class, but should not',
  '_Example__private': 'I cannot be accessed directly from outside the class'
}
"""

print("\n")#////////////////////

"""
As you can see, the __private attribute is stored as _Example__private. 
This means you can still access that attribute outside the class this way
"""

class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)
example2 = Example(
    'I should not be accessed from outside the class',
    'But I can be accessed from outside the class with name mangling'
)

print(example1._Example__private) # I cannot be accessed directly from outside the class
print(example2._Example__private) # But I can be accessed from outside the class with name mangling

#here are getting and setting examples, polymorphism
#and difference of underscoreses

print("\n")#////////////////////

class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}

print("\n")#////////////////////

class Parent:
   def __init__(self):
       self.data = 'Parent data'

class Child(Parent):
   def __init__(self):
       super().__init__()
       self.data = 'Child data'

c = Child()
print(c.__dict__)  # {'data': 'Child data'}

"""
So, which should you use to prefix attributes between single underscore (_) and double underscore (__)? It depends. 
If an attribute is only meant for internal use within the class, stick with a single underscore.
"""