class Player:
    def __init__(self, is_dealer, hand):
        self.is_dealer = is_dealer
        self.cash = 0
        self.bet = 0
        self.hand = hand

    def take_bet(self):
        try:
            self.bet = int(input("Make your bet: "))
        except ValueError:
            return "Error, only numbers"
        return f"Bet {self.bet} accepted." if self.cash >= self.bet > 0 else f"Faulty bet: {self.bet}. Current cash: {self.cash}."

    def take_cash(self):
        try:
            self.cash = int(input("How much cash do you want to play with? "))
        except ValueError:
            return "Error, only numbers"
        return f"{self.cash} accepted."

    def show_hand(self, hidden):
        if hidden:
            print("Dealer cards:")
            print("*hidden*")
            for num in range(1, len(self.hand)):
                print(self.hand[num].show())
        else:
            if self.is_dealer:
                print("Dealer cards:")
            else:
                print("Player cards:")
            for card in self.hand:
                print(card.show())

    def sum_hand(self):
        sum_hand = 0
        for card in self.hand:
            if card.rank[0] == 'Ace':
                sum_hand += 1 if sum_hand + 11 > 21 else card.rank[1]
            else:
                sum_hand += card.rank[1]
        return sum_hand
