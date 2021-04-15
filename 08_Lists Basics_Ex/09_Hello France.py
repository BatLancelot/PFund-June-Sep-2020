collection_of_items = input().split('|')
budget = int(input())
sell_price = 0.0
profit = 0
income = 0
items_bought = 0

for _ in collection_of_items:
    item, value = _.split('->')
    value = float(value)
    if budget >= value:
        if item == 'Clothes' and value <= 50:
            budget -= value
            items_bought += value
            sell_price = value * 1.4
            profit += sell_price - value
        elif item == 'Shoes' and value <= 35:
            budget -= value
            items_bought += value
            sell_price = value * 1.4
            profit += sell_price - value
        elif item == 'Accessories' and 0 < value <= 20.50:
            budget -= value
            items_bought += value
            sell_price = value * 1.4
            profit += sell_price - value

        else:
            continue
        income += sell_price
        print(f'{sell_price:.2f}', end=' ')

    else:
        continue
income += budget
print()
print(f'Profit: {profit:.2f}')
if income >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
