num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

# MOST Python's VERSION
print(max(num_1, num_2, num_3))
print(min(num_1, num_2, num_3))

# Pythonic Version
if num_2 < num_1 > num_3:
    print(num_1)
elif num_3 < num_2 > num_1:
    print(num_2)
else:
    print(num_3)

# MY VERSION
if num_1 > num_2 and num_1 > num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
else:
    print(num_3)
