"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""

# My Solution :

def remove_exclamation_marks(s):
    result = ""

    for i in s :
        if ord(i) == 33 :
            continue
        else :
            result += i

    return result


print(remove_exclamation_marks("Hello World!!!"))