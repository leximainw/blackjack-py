FACES = ["Spades", "Clubs", "Diamonds", "Hearts"]
VALUES = [
    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Jack", "Queen", "King"
]


class Deck:
    def __init__(self):
        self.cards = []

    def default():
        deck = Deck()
        for face in FACES:
            for value in VALUES:
                deck.cards.append(f"{value} of {face}")
        return deck
