from string import split

defined = r"""Exp     => Term [+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [-+]?[0-9]+([.][0-9]*)?"""

def grammar(description, whitespace=r'\s*'):
  """Convert a description to a grammar. Each line is a rule for a
  non-terminal symbol; it looks like this:
    Symbol =>  A1 A2 ... | B1 B2 ... | C1 C2 ...
  where the right-hand side is one or more alternatives, separated by
  the '|' sign. Each alternative is a sequence of atoms, separated by
  spaces. An atom is either a symbol on some left-hand side, or it is
  a regular expression that will be passed to re.match to match a token.

  The grammar that gets defined allows whitespace between tokens by default
  specify '' as the second argument to grammar() to disallow this (or supply
  any regular expression to describe allowable whitespace between tokens)."""
  G = {' ': whitespace}
  description = description.replace('\t', ' ') # remove all tabs
  for line in split(description, '\n'):
    print 'current line:'
    print line
    lhs, rhs = split(line, ' => ', 1)
    alternatives = split(rhs, ' | ')
    G[lhs.rstrip()] = tuple(map(split, alternatives))
  return G

G = grammar(defined)

print G

