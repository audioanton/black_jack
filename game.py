import deck
import player

cards = deck.Deck()

cards.shuffle_deck()

# TODO implement betting in loop

def show_hands(players):
        for p in players:
            p.show_hand(True) if p.is_dealer else p.show_hand(False)

p1 = player.Player(False, 1000, cards.give_start_hand())
dealer = player.Player(True, 0, cards.give_start_hand())

def play_again():
    again = input("hit again? (y/n) ")
    if again.strip().startswith("y"):
        p1.hand.append(cards.give_card())
        return True
    else:
        print(f"{p1.sum_hand()} Standing.")
        return False

def check_results(end):
    for p in [p1, dealer]:
        if p.sum_hand() == 21:
            print("Blackjack!")
            return "dealer" if p.is_dealer else "player"
        if p.sum_hand() > 21:
            print(f"BUST!")
            return "player" if p.is_dealer else "dealer"

    if end:
        if p1.sum_hand() == dealer.sum_hand():
            return "TIE!"
        return "player" if 21 - p1.sum_hand() < 21 - dealer.sum_hand() else "dealer"

    return "continue"

def dealer_play():
    print("Dealer plays...")
    dealer.show_hand(False)
    print(f"Dealer sum: {dealer.sum_hand()}")

    while 21 > dealer.sum_hand() < 17:
        print("Dealer hits.")
        dealer.hand.append(cards.give_card())
        dealer.show_hand(False)
        print(f"Dealer sum: {dealer.sum_hand()}")

while True:
    bet = p1.take_bet()
    print(bet)
    if bet.startswith("B"): break

while True:
    show_hands([dealer, p1])
    print(f"Player sum: {p1.sum_hand()}")
    status = check_results(False)
    if status != "continue":
        print(f"{status} wins!")
        break
    again = play_again()
    if not again:
        dealer_play()
        status = check_results(True)
        print(f"{status} wins!")
        break