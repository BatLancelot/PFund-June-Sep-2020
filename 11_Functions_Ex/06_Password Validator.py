password = input()
errors = []


def password_checker(password):
    digit_counter = 0

    if len(password) < 6 or len(password) > 10:
        errors.append("Password must be between 6 and 10 characters")

    for char in password:
        if char.isalpha():
            continue
        elif char.isdigit():
            digit_counter += 1
            continue
        else:
            errors.append("Password must consist only of letters and digits")
            break

    if digit_counter < 2:
        errors.append("Password must have at least 2 digits")

    if len(errors) == 0:
        print("Password is valid")
    else:
        print('\n'.join(errors))


password_checker(password)
