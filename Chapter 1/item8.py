"""
Walrus Operator (:=) Example

Demonstrates how to use the walrus operator for inline assignment in conditions.
This operator allows you to assign a value to a variable as part of an expression, 
which can help reduce redundancy and improve readability in certain cases.
"""

# This function returns True. We will use it in a conditional check.
def foo():
    return True

# Using the walrus operator to assign and evaluate 'condition' in one line
if condition := foo():
    print("Condition is True")

# As opposed to the traditional approach:
condition = foo()
if condition:
    print("Condition is True")