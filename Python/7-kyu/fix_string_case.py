"""
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
"""

# My Solution :

def solve(s):
    upper = 0
    lower = 0
    for i in s :
        if i.isupper() == True :
            upper = upper + 1
        else :
            lower = lower + 1

    if upper == lower or lower > upper :
        return s.lower()
    else :
        return s.upper()
