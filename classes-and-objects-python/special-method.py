"""
1. Arithmetic operations like addition, subtraction, multiplication, division, and others. For addition, __add__() is called,
 __sub__() for subtraction, __mul__() for multiplication, and __truediv__() for division.

2. String operations like concatenation, repetition, formatting, and conversion to text. __add__() is called for concatenation,
 __mul__() for repetition, __format__() for formatting, __str__() and __repr__() for text conversion, and so on.

3. Comparison operations like equality, less-than, greater-than, and others. __eq__() is called for equality checks, 
__lt__() for less-than, __gt__() for greater-than, and so on.

4. Iteration operations like making an object iterable and advancing through items.
 __iter__() is called to return an iterator and  __next__() to fetch the next item.
"""

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

#print(len(book1)) # TypeError: object of type 'Book' has no len()
#print(str(book1)) # <__main__.Book object at 0x102ed2900>
print(book1 == book2) # False even though they have the same number of pages

print("\n")

"""
Here's how you can define your own __len__(), __str__(), and __eq__() 
special methods to make working with objects created from the Book class easier
"""

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

   def __len__(self):
       return self.pages

   def __str__(self):
       return f"'{self.title}' has {self.pages} pages"

   def __eq__(self, other):
       return self.pages == other.pages
  
book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True

print("\n")

"""
1. __len__() to get the length of the items in the cart

2. __iter__() to loop through the items in the cart so you can see them

3. __contains__() to check if a specific item is in the cart

4. __getitem__() to return or display an item at a specific index in the cart
"""

class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart