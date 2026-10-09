"""
You are provided with a list (or array) of integer pairs. 
Elements of each pair represent the number of people that get on the bus (the first item) 
and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). 
Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, 
they are probably sleeping there :D
"""

# My Solution :

def number(bus_stops):
    total = 0 
    for i in bus_stops:
        total += i[0] - i[1]
    return total