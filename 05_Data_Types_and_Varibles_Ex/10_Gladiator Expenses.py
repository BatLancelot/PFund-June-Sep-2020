lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
helmet = 0
sword = 0
shield = 0
armor = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:  # Every second lost game, his helmet is broken.
        expenses += helmet_price
        helmet += 1
    if fight % 3 == 0:  # Every third lost game, his sword is broken.
        expenses += sword_price
        sword += 1
    if fight % 3 == 0 and fight % 2 == 0:  # When both his sword and helmet are broken in the same lost fight, his shield also brakes.
        expenses += shield_price
        shield += 1
    if fight % 12 == 0:  # Every second time, when his shield brakes, his armor also needs to be repaired.
        expenses += armor_price
        armor += 1

expenses_2 = (helmet * helmet_price) + (sword * sword_price) + (shield * shield_price) + (armor * armor_price)

print(f'Gladiator expenses: {expenses:.2f} aureus')
# print(f'Gladiator expenses: {expenses_2:.2f} aureus')
