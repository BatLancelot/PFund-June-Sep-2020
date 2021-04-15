numbers_string = input().split(', ')
beggars = int(input())

numbers_int = []
beggars_num = []

for _ in numbers_string:
    numbers_int.append(int(_))

for _ in range(beggars):
    beggars_num.append(0)

index_counter = 0

for number in numbers_int:
    beggars_num[index_counter] += number
    index_counter += 1
    if index_counter == beggars:
        index_counter = 0

print(beggars_num)
