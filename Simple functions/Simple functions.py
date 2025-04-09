# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 04:30:45 2025

@author: SEA4720
"""
#Function right triangle
# Function to check if three sides form a right triangle
def is_right_triangle(a, b, c):
    # First, sort the numbers so the largest (hypotenuse) comes last
    sides = sorted([a, b, c])
    
    # Apply the Pythagorean theorem: a² + b² = c²
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Sample test cases

print(f'is_right_triangle(3,4,5) is {is_right_triangle(3, 4, 5)}')   # True
print(f'is_right_triangle(5,4,6) is {is_right_triangle(5, 4, 6)}')  # True
print(f'is_right_triangle(1,1,1) is {is_right_triangle(1, 1, 1)}')   # False

#Median
# Function to compute the median of a list or tuple
def median(data):
    # Convert input to a list and sort it
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # If the number of elements is odd, return the middle one
    if n % 2 != 0:
        return sorted_data[n // 2]
    else:
        # If even, return average of the two middle values
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2

# Sample test cases 
print(median([6, 1, 3, 7, 8, 3, 9]))        # 6
print(median([6, 1, 3, 4, 5, 8, 9, 2]))     # 4.5

# Variable length arguments
# Define a function that accepts a variable number of numerical arguments
def max2(*args):
    # Check if any arguments are provided
    if len(args) == 0:
        return None  # Return None if no arguments passed
    
    # Initialize maximum with the first value
    maximum = args[0]
    
    # Iterate over the rest of the arguments
    for num in args[1:]:
        if num > maximum:
            maximum = num
    
    return maximum

# Sample test cases
print(max2(1, 4, 7))                     # Output: 7
print(max2(89, 4))                      # Output: 89
print(max2(4, 5, 76, 3, 7, 1, 435253))  # Output: 435253
