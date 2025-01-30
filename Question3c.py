# -----------------------------------------------------------------------------
# Quick Sort with Lomuto Partition Scheme
# -----------------------------------------------------------------------------

def lomuto_partition(arr, low, high):
    pivot = arr[high]  # Pivot is the last element
    i = low - 1  # Pointer for the smaller element
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot into correct place
    return i + 1  # Return the pivot index

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = lomuto_partition(arr, low, high)  # Partition the array
        quick_sort(arr, low, pivot_index - 1)  # Recursively sort the left part
        quick_sort(arr, pivot_index + 1, high)  # Recursively sort the right part

# Test the quick sort with Lomuto partition scheme
arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
quick_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)

# -----------------------------------------------------------------------------
# Bucket Sort
# -----------------------------------------------------------------------------

def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)] # Create the buckets based on the size of the array
    
    for num in arr:
        bucket_index = int((num - min_val) * (bucket_count - 1) // (max_val - min_val)) # Calculate the index of the bucket for the current element using the formula
        buckets[bucket_index].append(num) # Insert the element into the corresponding bucket

    for i in range(bucket_count):
        buckets[i].sort()  # Sorting each bucket using any efficient sorting algorithm
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)  # Concatenate the sorted buckets to get the final sorted array

    return sorted_arr

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)

print("Sorted Array:", sorted_arr)