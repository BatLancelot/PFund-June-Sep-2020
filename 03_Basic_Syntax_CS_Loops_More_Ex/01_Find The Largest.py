number = input()

number_list = ([int(number[i]) for i in range(len(number))])
number_list.sort(reverse=True)
largest_num = ''.join([str(i) for i in number_list])

print(largest_num)

# largest_num = 0
# number_list = []

# for i in range(len(number)):
#     number_list.append(int(number[i]))
# number_list.sort(reverse=True)
# for i in number_list:
#     largest_num += ''.join(str(i))
