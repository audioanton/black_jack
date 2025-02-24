import deck
import player

cards = deck.Deck()

cards.shuffle_deck()

p1 = player.Player(False, 1000)
dealer = player.Player(True, 0)

while True:
    b = p1.take_bet()
    print(b)
    if b.startswith("B"): break
