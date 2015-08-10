from itertools import permutations

houses = [1, 2, 3, 4, 5]
orderings = list(permutations(houses))


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1


for (red, green, ivory, yellow blue) in orderings:
    for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
            for (coffee, tea, milk, oj, WATER) in orderings:
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                    # Check if all conditions are met
                    pass


