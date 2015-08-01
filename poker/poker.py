def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    # counts is the count of each rank; ranks lists corresponding ranks
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1) # straight with low Ace
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else               # 5 of a kind
            8 if straight and flush else           # straight flush
            7 if (4, 1) == counts else             # 4 of a kind
            6 if (3, 2) == counts else             # full house
            5 if flush else                        # flush
            4 if straight else                     # straight
            3 if (3, 1, 1) == counts else          # 3 of a kind
            2 if (2, 2, 1) == counts else          # 2 pair
            1 if (2, 1, 1, 1) == counts else       # 2 of a kind
            0), ranks


def group(items):
    "Return a list of [(count, x)...], highest count first, then highest x first."
    groups = [(items.count(item), item) for item in set(items)]
    return sorted(groups, reverse=True)       


def unzip(pairs):
    return zip(*pairs)


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fh, fk]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + 99*[fh]) == [sf]
    return "tests pass"

print test()