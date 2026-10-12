"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
"""

# My Solution :

def count_smileys(arr):
    eyes = ":;"
    nose = "-~"
    mouth = ")D"

    total = 0
    for i in arr :
        if i[0] in eyes:
            if len(i) == 3 :
                if i[1] in nose and i[2] in mouth :
                    total += 1
            elif len(i) == 2 :
                if i[1] in mouth :
                    total += 1

    return total 
print(count_smileys([':D',':~)',';~D',':)']))