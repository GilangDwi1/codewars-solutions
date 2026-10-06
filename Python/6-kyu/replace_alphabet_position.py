"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""

# My Solution :

def alphabet_position(text):
    ascii = []
    for i in text :
        flag = ord(i)
        if flag >= 97 and flag <=122:
            upper = flag - 32
            result = upper - 64
            ascii.append(result)
        if flag >= 65 and flag <=90:
            result = flag - 64
            ascii.append(result)

    return " ".join(str(num) for num in ascii)

print(alphabet_position("The sunset sets at twelve o' clock."))