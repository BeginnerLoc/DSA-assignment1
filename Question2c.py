def three_way_split(arr,l,r):
    
    if l>=r:
        # Base case: single element or empty array
        return [arr[l]] if l == r else []

    # Split the array into three sub arrays with approximately size n/2
    n = r - l + 1
    mid1 = l + n // 4  
    mid2 = l + n // 2

    # Recursive sorting
    left_subarr = three_way_split(arr, l, mid2 - 1)
    middle_subarr = three_way_split(arr, mid1, mid1 + n//2 - 1)
    right_subarr = three_way_split(arr, mid2, r)

    # Merge the sorted arrays
    return merge_sort(left_subarr, middle_subarr, right_subarr)

def merge_sort(left_subarr, middle_subarr, right_subarr):  # Merge three sorted arrays
    merged = []
    i = j = k = 0

    # Merge elements from the three subarrays
    while i < len(left_subarr) or j < len(middle_subarr) or k < len(right_subarr):
        # Initialize variables to hold the current elements for comparison for each subarrays
        current_left = left_subarr[i] if i < len(left_subarr) else None
        current_middle = middle_subarr[j] if j < len(middle_subarr) else None
        current_right = right_subarr[k] if k < len(right_subarr) else None

        # Compare current elements and append the smallest to the merged array
        # Check if the element in the left array is the smallest
        if current_left is not None and (current_middle is None or current_left <= current_middle
            ) and (current_right is None or current_left <= current_right):
            if not merged or current_left != merged[-1]:
                merged.append(current_left)
            i += 1
        # Check if the element in the middle array is the smallest
        elif current_middle is not None and (current_right is None or current_middle <= current_right):
            if not merged or current_middle != merged[-1]:
                merged.append(current_middle)
            j += 1
        else: # The element in the right array is the smallest
            if not merged or current_right != merged[-1]:
                merged.append(current_right)
            k += 1

    return merged




# Usage
input_string = input("Enter the numbers you would like to sort (separated by a comma): ")
array = list(map(int, input_string.split(',')))
sorted_array = three_way_split(array,0,len(array)-1)
print("Sorted Array:", sorted_array)