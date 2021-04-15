number_a = int(input())
number_b = int(input())


def factorial(a, b):
    for i in range(a, 1, -1):
        a *= i - 1
    for i in range(b, 1, -1):
        b *= i - 1
    result = a / b
    return result


print(f'{factorial(number_a, number_b):.2f}')
