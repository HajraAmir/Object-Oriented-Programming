import random

def counting_sort(arr, max_val):
    # Create a count array to store the count of each unique object
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # Store the count of each element in count array
    for number in arr:
        count[number] += 1

    # Change count[i] so that count[i] now contains the actual position of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for number in reversed(arr):
        output[count[number] - 1] = number
        count[number] -= 1

    
    for i in range(len(arr)):
        arr[i] = output[i]

original_array = [random.randint(0, 10000) for _ in range(10000)]

print("Original Array  ")
print(original_array[:10000])  


max_val = 10000


counting_sort(original_array, max_val)

print("\nSorted Original Array : ")
print(original_array[:10000])  
