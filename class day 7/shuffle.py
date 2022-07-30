import random

card_deck = [
    {
        "rank": 1,
        "suit": "heart",
        "name": "one",
    },
    {
        "rank": 2,
        "suit": "heart",
        "name": "two",
    },
]

# Get a random index ranging from 0 (inclusive) to max (exclusive).
def get_random_index(max):
    my_random_value = random.randint(0, max)
    return my_random_value


# Shuffle the elements in the cardDeck array
def shuffle_cards(card_deck):
    # Loop over the card deck array once
    current_index = 0
    card_deck_length = len(card_deck)
    while current_index < card_deck_length:
        # Select a random index in the deck
        random_index = get_random_index(card_deck_length - 1)
        # Select the card that corresponds to randomIndex
        random_card = card_deck[random_index]
        # Select the card that corresponds to currentIndex
        current_card = card_deck[current_index]
        # Swap positions of randomCard and currentCard in the deck
        card_deck[current_index] = random_card
        card_deck[random_index] = current_card
        # Increment currentIndex
        current_index = current_index + 1

    # Return the shuffled deck
    return card_deck


print(shuffle_cards(card_deck))
