def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null

def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)

def star(x):        return lambda Ns: opt(plus(x))(Ns)

def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky

def oneof(chars):   return lambda Ns: set(chars) if 1 in Ns else null

@n_ary
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)

def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.

null = frozenset([])

def genseq(x, y, Ns, startx=0):
    "Set of matches to xy whose total len is in Ns, with x-match's len in Ns"
    if not Ns:
        return null
    xmatches = x(set(range(startx, max(Ns)+1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m >= 0)
    ymatches = y(Ns_y)
    return set(m1 + m2
               for m1 in xmatches for m2 in ymatches
               if len(m1+m2) in Ns)

from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    update_wrapper(n_ary_f, f) # add documentation from original function
    return n_ary_f

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again wtih same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f


def test():

    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    return 'tests pass'
print test()