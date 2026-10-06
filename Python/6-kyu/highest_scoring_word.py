"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
# My Solution :

def high(x):
    split = x.split()
    highest = []
    for i in split :
        flag = []
        for c in i :
            flag.append(ord(c) - 96)
        total = sum(flag)
        highest.append(total)

    idx = highest.index(max(highest))

    if len(split) < 3 :
        return split[0]
    else :
        return split[idx]
        
print(high('what time are we climbing up the volcano'))
