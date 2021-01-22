"""
Maps

Com map, fazemos mapeamento de valores para função.
"""

import math


def area(_radius):
    """Compute the circle area from the radius 'r'."""
    return math.pi * (_radius**2)


radius = [1, 2, 41, 5, 12, 76, 45, 7]

# Standard way to compute the areas
areas = []
for r in radius:
    areas.append(area(r))
print(areas)


# Using map to compute
areas = map(area, radius)  # return an map object
# OBS: after using list(areas) the map areas vanish
print("\nLook at the map:")
print(areas)
print(list(areas))
print(list(areas))
# It is interesting because cleans the computer memory
print("The map has gone.\n")


# Using lambda and map to compute
areas = map(lambda _r: math.pi*(_r**2), radius)
print(list(areas))
print(areas)


# Another example
cities = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
          ('Los angeles', 26), ('Tokio', 27), ('Nova Iorque', 28), ('Londres', 22)]
# I want to print temperatures in Fahrenheit
print(cities)
print(list(map(lambda data: (data[0], round(9/5*data[1]+32, 2)), cities)))


# functions to map must always receive ONE PARAMETER ONLY

