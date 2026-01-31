import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Merging the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Generate a list of 5000 random numbers between 0 and 5000
random_array = [random.randint(0, 5000) for _ in range(5000)]

print("Original Array: ")
print(random_array[:5000])  # Print the first 100 elements to check

# Sort the array
merge_sort(random_array)

print("\nSorted Array: ")
print(random_array[:5000])  # Print the first 100 elements to check
