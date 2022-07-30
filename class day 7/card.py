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

print(card_deck)


# Initialise index to 0 to start from the beginning of the array
index = 0
# Define loop condition to loop until index is the length of cardDeck
while index < len(card_deck):

    print(card_deck[index])
    # Access attributes of each card with dot notation.
    print(card_deck[index]["name"])
    # Construct a string using attributes of each card object
    card_title = card_deck[index]["name"] + " of " + card_deck[index]["suit"]
    # Log the string
    print(card_title)
    # Increment the card index
    index = index + 1
