import deck
import player

def show_hands(players):
        for p in players:
            p.show_hand(True) if p.is_dealer else p.show_hand(False)

def play_again(player):
    again = input("hit again? (y/n) ")
    if again.strip().startswith("y"):
        player.hand.append(cards.give_card())
        return True
    else:
        print(f"{player.sum_hand()} Standing.")
        return False

def calculate_bet(result, player):
    if "player" in result:
        player.cash += player.bet
    elif "dealer" in result:
        player.cash -= player.bet
    return player.cash

def check_results(end, players):
    results = ["dealer wins!", "player wins!", "TIE! Bet is returned", "BUST!", "Blackjack!"]

    for p in players:
        if p.sum_hand() == 21:
            return f"{results[-1]} {results[0]}" if p.is_dealer else f"{results[-1]} {results[1]}"
        if p.sum_hand() > 21:
            return f"{results[3]} {results[1]}" if p.is_dealer else f"{results[3]} {results[0]}"

    if end:
        if players[0].sum_hand() == players[1].sum_hand():
            return results[2]
        return results[1] if 21 - players[0].sum_hand() < 21 - players[1].sum_hand() else results[0]

    return "continue"

def dealer_play(player):
    print("Dealer plays...")
    player.show_hand(False)
    print(f"Dealer sum: {player.sum_hand()}")

    while 21 > player.sum_hand() < 17:
        print("Dealer hits.")
        player.hand.append(cards.give_card())
        player.show_hand(False)
        print(f"Dealer sum: {player.sum_hand()}")

# start game
cards = deck.Deck()
cards.shuffle_deck()

player_one = player.Player(False, cards.give_start_hand())
dealer = player.Player(True, cards.give_start_hand())

while True:
    cash = player_one.take_cash()
    print(cash)
    if not cash.startswith("E"): break

# game main loop
while True:
    if player_one.cash == 0:
        print("Game Over!")
        break

    cards = deck.Deck()
    cards.shuffle_deck()
    player_one.hand = cards.give_start_hand()
    dealer.hand = cards.give_start_hand()

    while True:
        bet = player_one.take_bet()
        print(bet)
        if bet.startswith("B"): break

    while True:
        show_hands([dealer, player_one])
        print(f"Player sum: {player_one.sum_hand()}")
        result = check_results(False, [player_one, dealer])
        if result != "continue":
            print(result)
            print(f"Player cash: {calculate_bet(result, player_one)}")
            break
        again = play_again(player_one)
        if not again:
            dealer_play(dealer)
            result = check_results(True, [player_one, dealer])
            print(result)
            print(f"Player cash left: {calculate_bet(result, player_one)}")
            break

    answer = input("Keep playing? (y/n) ")
    if answer.strip().startswith("n"):
        print(f"Ending sum: {player_one.cash}. See you!")
        break
