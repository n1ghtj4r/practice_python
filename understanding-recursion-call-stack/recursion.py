# Recursive functions can solve problems with an unknown depth, such as traversing a file tree. 
# They can also perform simpler tasks, such as counting down from a given number.

# Here is a function named recursive_countdown that accepts a number and prints it

def recursive_countdown(number):
    print(number)

recursive_countdown(5)

# Calling the function prints 5, but it does not count down yet. Before making the function call itself, 
# you need to define its base case. Without a reachable base case, the function will keep calling itself. 
# Python eventually stops the calls and raises a RecursionError.

# For this countdown, the function should stop when number is less than 1

print("\n")#//////////////////////////////////////////

def recursive_countdown(number):
    if number < 1:
        return
    print(number)

recursive_countdown(5)

# The if statement is the base case. When number is less than 1, return ends that function call.

# The function still needs a recursive case. The recursive case calls the function again with an argument 
# that moves it toward the base case. To count down, call recursive_countdown with number - 1

print("\n")#//////////////////////////////////////////

def recursive_countdown(number):
    if number < 1:
        return
    print(number)
    recursive_countdown(number - 1)

recursive_countdown(5)

# This prints the numbers 5, 4, 3, 2, and 1.

# The position of the recursive call changes when the numbers are printed. 
# If the print() call comes after the recursive call, the function prints the numbers in ascending order

print("\n")#//////////////////////////////////////////

def recursive_countdown(number):
    if number < 1:
        return
    recursive_countdown(number - 1)
    print(number)

recursive_countdown(5)

# This prints the numbers 1, 2, 3, 4, and 5. To understand why, you need to understand the call stack.

# The call stack is a last-in, first-out data structure that Python uses to keep track of active function calls. 
# When a function is called, Python adds a frame for that call to the top of the stack. The frame contains information 
# such as the function's arguments and local variables.

# Consider this version of the countdown

print("\n")#//////////////////////////////////////////

def recursive_countdown(number):
    print(f'Function call started for number: {number}')
    if number < 1:
        print('Base case reached')
        return
    print(f'Calling recursive_countdown with number: {number - 1}')
    recursive_countdown(number - 1)
    print(f'Function call completed for number: {number}')

recursive_countdown(3)

# The output is:

# Function call started for number: 3
# Calling recursive_countdown with number: 2
# Function call started for number: 2
# Calling recursive_countdown with number: 1
# Function call started for number: 1
# Calling recursive_countdown with number: 0
# Function call started for number: 0
# Base case reached
# Function call completed for number: 1
# Function call completed for number: 2
# Function call completed for number: 3

# The call to recursive_countdown(3) pauses when it calls recursive_countdown(2). 
# The call with 2 pauses when it calls the function with 1, and the call with 1 pauses when it calls the function with 0.

# The call with 0 reaches the base case and returns. Python removes that call from the top of the stack, 
# so the call with 1 resumes after its recursive call. The remaining calls then resume and return in reverse order: 1, 2, and 3.