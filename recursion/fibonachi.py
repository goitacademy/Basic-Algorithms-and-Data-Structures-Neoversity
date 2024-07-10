import time
from functools import lru_cache

# https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence
# F(6)                 *  <-- only once
# F(5)                 *  <-- only once too
# F(4)                 **
# F(3)                ****
# F(2)              ********
# F(1)          ****************           <-- 16
# F(0)  ********************************    <-- 32
# Now, in terms of complexity:
# O( F(6) ) = O(2^6)
# O( F(n) ) = O(2^n)

def fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    first, second = 0, 1

    for i in range(n):
        first, second = second, first + second
    return first


def fibonacci_recursive(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@lru_cache
def fibonacci_lru(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


# Manual caching using a dictionary.
def fibonacci_cache(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    result = fibonacci_cache(n - 1, cache) + fibonacci_cache(n - 2, cache)
    cache[n] = result
    return result


n = 40

start = time.perf_counter()
fibonacci(n)
end = time.perf_counter()
print("Plain version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fibonacci_recursive(n)
end = time.perf_counter()
print("Plain recursive version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fibonacci_lru(n)
end = time.perf_counter()
print("lru cache version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fibonacci_cache(n)
end = time.perf_counter()
print("Manual cache version. Seconds taken: {:.7f}".format(end - start))