from string import split

defined = r"""Exp     => Term [+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [-+]?[0-9]+([.][0-9]*)?"""

def grammar(description):
  """Convert a description to a grammar. """
  G = {}
  for line in split(description, '\n'):
    print 'current line:'
    print line
    lhs, rhs = split(line, ' => ', 1)
    alternatives = split(rhs, ' | ')
    G[lhs.rstrip()] = tuple(map(split, alternatives))
  return G

G = grammar(defined)

print G

