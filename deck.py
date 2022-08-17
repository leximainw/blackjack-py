from random import shuffle


SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]
VALUES = [
    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Jack", "Queen", "King"
]

IS_FACE = [
    False, False, False, False, False, False, False,
    False, False, False, True, True, True
]

POINT_VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Card:
    def __init__(self, suit, value):
        if suit not in SUITS:
            raise (ValueError if type(suit) is str else TypeError)()
        if value not in VALUES:
            raise (ValueError if type(value) is str else TypeError)()
        self.suit = suit
        self.value = value
        self.is_face = IS_FACE[VALUES.index(value)]
        self.point_value = POINT_VALUE[VALUES.index(value)]

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

    def default():
        deck = Deck()
        for suit in SUITS:
            for value in VALUES:
                deck.cards.append(Card(suit, value))
        return deck

    def add(self, card):
        self.cards.append(card)

    def draw(self):
        if len(self.cards):
            return self.cards.pop()
        else:
            return None

    def shuffle(self):
        shuffle(self.cards)
