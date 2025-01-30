# -----------------------------------------------------------------------------
# Stable Sorting Algorithm - Insertion Sort
# -----------------------------------------------------------------------------
array = [1,8,2,3,4,5,6,10,7,14]

for ptr in range(1, len(array)):
    ptrvalue = array[ptr]
    ptrminusone = ptr - 1

    while ptrminusone >= 0:
        if ptrvalue < array[ptrminusone]:
            array[ptrminusone+1] = array[ptrminusone]   # Shift number in ptr-1 to ptr
            array[ptrminusone] = ptrvalue           # Shift number in ptr to ptr-1
            ptrminusone = ptrminusone - 1

        else:
            break

print("hello")
print(array)


# -----------------------------------------------------------------------------
# Unstable Sorting Algorithm - Heap Sort
# -----------------------------------------------------------------------------
def heapify(arr, n, i): 

    largest = i  # Assume root (largest) as the largest element 
    left = 2 * i + 1  # Left child index 
    right = 2 * i + 2  # Right child index 

    # Check if left child exists and is greater than root 
    if left < n and arr[left] > arr[largest]: 
        largest = left

    # Check if right child exists and is greater than root 
    if right < n and arr[right] > arr[largest]: 
        largest = right 

    # If largest is not root, swap and continue heapifying 
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest)  # Recursively heapify the affected subtree 

  

def heap_sort(arr): 
    n = len(arr) 
    # Step 1: Build a max heap 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 


    # Step 2: Extract elements one by one from the heap 
    for i in range(n - 1, 0, -1): 

        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max) with the last element 

        heapify(arr, i, 0)  # Heapify the reduced heap 

