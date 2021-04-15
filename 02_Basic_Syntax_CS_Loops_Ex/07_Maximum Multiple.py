divisor = int(input())
bound = int(input())

for i in range(bound, -1, -1):
    if i % divisor == 0 and bound >= i > 0:
        print(i)
        break
