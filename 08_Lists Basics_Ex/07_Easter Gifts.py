gifts = input().split(' ')
command = ['', '']
final_gift_list = []

while command[0] != 'Money' and command[1] != 'Money':
    command = input().split(' ')
    item = command[1]
    index = 0
    if len(command) == 3:
        index = int(command[2])

    if 'OutOfStock' in command:
        for i in range(len(gifts)):
            if item == gifts[i]:
                gifts.remove(gifts[i])
                gifts.insert(i, 'None')

    if 'Required' in command:
        if len(gifts) < index or index < 0:
            continue
        elif len(gifts) == index:
            gifts.pop(index - 1)
            gifts.insert(index, item)
        else:
            gifts.pop(index)
            gifts.insert(index, item)

    if 'JustInCase' in command:
        gifts.pop(-1)
        gifts.append(item)

for gift in gifts:
    if gift == 'None':
        continue
    final_gift_list.append(gift)

print(' '.join(final_gift_list))
