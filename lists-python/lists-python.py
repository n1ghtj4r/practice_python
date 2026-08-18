cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0]) # 'Los Angeles'
print(cities[-1]) # 'Tokyo'

developer = 'Jessica'
print(list(developer)) # ['J', 'e', 's', 's', 'i', 'c', 'a']

numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 5

programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

"""
programming_languages[10] = 'JavaScript'

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""

developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

print('Rust' in programming_languages) # True
print('JavaScript' in programming_languages) # False

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2]) # ['Python', 'Rust', 'C++']
print(developer[2][1]) # 'Rust'

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

"""
developer = ['Alice', 34, 'Rust Developer']
name, age, job, city = developer

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # ['Cookies', 'Ice Cream', 'Pie']

numbers_1 = [1, 2, 3, 4, 5, 6]
print(numbers_1[1::2]) # [2, 4, 6]