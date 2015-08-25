def search(pattern, text):
    "Match pattern anywhere in text; return longest earliest match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None:
            return m

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text)-len(shortest)]


null = frozenset()

def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y


def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null
def seq(x, y): return lambda text: set().union(*map(y, x(text)))
def alt(x, y): return lambda text: x(text) | y(text)
def oneof(chars): return lambda t: set([t[1:]]) if (t and t[0] in chars) else null
def plus(x):      return seq(x, star(x))
def opt(x):       return alt(lit(''), x) #opt(x) means that x is optional
dot = lambda t: set([t[1:]]) if t else null
eol = lambda t: set(['']) if t == '' else null

def star(x): return lambda t: (set([t]) |
                               set(t2 for t1 in x(t) if t1 != t
                                   for t2 in star(x)(t1)))

def test():
    g = alt(lit('a'), lit('b'))
    assert g('abc') == set(['bc'])
    return 'test passes'

print test()
