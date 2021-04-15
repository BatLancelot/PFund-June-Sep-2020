number = int(input())

sign = '*'

for i in range(number + 1):
    for j in range(0, i):
        print(sign, end='')
    print()

for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print(sign, end='')
    print()
