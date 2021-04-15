events = input().split('|')

initial_energy = 100
initial_coins = 100
bankrupt = False

for event in events:
    event_values = event.split('-')

    if event_values[0] == "rest":
        gained_energy = 0
        if initial_energy + int(event_values[1]) < 100:
            gained_energy = int(event_values[1])
            initial_energy += int(event_values[1])
        else:
            gained_energy = 100 - initial_energy
            initial_energy = 100
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {initial_energy}.')

    elif event_values[0] == "order":
        if initial_energy < 30:
            initial_energy += 50
            print(f'You had to rest!')
            continue
        initial_coins += int(event_values[1])
        initial_energy -= 30
        print(f'You earned {event_values[1]} coins.')

    else:
        if initial_coins <= int(event_values[1]):
            print(f'Closed! Cannot afford {event_values[0]}.')
            bankrupt = True
            break
        initial_coins -= int(event_values[1])
        print(f'You bought {event_values[0]}.')

if not bankrupt:
    print(f'Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}')
