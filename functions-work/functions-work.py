name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

def hello():
    print('Hello World')

hello() # Hello World

def calculate_sum(a, b):
    print(a + b)

calculate_sum(3, 1) # 4

# calculate_sum() TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4