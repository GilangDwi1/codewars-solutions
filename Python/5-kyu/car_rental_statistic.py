"""
A chain of car rental locals made a statistical research for each local in a city. They measure the average of clients for every day.

They used the Simpson model for probabilities:

where:

λ: average for the amount of events having the same conditions during the measurement,
x: number of the events different from the average at the same place and time interval for obtaining the average.
The number e is 2.7182818284....

Suposse that one of the locals has an average 8 clients per day.

t is a very low value, almost 5%. It shows that they have to work a lot for this increment.

And, how would it be if we want to know the sum of probabilities for values below 12 (cumulative probability)?

P(c < 12) = P(c=0) + P(c=1) + P(c=3) + P(c=4) + P(c=5) + P(c=6) + P(c=7) + P(c=8) + P(c=9) +  P(c=10) + P(c=11) 

P(c<12) = 0.00033546262790251196 + 0.0026837010232200957 + 0.010734804092880383 + 0.02862614424768102 + 0.05725228849536204 + 0.09160366159257927 + 0.12213821545677235 + 0.13958653195059698 + 0.13958653195059698 + 0.12407691728941954 + 0.09926153383153563 + 0.072190206422935 = 0.888075998981
But the probability of having below or equal the value 12, will be:

P(c≤12) = P(c=0) + P(c=1) + P(c=3) + P(c=4) + P(c=5) + P(c=6) + P(c=7) + P(c=8) + P(c=9) +  P(c=10) + P(c=11) + P(c=12) = 0.936202803263
(P(c≤12) = P(12≥c))
The probability for having equal or more clients than 12 will be:

P(c>12) = P(c=13) + P(c=14) + P(c=15) + ........+ P(c=+∞) 
(P(c>12) = P(12<c))
But the sum of the probabilities for c = 0 to +∞ is 1

So,

P(c>12) = 1 - P(c≤12) = 1 - 0.936202803263 = 0.063797196737
Make the function prob_simpson(), that will receive 2 or 3 arguments.

Two arguments if we want to calculate the probability for a specific number, receives the average lamb and the variable x.

Three arguments if we want the cumulative probability for a value, besides receiving lamb and x, will receive one of the following operators in string format: <, <=, >, >=.

Let's see some cases for probability at the number:

prob_simpson(8, 12) == 0.04812680428195667
prob_simpson(8, 11) == 0.072190206422935
prob_simpson(8, 10) == 0.09926153383153563
And for cumulative probability:

prob_simpson(8, 12, '>') == 0.888075998981    # or P(12>c)
prob_simpson(8, 12, '>=') ==  0.936202803263  # or P(12≥c)
prob_simpson(8, 12, '<') == 0.063797196737    # or P(12<c)
prob_simpson(8, 12, '<=') == 0.111924001019   # or P(12≤c)
You may assume that you will not receive high values for lamb and x This kata will also have translations into Javascript and Ruby.

Enjoy it!
"""

"""
Note:

This function implements the Poisson distribution, not a "Simpson model".

The function name prob_simpson is retained to match the original kata's

required function signature.



Mathematical definition:

P(X = x) = (lambda ** x * exp(-lambda)) / factorial(x)



Standard probability operator meanings:

'<'  -> P(X < x)

'<=' -> P(X <= x)

'>'  -> P(X > x)

'>=' -> P(X >= x)



Important:

The kata's examples/expected results may use reversed operator mappings

compared with standard mathematical notation. Verify the expected test

cases before changing the operator logic.
"""

# My Solution :

import math

def prob_simpson(lamb, x, op='='):
    factorial = 1

    if op == "=" :
        for i in range(1, x + 1) :
            factorial *= i

        prob = lamb**x * math.exp(-lamb) / factorial

        return prob
    else :
        total = 0
        factorial_i = 1

        if op == "<" or op == ">=":
            bound = x + 1
        elif op == "<=" or op == ">":
            bound = x
        for i in range(bound) :
            if i > 0 :
                factorial_i *= i
            total += (lamb**i) * math.exp(-lamb) / factorial_i

        if op == "<=" or op == "<":
            return 1 - total
            
        elif op == ">=" or op == ">":
            return total
        
print(prob_simpson(8, 12))
