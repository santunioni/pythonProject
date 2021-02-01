import time
from threading import Thread

counter = 50000000


def regressive_counting(n):
    while n > 0:
        n -= 1


# Multi-Thread example:
thread_1 = Thread(target=regressive_counting, args=(counter//2, ))
thread_2 = Thread(target=regressive_counting, args=(counter//2, ))
initial_time = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
how_much_time = time.time() - initial_time
print(f'Time in second: {how_much_time}')

# The difference between multi-thread and single thread is not large in python.
# Because Python Global Interpreter Lock, both threads run as they were one.
