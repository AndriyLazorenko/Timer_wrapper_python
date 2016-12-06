# Timers as wrappers lib. Includes time(), clock() and perf_counter() timers from time lib

import time
from functools import wraps


def timer_time(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        var = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("   Function '{}' ran in {} s. (time) ".format(orig_func.__name__, t2))
        return var

    return wrapper


def timer_clock(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.clock()
        var = orig_func(*args, **kwargs)
        t2 = time.clock() - t1
        print("   Function '{}' ran in {} s. (clock: without CPU 'sleeps')".format(orig_func.__name__, t2))
        return var

    return wrapper


def timer_perf_counter(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        var = orig_func(*args, **kwargs)
        t2 = time.perf_counter() - t1
        print("   Function '{}' ran in {} s. (perf_counter)".format(orig_func.__name__, t2))
        return var

    return wrapper


@timer_time
def demo_timer_time():
    time.sleep(1)


@timer_clock
def demo_timer_clock():
    time.sleep(1)


@timer_perf_counter
def demo_timer_perf_counter():
    time.sleep(1)


@timer_time
@timer_clock
@timer_perf_counter
def demo_all():
    time.sleep(1)


if __name__ == '__main__':
    demo_all()
