def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    
    pivot = arr[0]  # Choose the first element as pivot
    
    less = []
    equal = []
    greater = []
    
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    
    return quick_sort(less) + equal + quick_sort(greater)

# Test cases
print(quick_sort([]))
print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))