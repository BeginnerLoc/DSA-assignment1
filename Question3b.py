# Stable Sorting Algorithm - Merge Sort





# -----------------------------------------------------------------------------
# Unstable Sorting Algorithm - Quick Sort
# -----------------------------------------------------------------------------

Arr = [8,2,4,6,7,8,5]

def QuickSort(inputArr) :

    # Array <= 1 element means already sorted
    if len(inputArr) <= 1: 
        return inputArr

    # Choose a pivot, in this case, we use the last value in the array
    pivot = inputArr[-1]
    less_than_pivot, equal_to_pivot, greater_than_pivot = [], [], []
    
    # Iterate through all the elements in the array
    for x in inputArr:
        # Values less than pivot in one array. Values more than pivot in another array
        if x < pivot:
            less_than_pivot.append(x)
        elif x > pivot:
            greater_than_pivot.append(x)
        else:
            equal_to_pivot.append(x)

    #  Recursively sort the sub arrays and combine the results
    return QuickSort(less_than_pivot) + equal_to_pivot + QuickSort(greater_than_pivot)

print(QuickSort(Arr))

