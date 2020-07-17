"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    if input_array == []:
        return -1
    input_array.sort()
    size = len(input_array)
    low = 0
    high = size - 1

    while low < high:
        mid = (low + high) // 2
        if input_array[mid] < value:
            low = mid + 1
        elif input_array[mid] > value:
            high = mid - 1
        else:
            # element fount
            return mid
    return -1

test_list = [1,3,9,11,15,19,29]
binary_search(test_list,29)
