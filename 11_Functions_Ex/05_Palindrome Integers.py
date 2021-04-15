string_of_numbers = input().split(', ')


def palindrome(number):
    reversed_string = ''.join(reversed(number))
    if number == reversed_string:
        return True
    else:
        return False


for number in string_of_numbers:
    print(palindrome(number))
