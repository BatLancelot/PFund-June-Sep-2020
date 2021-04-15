animals = input()

herd = animals.split(', ')
sheep_pos = []

for i in reversed(range(len(herd))):
    if herd[i] == 'wolf':
        if herd[i] == herd[-1]:
            print('Please go away and stop eating my sheep')
            break
        else:
            print(f'Oi! Sheep number {abs(i - (len(herd) - 1))}! You are about to be eaten by a wolf!')
            break

#  Wrong example:

# for i in range(len(herd)):
#     if herd[i] == 'wolf':
#         if herd[i] == herd[-1]:
#             print('Please go away and stop eating my sheep')
#             break
#         else:
#             print(f'Oi! Sheep number {(i + (len(herd) - 1))}! You are about to be eaten by a wolf!')
#             break
