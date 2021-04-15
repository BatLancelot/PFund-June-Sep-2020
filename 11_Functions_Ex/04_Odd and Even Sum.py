number_s: str = input()
even = []
odd = []


def sum_even_odd(number: str):
    for num in number:
        if int(num) % 2 == 0:
            even.append(int(num))
        else:
            odd.append(int(num))


sum_even_odd(number_s)
print(f'Odd sum = {sum(odd)}, Even sum = {sum(even)}')
