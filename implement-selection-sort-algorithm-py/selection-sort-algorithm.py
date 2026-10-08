def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the index of the minimum element in the unsorted portion
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap only if the minimum is not already in the correct position
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

print(selection_sort([33, 1, 89, 2, 67, 245]))
# Output: [1, 2, 33, 67, 89, 245]

print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
# Output: [3, 5, 12, 15, 16, 23, 72, 99, 567]