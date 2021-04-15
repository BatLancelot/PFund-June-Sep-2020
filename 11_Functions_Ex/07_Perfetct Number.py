number = int(input())
proper_positive_divisors = []


def perfect_number_checker(n):
    for num in range(1, n):
        if number % num == 0:
            proper_positive_divisors.append(num)
    if sum(proper_positive_divisors) == n:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


perfect_number_checker(number)
