"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

# My Solution :

def get_count(sentence):
        vowels = ["a","i","u","e","o"]
        count = 0
        for i in sentence:
            if i in vowels:
                count += 1
        return count

print(get_count("abracadabra"))