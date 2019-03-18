from deckOfCards import deck, card, dealer, hand


def get_input(value, message):
    while True:
        data = input(message)
        if data == value:
            break

    return data


def