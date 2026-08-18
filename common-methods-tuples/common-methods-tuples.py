programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Rust')) # 2
print(programming_languages.count('JavaScript')) # 0

"""
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count()

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: tuple.count() takes exactly one argument (0 given)
"""

print(programming_languages.index('Java')) # 1

"""
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: tuple.index(x): x not in tuple
"""

programming_languages_doublepy = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages_doublepy.index('Python', 3)) # 5

programming_languages_updated = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages_updated.index('Python', 2, 5)) # 2

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers)) # [2, 3, 7, 13, 18, 45, 67, 78]

programming_languages_sorting = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages_sorting, key=len))

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

programming_languages_reverse = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages_reverse, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']