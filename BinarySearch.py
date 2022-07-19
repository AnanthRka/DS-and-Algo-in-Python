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
    """Your code goes here."""
    l = len(input_array)
    left = 0
    right = l-1
    while left<=right:
        mid = (left +right)//2
        # print(input_array[mid])
        # print(mid, left ,right)
        if input_array[mid] < value:
            left = mid +1
        elif input_array[mid] > value:
            right = mid -1
        else:
            return mid
        # print(input_array[mid])
        # print(mid)
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))