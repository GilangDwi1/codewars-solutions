"""
Write a function that returns both the minimum and maximum number of the given list/array.

Examples (Input --> Output)
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
"""

# My Solution :

def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([1,2,3,4,5]))