"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

# My Solution :

def solution(s):
    result = []
    a = ""
    for i in s :
        count = 0
        count += 1
        if i.isupper() == True :
            result.append(" ".join(" "))
            result.append(" ".join(i))
            continue
        else :
            for x in range(count) :
                result.append(" ".join(i))

    return "".join(result)

print(solution("helloWorld"))