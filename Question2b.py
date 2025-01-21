# Wei Qi

# -----------------------------------------------------------------------------
# Constant Algorithm O(1)
# -----------------------------------------------------------------------------
def constant_is_double(n):
    return n * 2

constant_is_double(4)



# -----------------------------------------------------------------------------
# Logarithmic Algorithm o(logn)
# -----------------------------------------------------------------------------
logarithmic_array = []


# -----------------------------------------------------------------------------
# Linear Algorithm O(n)
# -----------------------------------------------------------------------------
linear_array = [3,4,5,6,7]

def linear_max(array):
    max = array[0]
    for i in array:
        if i > max:
            max = i
    return max

linear_max(linear_array)

#O(n) occurs when the numbers go in ascending order from array[0] e.g. [1,2,3,4,5]
#Best case scenario occurs when the largest number in the array occurs in array[0] e.g. [5,3,4,2,1]

# -----------------------------------------------------------------------------
# Linearithmic Algorithm O(nlogn)
# -----------------------------------------------------------------------------
linearthimic_array = []




# -----------------------------------------------------------------------------
# Quadratic Algorithm O(n^2)
# -----------------------------------------------------------------------------
quadratic_array = [1,2,3,4,5]

def quadratic_comparison(array, target_num):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == target_num:
                return True
    return False

#O(n^2) occurs when the desired target number is the last combination in the array e.g. array = [0,1,2,3,4,5] and the target number is 10. 
#This means the for loop will reach array[6] + array[6] meaning it will iterate the nested for loop 36 times before returning a True case. 
#Best case scenario occurs when the desired target number is the first combination in the array e.g. array = [0,1,2,3,4,5] and the target number is 0.
#This means the for loop will reach array[0] + array[0] meaning it will iterate the nested for loop only 1 time before returning a True case.

# -----------------------------------------------------------------------------
# Exponential Algorithm O(2^n)
# -----------------------------------------------------------------------------
exponential_array = [7,2,4]

def exponential_powerset(array):
    if not array:
        return [[]]
    powerset = exponential_powerset(array[:-1])

#
#
#
#

# -----------------------------------------------------------------------------
# Factorial Algorithm O(n!)
# -----------------------------------------------------------------------------
factorial_array = []

