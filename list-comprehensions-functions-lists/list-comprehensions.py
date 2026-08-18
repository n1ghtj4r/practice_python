even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

#[(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60

numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60