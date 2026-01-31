import random

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
      
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# Generate a list of 5000 random numbers between 0 and 5000
original_array = [random.randint(0, 10000) for _ in range(10000)]

print("Original Array (first 100 elements): ")
print(original_array[:10000])  # Print the first 100 elements to check

# Sort the original array in place
insertion_sort(original_array)

print("\nSorted Original Array (first 100 elements): ")
print(original_array[:10000])  # Print the first 100 elements of the sorted array
