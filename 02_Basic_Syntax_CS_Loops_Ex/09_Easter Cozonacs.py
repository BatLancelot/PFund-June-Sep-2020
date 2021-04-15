budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25

cozunac_price = price_flour + price_eggs + (price_milk / 4)
colored_eggs = 0
cozonacsCount = 0

while budget >= cozunac_price:
    budget -= cozunac_price
    cozonacsCount += 1
    colored_eggs += 3
    if cozonacsCount % 3 == 0:
        colored_eggs -= (cozonacsCount - 2)

print(f'You made {cozonacsCount} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
