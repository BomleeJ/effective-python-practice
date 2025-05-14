"""
Learned about representations of Object

This script demonstrates how to define a custom __repr__ method in Python to control 
how an object is represented as a string, which is especially useful for debugging 
and development. The example involves creating a simple class representing a color 
using RGB values.
"""

class TestObject:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        # Returns a developer-friendly string representation of the object.
        # This is used by repr(), f"{obj!r}", and the interactive console.
        return f"Color Red: {self.red} Green: {self.green} Blue: {self.blue}"

# Create an instance of TestObject representing a specific color.
color = TestObject(255, 207, 0)

# Print using __str__ if defined, otherwise __repr__ (here it falls back to __repr__).
print(color)

# Explicitly print using __repr__ via f-string.
print(f"{color!r}")

# Directly call repr() to get the representation of the object.
print(repr(color))