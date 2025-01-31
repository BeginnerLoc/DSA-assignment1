# Wei Qi

# -----------------------------------------------------------------------------
# Constant Algorithm O(1)
# -----------------------------------------------------------------------------

#Program to double a number
def constant_is_double(n):
    return n * 2

print(f"The outcome of the constant algorithm is {constant_is_double(3)}")
'''
Conditions on Input:
Input n must be an integer or floating-point number.
Must not be a string or other non-numeric type.

Conditions on Output:
Returns a single number which is double the input.
'''
# -----------------------------------------------------------------------------
# Logarithmic Algorithm o(logn)
# -----------------------------------------------------------------------------

#Program to find largest power of two less than or equal to n
def logarithmic_power(n):
    power = 1
    if n == 0:
        return None
    while 2 ** power <= n:
        power += 1
    return power - 1

print(f"The outcome of the logarithmic algorithm is {logarithmic_power(50)}")

'''
Conditions on Input:
n must be a positive integer.
Input cannot be negative or zero.

Conditions on Output:
Returns the largest power of 2 that is ≤ n.
'''

# -----------------------------------------------------------------------------
# Linear Algorithm O(n)
# -----------------------------------------------------------------------------

#Program to find the largest number in an array
linear_array = [3,4,5,6,7]

def linear_max(array):
    max = array[0]
    for i in array:
        if i > max:
            max = i
    return max

print(f"The outcome of the linear algorithm is {linear_max(linear_array)}")
'''
Conditions on Input:
Input must be a list of integers.
List must not be empty.

Conditions on Output:
Returns the largest integer in the list.
'''

# -----------------------------------------------------------------------------
# Linearithmic Algorithm O(nlogn)
# -----------------------------------------------------------------------------

#Program to sort an array (Heap Sort)
linearithmic_array = [3,1,5,8,2]

def linearithmic_heap_sort(array):    
    n = len(array)

    #Finds the largest element in the array
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

print(f"The outcome of the linearithmic algorithm is {linearithmic_heap_sort(linearithmic_array)}")

'''
Conditions on Input:
Input must be a list of integers.
The list can contain duplicates.

Conditions on Output:
Returns a sorted version of the list.
'''

# -----------------------------------------------------------------------------
# Quadratic Algorithm O(n^2)
# -----------------------------------------------------------------------------

#Program to find two numbers in an array that add up to a target number
quadratic_array = [1,2,3,4,5]

def quadratic_comparison(array, target_num):
    comparisons = 0  
    for i in range(len(array)):
        for j in range(len(array)):
            comparisons += 1  
            if array[i] + array[j] == target_num:
                print(f"Total comparisons made: {comparisons}")
                return True
    print(f"Total comparisons made: {comparisons}")
    return False

print(f"The outcome of the quadratic algorithm is {quadratic_comparison(quadratic_array, 10)}")

'''
Conditions on Input:
array must be a list of integers.
target_num must be an integer.

Conditions on Output:
Returns True if two numbers in the list sum up to target_num, otherwise False.
'''

# -----------------------------------------------------------------------------
# Exponential Algorithm O(2^n)
# -----------------------------------------------------------------------------

#Program to find the powerset of an array
exponential_array = [1,2,3]

def exponential_powerset(array):
    if len(array) == 0:
        return [[]]
    subsets = exponential_powerset(array[1:])
    return subsets + [[array[0]] + subset for subset in subsets]

print(f"The outcome of the exponential algorithm is {exponential_powerset(exponential_array)}")
'''
Conditions on Input:
Input must be a list of integers.
The list can contain duplicates.

Conditions on Output:
Returns all possible subsets of the list.
'''
# -----------------------------------------------------------------------------
# Factorial Algorithm O(n!)
# -----------------------------------------------------------------------------

#Program to find all permutations of an array
factorial_array = [1,2,3]

def factorial_permutations(array):
    permutations = []
    if len(array) == 0:
        return [[]]
    for i in range(len(array)):
        for j in factorial_permutations(array[:i] + array[i+1:]):
            permutations.append([array[i]] + j)
    return permutations

print(f"The outcome of the factorial algorithm is {factorial_permutations(factorial_array)}")

'''
Conditions on Input:
Input must be a list of integers.
The list must be non-empty.

Conditions on Output:
Returns all possible permutations of the list.
'''
