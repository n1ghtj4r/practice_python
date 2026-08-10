print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

#if condition:
#    pass # Code to execute if condition is True

age = 18

if age >= 18:
    print('You are an adult') # You are an adult

age = 18

if age >= 18:
    print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3

age = 12

if age >= 18:
    print('You are an adult') # Nothing shows up in the terminal

#if condition:
 #  pass # Code to execute if condition is True
#else:
 #  pass # Code to execute if condition is False

age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet

age = 12

if age >= 18:
    print('You are an adult')
    print('Almost there!')
else: # SyntaxError: invalid syntax
    print('You are not an adult yet')

#if condition1:
 #  pass # Code to execute if condition1 is True
#elif condition2:
 #  pass # Code to execute if condition1 is False and condition2 is True
#else:
 #  pass # Code to execute if all conditions are False

age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child

age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant