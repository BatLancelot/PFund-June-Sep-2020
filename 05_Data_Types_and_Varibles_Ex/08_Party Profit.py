import math

party_size = int(input())
days = int(input())

sum_coins = 0
day_earning = 50
food_price = 2
water_price = 3
boss_master = 20

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2  # 2 (two) of your companions leave
    if day % 15 == 0:
        party_size += 5  # 5 (five) new companions are joined

    sum_coins += day_earning   # you are earning 50 coins, spent 2 coin per companion for food.
    sum_coins -= food_price * party_size

    if day % 3 == 0:
        sum_coins -= water_price * party_size  # spending 3 coins per companion for drinking water
    if day % 5 == 0:
        sum_coins += boss_master * party_size  # boss monster and you gain 20 coins per companion.
        if day % 3 == 0:
            sum_coins -= food_price * party_size  # spent additional 2 coins per companion.

coins_per_person = math.floor(sum_coins / party_size)  # how much coins gets each companion

print(f"{party_size} companions received {coins_per_person} coins each.")
