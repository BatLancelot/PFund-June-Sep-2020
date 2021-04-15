def basic_calc(operation, a, b):
    if operation == 'multiply':
        return a * b
    if operation == 'divide':
        return a // b
    if operation == 'add':
        return a + b
    if operation == 'subtract':
        return a - b


operator = input()
first_num = int(input())
second_num = int(input())

print(basic_calc(operator, first_num, second_num))
