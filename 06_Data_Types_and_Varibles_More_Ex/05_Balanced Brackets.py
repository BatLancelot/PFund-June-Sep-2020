number_of_lines = int(input())

opening_bracket = 0
closing_bracket = 0

for _ in range(number_of_lines):
    random_string = input()
    if closing_bracket > opening_bracket or opening_bracket - closing_bracket == 2:
        print('UNBALANCED')
        break
    if random_string == '(':
        opening_bracket += 1
    elif random_string == ')':
        closing_bracket += 1

if opening_bracket == closing_bracket:
    print('BALANCED')
