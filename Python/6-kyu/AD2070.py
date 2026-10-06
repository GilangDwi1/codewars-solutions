"""
Chalange Description :
Your task is to search through a string of integers related to BOT system internals found during a recent scan of communication systems searching for a pattern.

100 ≤ log ≤ 100000
1 ≤ n ≤ 10000
  
Integer is Prime

Integer is 4 digits long such as 1031

Integer third digit is either 2 or 3 such as 1021 or 1031
                                               ^       ^
                                               |       |
The count of the integer in the log is > 3

If there are > 50 integers in the log matching this pattern the BOT at this location should be disabled

Here is an example

All the integers below are prime:

log= ['8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723', 
      '8923', '5639', '2423', '3929', '7723', 
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723', 
      '8923', '5639', '2423', '3929', '7723', 
      '8923', '5639', '2423', '3929', '7723', 
      '8923', '5639', '2423', '3929', '7723',
      '8923']

Here is the Count

({'2423': 10, '3929': 10, '5639': 10, '7723': 10, '8923': 11})

Count = 51
Count > 50

Return "match disable bot"
   
If these rules do not hold 
  
Return "no match continue"
"""

# My Solution :

def search_disable(log):
    bot = log.split()
    integers = {}
    counts = 0
    ## count each integers
    for i in bot :
        if integers.get(i) == None :
            integers[i] = 1
        else :
            integers[i] += 1
    
    for x, y in integers.items():
        a = int(x)
        isprime = True

        if len(x) != 4 :
            continue

        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                isprime = False
        if isprime == False :
            continue
        if x[2] != "2" or x[2] == "3" :
            continue
        if y <= 3 :
            continue
        counts += y

    if counts <= 50 :
        return 'no match continue'
    else :
        return 'match disable bot'