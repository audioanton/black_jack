import deck
import player

cards = deck.Deck()

cards.shuffle_deck()

def show_hands(players, player_turn):
    if player_turn:
        for player in players:
            player.show_hand()

def show_sums(players):
    for p in players:
        if not p.is_dealer:
            print(f"Player sum: {p.sum_hand()}")

p1 = player.Player(False, 1000, cards.give_start_hand())
dealer = player.Player(True, 0, cards.give_start_hand())

def play_again(player, cards):
    again = input("play again? (y/n)")
    if again.strip().startswith("y"):
        player.hand.append(cards.give_card()) # not working
        return True
    else:
        print("stopping")
        return False


while True:
    b = p1.take_bet()
    print(b)
    if b.startswith("B"): break


while True:
    show_hands([dealer, p1], True)
    show_sums([p1, dealer])
    b = play_again(p1, cards)
    if not b:
        break