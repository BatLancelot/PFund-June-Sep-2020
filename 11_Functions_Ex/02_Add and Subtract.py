first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(d, c):
    return d - c


def add_and_subtract(a, b, c):
    return subtract((sum_numbers(a, b)), c)


print(add_and_subtract(first_num, second_num, third_num))
