"""
This really depends on the algorithm that you choose to sort them.

Big O notation will not give you an exact number to describe the algorithm's efficiency, 
but it will give you an idea of how it scales as the input size grows, based on the number of operations performed by the algorithm.

In Big O notation, we usually denote input size with the letter n. For example, if the input is a list, 
n would denote the number of elements in that list.

Constant factors and lower-order terms are not taken into account to find the time complexity of an algorithm based on the number of operations. 
That's because as the size of n grows, the impact of these smaller terms in the total number of operations performed will become smaller and smaller.

The term that will dominate the overall behavior of the algorithm will be the highest order term with n, the input size.

For example, if an algorithm performs 7n + 20 operations to be completed, 
the impact of the constant 20 on the final result will be smaller and smaller as n grows. 
The term 7n will tend to dominate and this will define the overall behavior and efficiency of the algorithm.

Another example would be an algorithm that takes 20n² + 15n + 7 operations to be completed. The term 20n² will tend to dominate as n grows, 
so this algorithm would have a quadratic time complexity because the dominant term has n².

Quadratic time complexity is one of many different types of time complexities that you can find in the world of algorithms.

Let's learn about some of the most common ones.

O(1) is known as "Constant Time Complexity". When an algorithm has constant time complexity, it takes the same amount of time to run, 
regardless of input size.

For example, checking if a number is even or odd will always take the same amount of time, regardless of the number itself.
"""

def check_even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(check_even_or_odd(5))

"""
O(log n) is known as "Logarithmic Time Complexity". This means that the time required by the algorithm increases slowly as the input size grows. 
This is common in problems in which the size of the problem is repeatedly reduced by a constant fraction.

For example, a popular search algorithm called Binary Search has O(log n) worst-case time complexity. 
This is because it eliminates half of the remaining elements in each comparison, which makes it more efficient overall.

O(n) is known as "Linear Time Complexity". The running time of algorithms with this time complexity increases proportionally to the input size.

For example, a for loop that iterates over all the elements of a list will perform more iterations as the number of list elements increases. 
If the list is doubled in size, the number of operations will approximately double as well.
"""

#for grade in grades:  # grades is a list.
 #   print(grade)

"""
O(n log n) is known as "Log-Linear Time Complexity". This is a common time complexity of efficient sorting algorithms, 
like Merge Sort and Quick Sort.

O(n²) is known as "Quadratic Time Complexity". The running time of these algorithms increases quadratically relative to the input size,
 which is generally not efficient for real-world problems.

Nested loops are a common example of quadratic time complexity. The inner loop will perform n iterations for each one of the n iterations of the outer loop, 
resulting in n squared iterations.
"""

#for i in range(n):
 #   for j in range(n):
  #      print("Hello, World!")

"""
Other time complexities include "Exponential Time Complexity", denoted as O(2^n), 
and "Factorial Time Complexity", denoted as O(n!). Both are inefficient for real-world scenarios.

In this graph, you can compare the growth of the mathematical functions that represent the most common time complexities. 
Think of the x-axis (horizontal) as the input size and the y-axis (vertical) as the running time of the algorithm.

You can see that the Quadratic Time Complexity (O(n²)) (yellow) grows much faster than the other ones, while the Constant Time Complexity 
(O(1)) (red) stays constant, even if the input gets larger.
"""