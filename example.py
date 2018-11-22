def reverse_words(s):
	words = s.split( )
	words_reversed = words[::-1]
	return ' '.join(words_reversed)

def test_reverse_words():
	assert reverse_words('dogs hate cats') == 'cats hate dogs'
	assert reverse_words('dog eat dog') == 'dog eat dog'
	assert reverse_words('one two three four') == 'four three two one'
