def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative

print("\n")

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')

print("\n")

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

print("\n")

"""def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')"""

#output error

"""
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    config = parse_config('config.txt')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "main.py", line 7, in parse_config
    raise ValueError('Configuration file is missing') from None
ValueError: Configuration file is missing
"""

#console lines

"""
Traceback (most recent call last):
  File "main.py", line 5, in parse_config
    return int(data)
           ^^^^^^^^^
ValueError: invalid literal for int() with base 10: ''

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "main.py", line 12, in <module>
    config = parse_config('config.txt')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "main.py", line 9, in parse_config
    raise ValueError('Invalid configuration format') from e
ValueError: Invalid configuration format
"""

print("\n")

def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')