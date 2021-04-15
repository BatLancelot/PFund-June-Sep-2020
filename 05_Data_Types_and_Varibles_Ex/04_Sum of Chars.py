num_of_lines = int(input())

total_sum = 0
ascii_code = 0

for i in range(num_of_lines):
    letter = input()
    ascii_code = ord(letter)
    total_sum += ascii_code

print(f'The sum equals: {total_sum}')
