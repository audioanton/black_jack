class Player:
    def __init__(self, is_dealer, cash, hand):
        self.is_dealer = is_dealer
        self.cards = []
        self.cash = cash
        self.bet = 0
        self.hand = hand

    def take_bet(self):
        try:
            self.bet = int(input("Make your bet: "))
        except ValueError:
            return "Error, only numbers"
        return f"Bet {self.bet} accepted." if self.cash >= self.bet > 0 else f"Faulty bet: {self.bet}. Current cash: {self.cash}."

    def show_hand(self):
        if self.is_dealer:
            print("Dealer cards:")
            print("*hidden*")
            for num in range(1, len(self.hand)):
                print(self.hand[num].show())
        else:
            print("Player cards:")
            for card in self.hand:
                print(card.show())

    def sum_hand(self):
        sum = 0
        for card in self.hand:
            # if card.suit == "Ace"...
            sum += card.rank[1]
        return sum
