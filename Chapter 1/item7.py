import random as rd

"""
in line if statements
"""

random_int = rd.randint(0,100)

# Note x is not reassigns to Odd, x is "assigned" dependeing on the if statement
x = "Even" if random_int % 2 == 0 else "Odd"

print(f"{random_int} is {x}")