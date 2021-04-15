product = input()
qty = int(input())


def bill_calc(prod, quantity):
    if prod == 'coffee':
        return quantity * 1.50
    if prod == 'water':
        return quantity * 1.00
    if prod == 'coke':
        return quantity * 1.40
    if prod == 'snacks':
        return quantity * 2.00


print(f'{bill_calc(product, qty):.2f}')
