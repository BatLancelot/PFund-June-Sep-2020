num_of_lines = int(input())

tank_capacity = 255
total_water = 0

for i in range(num_of_lines):
    quantity_of_water = int(input())

    if tank_capacity > 0 and total_water + quantity_of_water <= 255:
        total_water += quantity_of_water
    else:
        print('Insufficient capacity!')

print(total_water)
