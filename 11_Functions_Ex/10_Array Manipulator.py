import sys


def exchange(index_value: int):  # DONE
    temp_array = initial_array
    first_half_sub_array = temp_array[: index_value + 1]
    second_half_sub_array = temp_array[index_value + 1:]
    return second_half_sub_array + first_half_sub_array


def max_even(array):  # DONE
    max_num_even = -sys.maxsize
    max_num_even_index = -1

    for i in range(len(array)):
        number = array[i]
        if number % 2 == 0:
            if number >= max_num_even:
                max_num_even = number
                max_num_even_index = i
    return max_num_even_index


def max_odd(array):  # DONE
    max_num_odd = -sys.maxsize
    max_num_odd_index = -1

    for i in range(len(array)):
        number = array[i]
        if number % 2 != 0:
            if number >= max_num_odd:
                max_num_odd = number
                max_num_odd_index = i
    return max_num_odd_index


def min_even(array):  # DONE
    min_num_even = sys.maxsize
    min_num_even_index = -1

    for i in range(len(array)):
        number = array[i]
        if number % 2 == 0:
            if number <= min_num_even:
                min_num_even = number
                min_num_even_index = i
    return min_num_even_index


def min_odd(array):  # DONE
    min_num_odd = sys.maxsize
    min_num_odd_index = -1

    for i in range(len(array)):
        number = array[i]
        if number % 2 != 0:
            if number <= min_num_odd:
                min_num_odd = number
                min_num_odd_index = i

    return min_num_odd_index


def first_even(count: int):
    temp_array_first_even = []
    number_counter = 0
    for num in initial_array:
        if number_counter == count:
            break
        if num % 2 == 0:
            temp_array_first_even.append(num)
            number_counter += 1
    return temp_array_first_even


def last_even(count: int):
    temp_array_last_even = []
    number_counter = 0
    for i in range(len(initial_array) - 1, -1, -1):
        num = initial_array[i]
        if number_counter == count:
            break
        if num % 2 == 0:
            temp_array_last_even.append(num)
            number_counter += 1
    temp_array_last_even.reverse()
    return temp_array_last_even


def first_odd(count: int):
    temp_array_first_odd = []
    number_counter = 0
    for num in initial_array:
        if number_counter == count:
            break
        if num % 2 != 0:
            temp_array_first_odd.append(num)
            number_counter += 1
    return temp_array_first_odd


def last_odd(count: int):
    temp_array_last_odd = []
    number_counter = 0
    for i in range(len(initial_array) - 1, -1, -1):
        num = initial_array[i]
        if number_counter == count:
            break
        if num % 2 != 0:
            temp_array_last_odd.append(num)
            number_counter += 1
    temp_array_last_odd.reverse()
    return temp_array_last_odd


input_array = input().split()
initial_array = []

for item in input_array:
    initial_array.append(int(item))

manipulation_commands: str = input()

while manipulation_commands != 'end':
    commands = manipulation_commands.split()

    if commands[0] == 'exchange':
        if int(commands[1]) < 0 or int(commands[1]) > len(initial_array):
            print('Invalid index')
        else:
            initial_array = exchange(int(commands[1]))

    elif commands[0] == 'max':
        index = -1
        if commands[1] == 'even':
            index = max_even(initial_array)
        elif commands[1] == 'odd':
            index = max_odd(initial_array)

        if index == -1:
            print('No matches')
        else:
            print(index)

    elif commands[0] == 'min':
        index = -1
        if commands[1] == 'even':
            index = min_even(initial_array)
        elif commands[1] == 'odd':
            index = min_odd(initial_array)

        if index == -1:
            print('No matches')
        else:
            print(index)

    elif commands[0] == 'first':
        first_n_elements = []

        if int(commands[1]) < 0 or int(commands[1]) > len(initial_array):
            print('Invalid count')
        else:
            if commands[2] == 'even':
                first_n_elements = first_even(int(commands[1]))
            elif commands[2] == 'odd':
                first_n_elements = first_odd(int(commands[1]))

        print(first_n_elements)

    elif commands[0] == 'last':
        last_n_elements = []

        if int(commands[1]) < 0 or int(commands[1]) > len(initial_array):
            print('Invalid count')
        else:
            if commands[2] == 'even':
                last_n_elements = last_even(int(commands[1]))
            elif commands[2] == 'odd':
                last_n_elements = last_odd(int(commands[1]))

        print(last_n_elements)
    else:
        continue

    manipulation_commands: str = input()


print(initial_array)
