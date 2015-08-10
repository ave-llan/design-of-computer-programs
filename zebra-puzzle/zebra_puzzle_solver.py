from itertools import permutations

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(permutations(houses))
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow blue) in orderings
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings:
            for (dog, snails, fox, horse, ZEBRA) in orderings
            for (coffee, tea, milk, oj, WATER) in orderings
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Englishman is red            #2
            if Spaniard is dog              #3
            if coffee is green              #4
            if Ukranian is tea              #5
            if imright(green, ivory)        #6
            if OldGold is snails            #7
            if Kools is yellow              #8
            if milk is middle               #9
            if Norwegian is first           #10
            if nextto(Chesterfields, fox)   #11
            if nextto(Kools, horse)         #12
            if LuckyStrike is oj            #13
            if Japanese is Parliaments      #14
            if nextto(Norwegian, blue)      #15
            )

