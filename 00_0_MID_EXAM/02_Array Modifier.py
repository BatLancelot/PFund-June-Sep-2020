initial_array = input().split()
array_of_integers = [int(i) for i in initial_array]
# array_of_integers: list = list(map(int, initial_array))

full_command = input().split()
command = full_command[0]

while command != 'end':

    if command == 'swap':

        array_of_integers[int(full_command[1])], array_of_integers[int(full_command[2])] = \
            array_of_integers[int(full_command[2])], array_of_integers[int(full_command[1])]

    elif command == 'multiply':
        first_index = int(full_command[1])
        second_index = int(full_command[2])

        multiply_result = array_of_integers[first_index] * array_of_integers[second_index]
        array_of_integers.pop(first_index)
        array_of_integers.insert(first_index, multiply_result)

    elif command == 'decrease':
        decreased_array = []
        for item in array_of_integers:
            item -= 1
            decreased_array.append(item)
        array_of_integers = decreased_array

    full_command = input().split()
    command = full_command[0]

final_array = [str(i) for i in array_of_integers]

print(', '.join(final_array))
