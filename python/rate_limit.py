#!/usr/bin/env python 

import functools
from typing import Callable, Deque
import time
import threading
from collections import deque
import inspect

MAX_CALLS = 10
PERIOD_SEC = 3

def rate_limited(func: Callable, max_calls: int, period: int) -> Callable:
    print("Max calls : " + str(max_calls) + " / " + str(period))
    calls: Deque = deque()

    lock = threading.RLock()

    @functools.wraps(func)
    def wrapper(*args, **kargs):
        with lock:
            if len(calls) >= max_calls:
                until = time.time() + period - (calls[-1] - calls[0])
                sleeptime = until - time.time()
                if sleeptime > 0:
                    print("Rate Limit Reached => sleep with : " + str(sleeptime))
                    time.sleep(sleeptime)
                while len(calls) > 0:
                    calls.popleft()
            _time = time.time()
            calls.append(_time)
            
            # Pop the timestamp list front (ie: the older calls) until the sum goes
            # back below the period. This is our 'sliding period' window.
            while (calls[-1] - calls[0]) >= period:
                calls.popleft()
        
        return func(*args, **kargs)

    return wrapper

class Test:
    def __init__(self) -> None:
        for name, fn in inspect.getmembers(self, inspect.ismethod):
            setattr(
                self, name, rate_limited(fn, MAX_CALLS, PERIOD_SEC)
            )

    def function_test(self, num):
        print("function_test called: " + str(num))
        return


if __name__ == "__main__":
    t = Test()
    num = 0
    while True:
        t.function_test(num)
        num += 1
