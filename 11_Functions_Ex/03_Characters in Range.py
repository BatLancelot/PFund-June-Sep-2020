symbol_a = input()
symbol_b = input()
symbols = []


def letters_in_between(letter_a, letter_b):
    for symbol in range(ord(letter_a) + 1, ord(letter_b)):
        symbols.append(chr(symbol))
    return symbols


print(' '.join(letters_in_between(symbol_a, symbol_b)))
