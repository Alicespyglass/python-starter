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

    def test_7_discard_first_3_elements(self):
        x = [1, 2, 3, 4, 5, 6]
        assert puzzles.discard_first_3_elements(x) == [4, 5, 6]

    def test_8_add_element_to_beginning_of_array(self):
        x = [2, 3, 4, 5]
        element = 1
        assert puzzles.add_element_to_beginning_or_array(x, element) == [1, 2, 3, 4, 5]

    def test_9_sort_elements_by_last_letter(self):
        x = ['sky', 'puma', 'maker']
        assert puzzles.sort_elements_by_last_letter(x) == ['puma', 'maker', 'sky']

    def test_10_cut_strings_in_half(self):
        x = 'banana'
        y = 'apple'
        assert puzzles.cut_strings_in_half(x) == 'ban'
        assert puzzles.cut_strings_in_half(y) == 'app'
