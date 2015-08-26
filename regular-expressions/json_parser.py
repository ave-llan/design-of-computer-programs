from grammar import grammar, parse, Fail

JSON = grammar(r"""value    => object | array | string | number | true | false | null
string   => ["][^"\\]+["]
number   => int frac exp | int exp | int frac | int
int      => [-]?[\d]+
frac     => [.][\d]+
exp      => [eE][+-]?[\d]+
object   => [{] members [}] | {}
array    => [\[] elements [\]]
elements => value [,] elements | value
members  => pair [,] members | pair
pair     => string [:] value""", whitespace='\s*')

def json_parse(text):
    return parse('value', text, JSON)

def test():
    assert json_parse('["testing", 1, 2, 3]') == (
                       ['value', ['array', '[', ['elements', ['value',
                       ['string', '"testing"']], ',', ['elements', ['value', ['number',
                       ['int', '1']]], ',', ['elements', ['value', ['number',
                       ['int', '2']]], ',', ['elements', ['value', ['number',
                       ['int', '3']]]]]]], ']']], '')

    assert json_parse('-123.456e+789') == (
                       ['value', ['number', ['int', '-123'], ['frac', '.456'], ['exp', 'e+789']]], '')

    assert json_parse('{"age": 21, "state":"CO","occupation":"rides the rodeo"}') == (
                      ['value', ['object', '{', ['members', ['pair', ['string', '"age"'],
                       ':', ['value', ['number', ['int', '21']]]], ',', ['members',
                      ['pair', ['string', '"state"'], ':', ['value', ['string', '"CO"']]],
                      ',', ['members', ['pair', ['string', '"occupation"'], ':',
                      ['value', ['string', '"rides the rodeo"']]]]]], '}']], '')
    return 'tests pass'

print test()