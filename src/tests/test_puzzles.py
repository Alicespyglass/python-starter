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

    def test_5_reverse_each_word_in_list(self):
        x = ['dog', 'monkey', 'elephant'];
        assert puzzles.reverse_each_word_in_list(x) == ['god', 'yeknom', 'tnahpele']

    def test_6_permutations(self):
        x = ['Bob', 'Dave', 'Clive'];
        assert puzzles.permutations(x) == ['Bob,Dave', 'Bob,Clive', 'Dave,Clive']

    def test_7_discard_first_3_elements(self):
        x = [1, 2, 3, 4, 5, 6]
        assert puzzles.discard_first_3_elements(x) == [4, 5, 6]

    def test_8_add_element_to_beginning_of_list(self):
        x = [2, 3, 4, 5]
        element = 1
        assert puzzles.add_element_to_beginning_or_list(x, element) == [1, 2, 3, 4, 5]

    def test_9_sort_elements_by_last_letter(self):
        x = ['sky', 'puma', 'maker']
        assert puzzles.sort_elements_by_last_letter(x) == ['puma', 'maker', 'sky']

    def test_10_cut_strings_in_half(self):
        x = 'banana'
        y = 'apple'
        assert puzzles.cut_strings_in_half(x) == 'ban'
        assert puzzles.cut_strings_in_half(y) == 'app'

    def test_11_turn_integers_negative(self):
        x = 5
        y = -7
        assert puzzles.turn_integers_negative(x) == -5
        assert puzzles.turn_integers_negative(y) == -7

    def test_12_split_list_by_odds_and_evens(self):
        x = [1, 2, 3, 4, 5, 6]
        assert puzzles.split_list_by_odds_and_evens(x) == [[2, 4, 6], [1, 3, 5]]

    def test_13_count_palindromes(self):
        x = ['bob', 'radar', 'eat']
        assert puzzles.count_palindromes(x) == 2

    def test_14a_return_shortest_word_in_list(self):
        x = ['here', 'is', 'a', 'bunch', 'of', 'words', 'of', 'different', 'lengths']
        assert puzzles.return_shortest_word_in_list_A(x) == 'a'

    def test_14b_return_shortest_word_in_list(self):
        x = ['here', 'is', 'a', 'bunch', 'of', 'words', 'of', 'different', 'lengths']
        assert puzzles.return_shortest_word_in_list_B(x) == 'a'

    def test_15a_return_longest_word_in_list(self):
        x = ['here', 'is', 'a', 'bunch', 'of', 'words', 'of', 'different', 'lengths']
        assert puzzles.return_longest_word_in_list_A(x) == 'different'

    def test_15b_return_longest_word_in_list(self):
        x = ['here', 'is', 'a', 'bunch', 'of', 'words', 'of', 'different', 'lengths']
        assert puzzles.return_longest_word_in_list_B(x) == 'different'

    def test_16a_sum_numbers_in_list(self):
        x = [1, 3, 5, 6]
        assert puzzles.sum_numbers_in_list_A(x) == 15

    def test_16b_sum_numbers_in_list(self):
        x = [1, 3, 5, 6]
        assert puzzles.sum_numbers_in_list_B(x) == 15

    def test_17_repeat_list(self):
        x = [1, 2, 3]
        assert puzzles.repeat_list(x) == [1, 2, 3, 1, 2, 3]

    def test_19_list_integer_average(self):
        x = [10, 15, 25]
        assert puzzles.list_integer_average(x) == 17

    def test_20_list_elements_less_than_five(self):
        x = [1, 3, 5, 4, 1, 2, 6, 2, 1, 3, 7]
        assert puzzles.list_elements_less_than_five(x) == [1, 3, 5, 4, 1, 2]
        
