import puzzles

class TestClass(object):
    def test_1_elements_starting_with_a(self):
        x = ['bananas', 'apples', 'pears', 'avocados']
        assert puzzles.elements_starting_with_a(x) == ['apples', 'avocados']

    def test_2_elements_starting_with_vowels(self):
        x = ['john', 'david', 'omar', 'fred', 'idris', 'angela']
        assert puzzles.elements_starting_with_vowels(x) == ['omar', 'idris', 'angela']

    def test_3_remove_none_not_false(self):
        x = ['a', 'b', None, None, False, 'c', None];
        assert puzzles.remove_none_not_false(x) == ['a', 'b', False, 'c']

    def test_4_remove_none_and_false(self):
        x = ['a', 'b', None, None, False, 'c', None];
        assert puzzles.remove_none_and_false(x) == ['a', 'b', 'c']

    def test_5_reverse_each_word_in_array(self):
        x = ['dog', 'monkey', 'elephant'];
        assert puzzles.reverse_each_word_in_array(x) == ['god', 'yeknom', 'tnahpele']

    def test_6_permutations(self):
        x = ['Bob', 'Dave', 'Clive'];
        assert puzzles.permutations(x) == ['Bob,Dave', 'Bob,Clive', 'Dave,Clive']

  # // e.g. [1, 2, 3, 4, 5, 6] becomes [4, 5, 6]
    # const n = [2, 3, 4, 5],

# [1, 2, 3, 4, 5]
#  ['sky', 'puma', 'maker'] becomes ['puma', 'maker', 'sky']

  # // 'banana' becomes 'ban'. If the string is an odd number of letters
  #
  # // round up - so 'apple' becomes 'app'
