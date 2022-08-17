from deck import Deck


class Game:
    def __init__(self, *players):
        self.dealer = Player()
        self.players = players
        self.deck = Deck.default()
        self.deck.shuffle()
        for player in players:
            self.deal(player, 2)
        self.deal(self.dealer, 2)

    def deal(self, player, cards=1):
        for _ in range(cards):
            player.add_card(self.deck.draw())


class Player:
    def __init__(self):
        self.hand = Deck()

    def add_card(self, card):
        self.hand.add(card)


if __name__ == "__main__":
    game = Game(Player())
    for card in game.players[0].hand.cards:
        print(card)
