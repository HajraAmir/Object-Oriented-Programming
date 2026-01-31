import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Merge until one of the halves is exhausted
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append remaining elements from left half
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Append remaining elements from right half
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

# Generating 5000 random numbers
random_numbers = [random.randint(1, 10000) for _ in range(5000)]

# Sorting the random numbers using Merge Sort
sorted_numbers = merge_sort(random_numbers)

# Printing the sorted numbers (optional)
print(sorted_numbers)
