from functools import wraps


# def check_if_first_args_is(value):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return inner_dec
#
#
# @check_if_first_args_is('red')
# def print_reinbow_colors(*colors):
#     print(colors)
#
#
# print_reinbow_colors('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
#
#
# @check_if_first_args_is(7)
# def multiply_7(a, b):
#     return a * b
#
#
# print(multiply_7(7, 3))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wraperr(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)

        return wraperr

    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', '3')


# *args - ('Hi!', '3')
# *types - (str, int)
# zip(args, types) - ('Hi!', str) ('3', int)

@enforce(float, float)
def divide(a, b):
    return a / b


print(divide('4', '2'))
