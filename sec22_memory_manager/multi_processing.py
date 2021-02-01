from multiprocessing import Pool
import time

counter = 50000000


def regressive_counting(n):
    while n > 0:
        n -= 1


# Multi-processing example:
if __name__ == '__main__':
    pool = Pool(processes=8)
    initial_time = time.time()
    r1 = pool.apply_async(regressive_counting, counter//2)
    r2 = pool.apply_async(regressive_counting, counter//2)
    pool.close()
    pool.join()
    how_much_time = time.time() - initial_time
    print(f'Time in second: {how_much_time}')


# Multiprocessing increase python performance largely. However they are heavier than multithreading
# Therefore python illness with multithreading makes it a not good language for performance
