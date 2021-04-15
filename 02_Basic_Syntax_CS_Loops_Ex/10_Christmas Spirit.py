quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

christmas_spirit = 0
budget = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        christmas_spirit += 5
        budget += ornament_set * quantity
    if i % 3 == 0:
        christmas_spirit += 13
        budget += (tree_skirt + tree_garlands) * quantity
    if i % 5 == 0:
        christmas_spirit += 17
        budget += tree_lights * quantity
    if i % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights
    if i % 15 == 0:
        christmas_spirit += 30

if days % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')
