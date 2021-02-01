import time
from threading import Thread

counter = 50000000


def regressive_counting(n):
    while n > 0:
        n -= 1


# Single-Thread example:
initial_time = time.time()
regressive_counting(counter)
how_much_time = time.time() - initial_time
print(f'Time in second: {how_much_time}')
