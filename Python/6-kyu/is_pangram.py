"""
Chalange Description :
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

# My Solution :

def is_pangram(st):
    com = [i for i in range(97,123)]
    stag = []
    for i in st :
        a = i.lower()
        ascii = ord(a)

        if 97 <= ascii <= 122:
            if ascii in stag :
                continue
            else :
                stag.append(ascii)
                
    if com == stag :
        return True
    else :
        return False

print( is_pangram("The quick brown fox jumps over the lazy dog."))