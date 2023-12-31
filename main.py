import functools
import timeit


def cache_decorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


@cache_decorator
def fibonacci(n):
    fib_values = [0, 1]
    if n <= 1:
        return fib_values[n]
    else:
        for i in range(2, n + 1):
            fib_values.append(fib_values[i - 1] + fib_values[i - 2])
        return fib_values[n]


def f(n):
    fib_values = [0, 1]
    if n <= 1:
        return fib_values[n]
    else:
        for i in range(2, n + 1):
            fib_values.append(fib_values[i - 1] + fib_values[i - 2])
        return fib_values[n]


if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))

    # With cache decorator
    duration = timeit.timeit(lambda: fibonacci(30), number=1)
    print("With cache decorator:", duration, "s")
    # Without cache decorator
    d = timeit.timeit(lambda: f(30), number=1)
    print("Without cache decorator:", d, "s")
