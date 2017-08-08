import puzzles

class TestClass(object):
    def test_one(self):
        x = ['bananas', 'apples', 'pears', 'avocados']
        assert puzzles.elements_starting_with_a(x) == ['apples', 'avocados']

# ['john', 'david', 'omar', 'fred', 'idris', 'angela']
# ['omar', 'idris', 'angela']
