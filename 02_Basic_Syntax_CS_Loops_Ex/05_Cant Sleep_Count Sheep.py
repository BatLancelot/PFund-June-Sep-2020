number = int(input())
total_count = ''

# total_count += ''.join([f'{str(i)} sheep...' for i in range(1, number + 1)])
# print(total_count)

for i in range(1, number + 1):
    total_count += f'{str(i)} sheep...'
print(total_count)
