products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price)

#990
#600
#250
#70

print("\n")

for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)

#Laptop
#Smartphone
#Tablet
#Headphones

print("\n")

for product in products.items():
    print(product)

#('Laptop', 990)
#('Smartphone', 600)
#('Tablet', 250)
#('Headphones', 70)

print("\n")

for product, price in products.items():
    print(product, price)

#Laptop 990
#Smartphone 600
#Tablet 250
#Headphones 70

print("\n")

products_1 = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products_1.items():
    products_1[product] = round(price * 0.8)

print(products_1) 

for product in enumerate(products):
    print(product)

#(0, 'Laptop')
#(1, 'Smartphone')
#(2, 'Tablet')
#(3, 'Headphones')

print("\n")

for index, product in enumerate(products):
    print(index, product)

for price in enumerate(products.values()):
    print(price)

#(0, 990)
#(1, 600)
#(2, 250)
#(3, 70)

print("\n")

for index, price in enumerate(products.values()):
    print(index, price)

#0 990
#1 600
#2 250
#3 70

print("\n")

for index, product in enumerate(products.items()):
    print(index, product)

#0 ('Laptop', 990)
#1 ('Smartphone', 600)
#2 ('Tablet', 250)
#3 ('Headphones', 70)

print("\n")

for index, product in enumerate(products.items(), 1):
    print(index, product)

#1 ('Laptop', 990)
#2 ('Smartphone', 600)
#3 ('Tablet', 250)
#4 ('Headphones', 70)