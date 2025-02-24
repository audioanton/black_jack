from sympy import false


class Player:
    def __init__(self, is_dealer, cash):
        self.is_dealer = is_dealer
        self.cards = []
        self.cash = cash
        self.bet = 0

    def take_bet(self):
        try:
            self.bet = int(input("Make your bet: ")) # try except
        except ValueError:
            return "Error, only numbers"
        return f"Bet {self.bet} accepted." if self.cash >= self.bet > 0 else f"Faulty bet: {self.bet}. Current cash: {self.cash}."
