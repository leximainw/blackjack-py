from deck import Deck

if __name__ == "__main__":
    deck = Deck.default()
    deck.shuffle()
    for _ in range(10):
        print(deck.draw())
    print([str(x) for x in deck.cards])
