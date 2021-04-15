import sys

numbers_string = input().split(' ')
n = int(input())

min_number = sys.maxsize

numbers_int = []

for number in numbers_string:
    digit = int(number)
    numbers_int.append(digit)

for _ in range(n):
    for number in numbers_int:
        if number < min_number:
            min_number = number
    numbers_int.remove(min_number)
    min_number = sys.maxsize

print(numbers_int)
