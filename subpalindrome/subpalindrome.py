# A function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)
    def length(slice): a,b = slice; return b-a
    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start+1)]
    return max(candidates, key=length)


def grow(text, start, end):
    "Start with a 0 or 1 length palindrome; try to grow a bigger one."
    while (start > 0 and end < len(text)
            and text[start-1].lower() == text[end].lower()):
        start -= 1; end += 1
    return (start, end)

    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()