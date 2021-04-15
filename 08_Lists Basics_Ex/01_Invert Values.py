text = input()
separated_nums = text.split()
opposite_nums = []

for num in separated_nums:
    convert_num = -int(num)
    opposite_nums.append(convert_num)

print(opposite_nums)
