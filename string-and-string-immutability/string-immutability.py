my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

print("")

my_str = 'Hello world'
print(len(my_str))  # 11

print("")

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

print("")

my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

print("")

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

print("")

#greeting = 'hi'
#greeting[0] = 'H' # TypeError: 'str' object does not support item assignment