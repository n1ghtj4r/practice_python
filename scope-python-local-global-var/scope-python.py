def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

#print(my_var) # NameError: name 'my_var' is not defined

def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!

#def outer_func():
 #   msg = 'Hello there!'
  #  print(res)

   # def inner_func():
    #    res = 'How are you?'
     #   print(msg)

#    inner_func()

#outer_func() # NameError: name 'res' is not defined

def outer_func():
    msg = 'Hello there!!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?

my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False