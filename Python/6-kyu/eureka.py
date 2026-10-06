"""
e need a function to collect these numbers, that may receive two integers a, b that defines the range
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a,b] the function should output an empty list.

90, 100 --> []
"""

# My Soluion :

def sum_dig_pow(a, b): 
    d = []
    for i in range (a , b + 1) :
        a = []
        flag = list(str(i))
        result = i
        for index, number in enumerate(flag, start=1):
            
            if len(flag) > 1 :
                a.append(int(number) ** int(index))
                
                print(total)
                

            else :
                d.append(i)
        total = sum(a)
        if total == int(result) :
            d.append(i)
        else :
            continue
    return d


        
print(sum_dig_pow(1, 135))

