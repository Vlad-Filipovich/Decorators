from time import time
from functools import wraps


def speed_test(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time() - start_time
        print(f'{function.__name__.capitalize()} function code execution time: {end_time}')
        return result

    return wrapper


@speed_test
def list_square_sum(length):
    result = sum([number for number in range(length)])
    return result


@speed_test
def gen_square_sum(length):
    result = sum(number for number in range(length))
    return result


@speed_test
def product():
    result = 1
    for number in range(1, 100_000_000):
        result += number

    return result


print(list_square_sum(10_000_000))
print(gen_square_sum(10_000_000))
print(product())