numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5]

extend_num = [50]
numbers.extend(extend_num)
print(numbers)

numbers.remove(50)
print(numbers, "Removed number \"50\"") # [10, 20, 30, 40, 50]

numbers.pop(1) # The number 2 is returned
print(numbers)

numbers.pop() # The number 5 is returned
print(numbers)

numbers.clear()
print(numbers) # [] clear all values in the list

unsort_numbers = [19, 2, 35, 1, 67, 41]
unsort_numbers.sort()
print(unsort_numbers) # [1, 2, 19, 35, 41, 67] sorting number smaller to bigest

numbers_example = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers_example) # method to sort with variable
print(numbers_example) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

numbers_reverse = [6, 5, 4, 3, 2, 1]
numbers_reverse.reverse()
print(numbers_reverse) # [1, 2, 3, 4, 5, 6] reverse value

programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java')) # 1

"""
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('JavaScript')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""