"""
New functionalities were added to python 3.8 regarded mathematics and statistics

import math

 - math.prod(): returns the product of a numeric container.
 - math.sqrt(): returns the INTEGER PART of a number square root.
 - math.dist(): returns the Euclidean distance between two points, 2D or 3D. Don't work properly with Sets, obviously \
 for who knows geometry.
 - math.hypot(): returns the hypotenuse of a triangle, given two sides.

import statistics

 - statistics.fmean(): returns the float mean of a numerical container
 - statistics.geometric_mean(): returns the geometric float mean of a numericao container
 - statistics.multimode(): returns the most frequently occurring values of a container.
"""

import math
import statistics

first_vector, second_vector = [0, 12, 1], (54, 0, 0)

print(f"New MATH functions: \n")
print(f"{math.prod(first_vector) = }; \n{math.prod(second_vector) = } \n")
print(f"{math.sqrt(2) = }; \n{math.isqrt(2) = } \n")
print(f"{math.dist(first_vector, second_vector) = }; \n{math.dist(first_vector, second_vector) = } \n")
print(f"{math.hypot(3, 4) = }; \n")

print(f"New STATISTICS functions: \n")
print(f"{statistics.fmean((*first_vector, *second_vector)) = }")  # this is the float mean
print(f"{statistics.geometric_mean((*first_vector, *second_vector)) = }")  # compute the geometric mean of real numbers
print(f"{statistics.multimode((*first_vector, *second_vector)) = }")  # a list of the most frequently occurring values.
