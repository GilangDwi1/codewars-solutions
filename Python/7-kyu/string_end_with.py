"""
Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument (also a string).

Examples:

Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false
"""

# My Solution :

def solution(str, ending):
    return str.endswith(ending)

print(solution("samurai", "ai"))