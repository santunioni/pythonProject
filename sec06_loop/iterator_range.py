"""
Ranges

Ranges are used to cast numerical sequences
"""


start_value, stop_value = 5, 12


# Use 1
range_1 = range(stop_value)
# stop_value non-included


# Use 2
range_2 = range(start_value, stop_value)


# Comparing
print(range(stop_value) == range(0, stop_value))


# Use 3
step_value = 2
range_3 = range(start_value, stop_value, step_value)
