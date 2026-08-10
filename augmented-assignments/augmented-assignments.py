#variable <operator>= value
#variable = variable <operator> value

my_var = 10
my_var += 5
print(my_var) # 15

my_var = 10
my_var = my_var + 5
print(my_var) # 15

count = 14
count -= 3
print(count) # 11

product = 65
product *= 7
print(product) # 455

price = 100
price /= 4
print(price) # 25.0

total_pages = 23
total_pages //= 5
print(total_pages) # 4

bits = 35
bits %= 2
print(bits) # 1

power = 2
power **= 3
print(power) # 8

greet = 'Hello'
greet += ' World'
print(greet) # Hello World

greet = 'Hello'
greet *= 3
print(greet) # HelloHelloHello

#greet = 'Hello'
#greet -= ' World'
#print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


#greet = 'Hello'
#greet /= 'World'
#print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 

my_var = 5
print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1
print(my_var) # 6