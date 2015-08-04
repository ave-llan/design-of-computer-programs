from poker import hand_rank
from itertools import combinations, product


def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    return max(combinations(hand, 5), key=hand_rank)


# '?B' can be any spade or club
# '?R' can be any heart or diamond 
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h)
    			for h in product(*map(card_expand, hand)))
    return max(hands, key=hand_rank)

def card_expand(card):
	"""If card is a joker, expand it and return a list.
	Else, return the card in a list of length 1."""
	if card == '?B':
		return [r+s for r in '23456789TJQKA' for s in 'SC']
	elif card == '?R':
		return [r+s for r in '23456789TJQKA' for s in 'DH']
	else:
		return [card]



# Tests

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


print test_best_hand()
print test_best_wild_hand()
