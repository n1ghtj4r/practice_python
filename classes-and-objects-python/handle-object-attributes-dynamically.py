"""
Python gives you four handy built-in functions to dynamically work with object attributes. 
They are getattr(), setattr(), hasattr(), and delattr().
"""

class Car: 
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 

my_car = Car('Lamborghini', 'Gallardo') 
print(my_car.brand) # Lamborghini 
print(my_car.model) # Gallardo 

print("\n") # Example 2 /////////////////////////////////////////////////////////

"""
getattr() makes it possible to read an attribute from an object when you don't know its name until runtime. 
If the attribute doesn't exist, it raises an AttributeError, unless you provide a default value.
"""

#getattr(object, attribute_name, default_value) /////////////---------

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30) 
 
print(getattr(person, 'name')) # John Doe 
print(getattr(person, 'age')) # 30 
print(getattr(person, 'city', 'Milano')) # Milano

print("\n") # Example 3 /////////////////////////////////////////////////////////

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))
 
print("\n") # Example 4 /////////////////////////////////////////////////////////

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

# Loop through all attributes of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)): 
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Output
# age: 30
# name: John Doe

print("\n") # Example 5 /////////////////////////////////////////////////////////

"""
The setattr() function lets you create a new attribute or update an existing one dynamically. 
The syntax looks like this
"""

#setattr(object, attribute_name, value) /////////////---------

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30

print("\n") # Example 6 /////////////////////////////////////////////////////////

"""
There is also hasattr(). Before you do something with an attribute or delete it, 
it's a good practice to check if it exists. That's what hasattr() lets you do. 
It checks if an attribute exists and returns True or False based on the result.
"""

#hasattr(object, attribute_name)  /////////////---------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        # Access the attributes dynamically once their existence is confirmed
        print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'

print("\n") # Example 7 /////////////////////////////////////////////////////////

"""
Lastly, delattr() lets you remove an attribute dynamically
"""

#delattr(object, attribute_name) /////////////---------

class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token # sensitive
        self.temp_counter = 0 # temporary

session = UserSession(101, 'a1b2c3d4e5')

# List of attributes to remove dynamically before "saving" the session
attributes_to_clean = ['auth_token', 'temp_counter']

# Dynamically remove specified attributes
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

# Loop through the remaining attributes with dir()
for attr in dir(session):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')

# Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter

# Final attributes remaining:
#  - user_id: 101