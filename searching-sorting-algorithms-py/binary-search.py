# If the target value is found, the index where it's located in the list is returned. 
# If the target value isn't found, -1 is returned. We return -1 because it's not a valid index in most programming languages.

# Here is what the code looks like for linear search

arr = [1, 2, 3, 4, 5]
target = 3

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, target))

# If the list we'll search through is [13, 4, 7, 9, 10] and the target value is 9, the function would return 3 because 9 is at index 3.

# If we changed the target value to 5, the function would return -1 because 5 is not in the list.

# While this is a relatively straightforward algorithm, it is not the most efficient. If you have a large list of items, 
# linear search can take a long time to find the target value.

# The time complexity of linear search is O(n) because the time it takes to search through the list grows linearly with the size of the list.
# The space complexity of linear search is O(1) because it doesn't require any additional space to search through the list.

# Binary search is a more efficient algorithm for searching through a large list of items. 
# The condition here is that the list must be sorted in ascending order.

# Binary search works by dividing the list in half and checking if the target value is in the middle of the list. 
# If the target value is in the middle of the list, the index of the target value is returned. Otherwise, 
# the algorithm checks if the target value is in the left or right half of the list.

# It continues to divide the remaining parts of the list into halves until the target value is found. 
# If the target value is not in the list, it returns -1.

# Here is what the code looks like for binary search

print("\n") # ///////////////////////////////////////////////////////

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary_search(arr, target))

# We start by identifying a low and high index. This represents the range of the list we are searching through.

# We then check the condition of low being less than or equal to high. If low is greater than high, 
# we have searched through the entire list and the target value is not found. In that case we stop the search and return -1.

# If the low index is less than or equal to the high index, we calculate the middle index of the list,
# mid. We then check if the target value is at the middle index. If it is, we return the middle index.

# Otherwise, we check if the value at the midpoint is less than the target. If it is, 
# we update the low index to be the middle index plus one. This means we will search the right half of the list.

# Lastly, if none of the other conditions are True, we update the high index to be the middle index minus one. 
# This means we will search the left half of the list.

# We continue to repeat this process until we find the target or determine that the target is not in the list.

# The time complexity of binary search is O(log n) because the time it takes to search through 
# the list grows logarithmically with the size of the list.

# The space complexity of binary search is O(1) because it doesn't require any additional space to search through the list.