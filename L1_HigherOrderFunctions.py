# Higher order functions, which accept another functions as arguments

# def product(n, func):
#     result = 1
#
#     for number in range(1, n):
#         result *= func(number)
#
#     return result
#
#
# def square(x):
#     return x*x
#
#
# def cube(x):
#     return x*x*x
#
#
# print(product(4, square))
# # 1 2 3
# # squares: 1*4*9 = 36
#
# print(product(4, cube))
# # 1 2 3
# # cubes: 1*8*27 = 216

# def my_function(a, b, func):
#     result = func([a, b])
#     return result
#
#
# print(my_function(2, 3, sum))


# Using nested functions

from random import choice


# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#
#     result = get_color() + ' ' + thing
#     return result
#
#
# print(colorize('apple'))


# Higher order functions, which return another functions

# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#
#     return get_color
#
#
# first_color = make_color()
# print(first_color())
#
# second_color = make_color()
# print(second_color())
#
# third_color = make_color()
# print(third_color())


# Inner functions can access outer functions scope

def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color


# print(colorize('apple')())

colorized_dog = colorize('dog')
print(colorized_dog())