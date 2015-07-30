import random

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Shuffle the deck and deal out numhands n-card hands."
    random.shuffle(deck)
    return [deck[hand:hand+n] for hand in range(0, n*numhands, n)]