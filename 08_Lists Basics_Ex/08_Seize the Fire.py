fire_cells = input().split('#')
water = int(input())
effort = 0.0
total_fire = 0

print('Cells:')


def fire_calculation(w, t, e):
    w -= value
    t += value
    e += (value / 100) * 25
    return water, total_fire, effort


for _ in fire_cells:
    cell, value = _.split(' = ')
    value = int(value)
    if water >= value:
        if cell == 'High' and 81 <= value <= 125:
            fire_calculation(water, total_fire, effort)
            # water -= value
            # total_fire += value
            # effort += (value / 100) * 25
        elif cell == 'Medium' and 51 <= value <= 80:
            fire_calculation(water, total_fire, effort)
            # water -= value
            # total_fire += value
            # effort += (value / 100) * 25
        elif cell == 'Low' and 0 < value <= 50:
            fire_calculation(water, total_fire, effort)
            # water -= value
            # total_fire += value
            # effort += (value / 100) * 25
        else:
            continue

        print(f' - {value}')

    else:
        continue
print(f'Effort: {effort:.2f}\nTotal Fire: {total_fire}')
