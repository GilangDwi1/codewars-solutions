"""
ask
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
"""

# My Solution :

def sum_array(arr):
    sum = 0
    
    
    if arr == None:
        return 0
    if len(arr) == 0 :
            return 0
    if len(arr) == 1 :
        return 0
    if len(arr) == 2 :
        return 0
    else :
        highest = arr[0]
        lowest = arr[0]
        for i in arr :
            sum += i
            if i > highest :
                highest = i
            if i < lowest :
                lowest = i

    return sum - lowest - highest

print(sum_array([-6, -20, -1, -10, -12]))