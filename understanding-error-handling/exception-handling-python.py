# run it as python file, it has a input variable
"""
try: The block of code where you anticipate an error might occur.

except: This block runs if an error of the specified type is raised inside the try block.

In this case, dividing by zero raises a ZeroDivisionError, which is then caught and handled.
"""
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

print("\n")

"""
else: Runs if no exception is raised in the try block.

finally: Runs no matter what, whether or not an exception occurred. Useful for clean-up tasks like closing files or releasing resources.
"""

try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')

print("\n")

# By using separate except clauses, you can make your error responses more specific and useful.

try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")

print("\n")

# You can also use the exception object, which is typically aliased to another name with the as keyword. 
# Here we're using e as an alias for the error object

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')

print("\n")

# You can also catch multiple exceptions in a single except clause by specifying the exceptions as a tuple

try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')