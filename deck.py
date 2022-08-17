FACES = ["Spades", "Clubs", "Diamonds", "Hearts"]
VALUES = [
    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Jack", "Queen", "King"
]


class Card:
    def __init__(self, face, value):
        if face not in FACES:
            raise (ValueError if type(face) is str else TypeError)()
        if value not in VALUES:
            raise (ValueError if type(value) is str else TypeError)()
        self.face = face
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []

    def default():
        deck = Deck()
        for face in FACES:
            for value in VALUES:
                deck.cards.append(Card(face, value))
        return deck
