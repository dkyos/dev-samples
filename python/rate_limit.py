#!/usr/bin/env python 

"""global variables for the API URL and rate limiting."""

import functools
from typing import Callable, Dict, Any, Union, Deque
import time
import threading
from collections import deque
import logging
import inspect

logger = logging.getLogger(__name__)


def rate_limited(func: Callable, max_calls: int, period: int) -> Callable:
    """Limit the number of times a function can be called."""
    calls: Deque = deque()

    # Add thread safety
    lock = threading.RLock()

    @functools.wraps(func)
    def wrapper(*args, **kargs):
        """Wrap function."""
        with lock:
            #print(type(calls))
            if len(calls) >= max_calls:
                until = time.time() + period - (calls[-1] - calls[0])
                sleeptime = until - time.time()
                if sleeptime > 0:
                    logger.info(
                        f"Rate Limit Reached. (Sleeping for {round(sleeptime)} seconds)"
                    )
                    print("Rate Limit Reached => sleep with : " + str(sleeptime))
                    time.sleep(sleeptime)
                while len(calls) > 0:
                    calls.popleft()
            _time = time.time()
            calls.append(_time)
            print("call append : " + str(len(calls)) + " with : " + str(_time))

            # Pop the timestamp list front (ie: the older calls) until the sum goes
            # back below the period. This is our 'sliding period' window.
            while (calls[-1] - calls[0]) >= period:
                print("call popleft: " + str(len(calls)))
                calls.popleft()
        
        return func(*args, **kargs)

    return wrapper

class Test:
    def __init__(self) -> None:
        for name, fn in inspect.getmembers(self, inspect.ismethod):
            print(name)
            setattr(
                self, name, rate_limited(fn, 10, 3)
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
