card_string = input().split(' ')
faro_shuffles = int(input())

half_deck_start = len(card_string) // 2

for i in range(faro_shuffles):
    shuffled_deck = []

    for index in range(half_deck_start):
        first_deck = card_string[index]
        second_deck = card_string[index + half_deck_start]
        shuffled_deck.append(first_deck)
        shuffled_deck.append(second_deck)

    card_string = shuffled_deck

print(card_string)
