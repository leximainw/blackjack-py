from deck import Deck


class Game:
    def __init__(self, *players):
        self.dealer = Player()
        self.curr_player = 0
        self.players = players
        self.deck = Deck.default()
        self.deck.shuffle()
        for player in players:
            self.deal(player, 2)
        self.deal(self.dealer, 2)

    def deal(self, player, cards=1):
        drawn = []
        for _ in range(cards):
            card = self.deck.draw()
            drawn.append(card)
            player.add_card(card)
        return drawn

    def play(self):
        while True:
            self.play_next()
            # TODO: implement game-over condition

    def play_next(self):
        if self.curr_player == len(self.players):
            self.play_dealer()
            self.curr_player = 0
        else:
            self.play_player(self.players[self.curr_player])
            self.curr_player += 1

    def play_dealer(self):
        if Game.score_hand(self.dealer.hand, True) < 17:
            self.deal(self.dealer)

    def play_player(self, player):
        print(f"Player {self.curr_player + 1}, your hand is:")
        for card in player.hand.cards:
            print(f"   {card}")
        while True:
            choice = input("Hit or stand pat? ").lower()
            if choice == "hit" or choice == "hit me":
                print(f"You drew the {self.deal(player)[0]}!")
                print(f"You have {Game.score_hand(player.hand)} points.")
                break
            elif choice == "stand" or choice == "pat" or choice == "stand pat":
                break
            else:
                print("I don't know what that means!")

    def score_hand(hand, as_dealer=False):
        score = 0
        num_aces = 0
        for card in hand.cards:
            if card.is_face():
                score += 10
            elif card.value != "Ace":
                score += card.get_value()
            else:
                score += 11
                num_aces += 1
        if as_dealer:
            score -= max(num_aces - 1, 0) * 10
            num_aces = min(num_aces, 1)
        for _ in range(num_aces):
            if score <= 21:
                break
            score -= 10
        return score


class Player:
    def __init__(self):
        self.hand = Deck()

    def add_card(self, card):
        self.hand.add(card)


if __name__ == "__main__":
    game = Game(Player())
    game.play()
