from string import split
import re

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
    lhs, rhs = split(line, ' => ', 1)
    alternatives = split(rhs, ' | ')
    G[lhs.rstrip()] = tuple(map(split, alternatives))
  return G

G = grammar(defined)

def parse(start_symbol, text, grammar):
  """Example call: parse('Exp', '3*x + b', G).
  Returns a (tree, remainder) pair. If remainder is '',
  it has parsed the whole string. Failure iff remainder is None.
  This is a deterministic PEG parser, so rule order (left-to-right)
  matters. Do 'E => T op E | T', putting the longest parse first;
  don't do 'E => T | T op E'
  Also, no left recursion allowed: don't do 'E => E op T' """

  tokenizer = grammar[' '] + '(%s)'

  def parse_sequence(sequence, text):
    result = []
    for atom in sequence:
      tree, text = parse_atom(atom, text)
      if text is None: return Fail
      result.append(tree)
    return result, text

  def parse_atom(atom, text):
    if atom in grammar: # Non-Terminal: tuple of alternatives
      for alternative in grammar[atom]:
        tree, rem = parse_sequence(alternative, text)
        if rem is not None: return [atom]+tree, rem
      return Fail
    else: # Terminal: match characters against start of text
      m = re.match(tokenizer % atom, text)
      return Fail if (not m) else (m.group(1), text[m.end():])

  # Body of parse:
  return parse_atom(start_symbol, text)

Fail = (None, None)

