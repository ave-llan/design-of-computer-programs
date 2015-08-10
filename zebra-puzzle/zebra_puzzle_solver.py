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
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory)        #6
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
            if Englishman is red            #2
            if Norwegian is first           #10
            if nextto(Norwegian, blue)      #15
            for (coffee, tea, milk, oj, WATER) in orderings
            if coffee is green              #4
            if Ukranian is tea              #5
            if milk is middle               #9
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Kools is yellow              #8
            if LuckyStrike is oj            #13
            if Japanese is Parliaments      #14
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard is dog              #3
            if OldGold is snails            #7
            if nextto(Chesterfields, fox)   #11
            if nextto(Kools, horse)         #12
            )

