developer = ('Alice', 34, 'Rust Developer')
print(developer[1]) # 34

"""
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""

numbers = (1, 2, 3, 4, 5)
print(numbers[-2]) # 4

"""
numbers[7]

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
"""

developer_tuple = 'Jessica'
print(tuple(developer_tuple)) # ('J', 'e', 's', 's', 'i', 'c', 'a')

programming_languages = ('Python', 'Java', 'C++', 'Rust')

print('Rust' in programming_languages) # True
print('JavaScript' in programming_languages) # False

developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3]) # ('pie', 'cookies')

"""
developer = ('Jane Doe', 23, 'Python Developer')
del developer[1]

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: "tuple" object doesn't support item deletion
"""