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


# Shuffle the deck and save it in a new variable shuffledDeck
# to communicate that we have shuffled the deck.
shuffled_deck = shuffle_cards(card_deck)


def main():
    # Draw 2 cards from the top of the deck
    computer_card = shuffled_deck.pop()
    player_card = shuffled_deck.pop()

    # Construct an output string to communicate which cards were drawn

    "The {} {} {}".format("cute", "ginger", "kitten")

    my_output = "Computer had {} of {}. Player had {} of {}.".format(
        computer_card["name"],
        computer_card["suit"],
        player_card["name"],
        player_card["suit"],
    )

    # Compare computer and player cards by rank attribute
    # If computer card rank is greater than player card rank, computer wins
    if computer_card["rank"] > player_card["rank"]:
        # Add conditional-dependent text to the output string
        my_output = my_output + " Computer wins."
        # Else if computer card rank is less than player card rank, player wins
    elif computer_card["rank"] < player_card["rank"]:
        my_output = my_output + " Player wins!"
        # Otherwise (i.e. ranks are equal), it's a tie
    else:
        my_output = my_output + "It's a tie."

    # Return the fully-constructed output string
    return my_output


result = main()
print(result)
