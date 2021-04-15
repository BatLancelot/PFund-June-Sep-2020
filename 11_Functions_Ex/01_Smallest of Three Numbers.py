first_num = int(input())
second_num = int(input())
third_num = int(input())


def smallest_of_three(a, b, c):
    return min(a, b, c)


# def smallest_of_three(a, b, c):
#     if second_num > first_num < third_num:
#         print(first_num)
#     if first_num > second_num < third_num:
#         print(second_num)
#     if second_num > third_num < first_num:
#         print(third_num)
#
#
# smallest_of_three(first_num, second_num, third_num)

print((smallest_of_three(first_num, second_num, third_num)))
