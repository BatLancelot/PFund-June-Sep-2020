import sys

num_of_snowballs = int(input())
max_snowball_value = -sys.maxsize
highest_snowballValue = []

for ball in range(num_of_snowballs):

    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())

    snowballValue = (snowballSnow // snowballTime) ** snowballQuality

    if snowballValue > max_snowball_value:
        max_snowball_value = snowballValue
        highest_snowballValue.clear()
        highest_snowballValue.append(snowballSnow)
        highest_snowballValue.append(snowballTime)
        highest_snowballValue.append(snowballQuality)
        highest_snowballValue.append(snowballValue)

print(f'{highest_snowballValue[0]} : {highest_snowballValue[1]} = {highest_snowballValue[3]} ({highest_snowballValue[2]})')
