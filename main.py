from deck import Deck

if __name__ == "__main__":
    deck = Deck.default()
    deck.shuffle()
    print([str(x) for x in deck.cards])
