start = int(input())
stop = int(input())

letter = []

for i in range(start, stop + 1):
    ascii_code = chr(i)
    letter.append(ascii_code)

print(' '.join(letter))
