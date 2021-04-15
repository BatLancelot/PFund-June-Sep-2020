integer_sequence = input().split()
array_of_integers = []
grater_than_average = []
reverse_state = True
for i in integer_sequence:
    array_of_integers.append(int(i))

sequence_average = sum(array_of_integers) / len(array_of_integers)
if sequence_average < 0:
    reverse_state = False

for item in array_of_integers:
    if item > sequence_average:
        grater_than_average.append(str(item))

grater_than_average = sorted(grater_than_average, reverse=reverse_state)

top_5 = grater_than_average[:5]

if len(top_5) == 0:
    print('No')
else:
    print(' '.join(top_5))
