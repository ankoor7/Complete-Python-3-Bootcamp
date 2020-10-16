from deckOfCards import deck, card, dealer, hand


def default_validator(value):
    return value and True


def number_validator(value):
    try:
        val = int(value)
        if (val > 0):
            return val
        else:
            return False
    except ValueError:
        return False


def get_input(message, validator=default_validator):
    while True:
        data = input(message)
        if validator(data):
            break

    return validator(data)
