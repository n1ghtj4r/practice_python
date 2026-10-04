# The divide and conquer paradigm in computer science is a technique for recursively breaking down problems into smaller sub-problems. 
# One of the key aspects of this technique is recursion, which happens when a function calls itself repeatedly until a base case is reached. 
# In this lesson, we will take a look at the merge sort algorithm to better understand how the divide and conquer technique works.

# Let's say we had this list of numbers
# 42 37 53 17

# The goal is to sort that list from smallest to largest using the merge sort algorithm. The first step is to divide that list in half
# 42 37 | 53 17

# Then we need to look at the left side of the list'
# 42 37

# We take that sub list and divide it in half again until each sub list has only one item in it
# 42 | 37

# A list with only one item in it is sorted by default. Next we need to merge each of those one element sub lists into a sorted list
# 37 42

# Then we follow the same process for the right side of the original list

# right side of original list
#53 17

# divide the list in half
#53 | 17

# merge the lists in sorted order
#17 53

# Now that both halves of the original list are sorted, we merge those two halves together and sort the elements

# 17 37 42 53

# Here is what the algorithm looks like in code

arr = [2, 6, 5, 3, 1, 4]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

print(merge_sort(arr))

# The time complexity for merge sort would be O(n log n) because the list is continuously 
# divided in half (log n) and then merged together (O(n)). Unlike other sorting algorithms like bubble sort, 
# merge sort is not sorted in place and has a space complexity of O(n).