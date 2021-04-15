bar_length = int(input())
numbers = []


def loading_bar_display(length):
    sign = '%'
    dots = '.'
    if length == 100:
        print(f'{length}% Complete!')
        print('[%%%%%%%%%%]')
    elif length > 0:
        for i in range(1, length + 1):
            if i % 10 == 0:
                numbers.append(i)
        print(f'{length}% [{sign * len(numbers)}{dots * (10 - len(numbers))}]')
        print('Still loading...')


loading_bar_display(bar_length)
