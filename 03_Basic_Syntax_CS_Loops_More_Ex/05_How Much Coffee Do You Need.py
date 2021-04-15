event = input()
coffee_counter = 0

if event.isupper():
    coffee_needed = 2

while event != 'END':
    if event.isupper():
        coffee_needed = 2
    else:
        coffee_needed = 1
    event = event.lower()

    if event == 'coding':
        coffee_counter += coffee_needed
    elif event == 'cat' or event == 'dog':
        coffee_counter += coffee_needed
    elif event == 'movie':
        coffee_counter += coffee_needed

    event = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
