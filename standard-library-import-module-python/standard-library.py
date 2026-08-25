#import module_name //importing module

import math #importing library
import math as m 

#from module_name import name1 as alias1, name2 as alias2 <---> //If you want to assign aliases to these names, 
# you can do that by using the as keyword after each, 
# followed by the alias you want to use

#from module_name import name1, name2 <---> //Now the import statement starts with from, followed by the name of the module, 
# and then the import keyword followed by the name of the elements that you want to import

#import module_name as module_alias <---> //This is often used to shorten long module names, or to avoid naming conflicts.

#module_name.function_name() <---> //if you need to call a function from that module in your Python script, 
# you would use dot notation, with the name of the module followed by the name of the function

#from module_name import * <---> //And finally, we find this import statement that ends with an asterisk. 
# The asterisk is telling Python that you want to import everything in that module, 
# but you want to import it so that you don't need to use the name of the module as a prefix

from math import radians, sin, cos
from math import *
import math
import datetime

print("Using normal call")
print(math.sqrt(36)) # 6.0
print(m.sqrt(36)) # 6.0

print("\n")

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print("Naming import of the function")
print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

print("\n")

print("Calling all function with \"*\" ")
print(sqrt(36))  # 6.0
print(pow(5, 2)) # 25.0
print(exp(1))    # 2.718281828459045

print("\n")

print("Number of pi") #Here is an example of a constant from the math module, the number pi
print(math.pi)

print("\n")

print("Import class of datetime")
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959

#if __name__ == '__main__': <---> // __name__ is a special built-in variable in Python.

# When a Python file is executed directly, Python sets the value of this variable to the string "__main__".

# But if the Python file is imported as a module into another Python script, 
# the value of the __name__ variable is set to the name of that module (usually the filename without the .py extension).