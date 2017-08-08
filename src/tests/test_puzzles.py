import puzzles

class TestClass(object):
    def test_one_elements_starting_with_a(self):
        x = ['bananas', 'apples', 'pears', 'avocados']
        assert puzzles.elements_starting_with_a(x) == ['apples', 'avocados']

    def test_two_elements_starting_with_vowels(self):
        x = ['john', 'david', 'omar', 'fred', 'idris', 'angela']
        assert puzzles.elements_starting_with_vowels(x) == ['omar', 'idris', 'angela']

    # const n = ['a', 'b', null, null, false, 'c', null];
    #
    # ['a', 'b', false, 'c']
    #
    # const n = ['a', 'b', null, null, false, 'c', null];
    #
    # ['a', 'b', 'c']
    #
    # const n = ['dog', 'monkey', 'elephant']
    #
    # ['god', 'yeknom', 'tnahpele']
    #
    # const n = ['Bob', 'Dave', 'Clive'];
    #
    # ['Bob', 'Dave'], ['Bob', 'Clive'], ['Dave', 'Clive']]
