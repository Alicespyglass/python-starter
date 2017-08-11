from IPython import embed
from itertools import combinations

# 1 - select elements starting with 'a'
def elements_starting_with_a(array):
    answer = []
    for element in array:
        if element[0] == 'a':
            answer.append(element)
    return answer

# 2 - keep only the elements that start with a vowel
def elements_starting_with_vowels(array):
    answer = []
    for element in array:
        if element[0] in 'aeiou':
            answer.append(element)
    return answer

# 3. remove instances of None (but NOT false) from an array
def remove_none_not_false(array):
    answer = []
    for element in array:
        if element != None:
            answer.append(element)
    return answer

# 4. remove instances of nil AND false from an array
def remove_none_and_false(array):
    answer = []
    for element in array:
        if element not in (None, False):
            answer.append(element)
    return answer

# 5. don't reverse the array, but reverse every word inside it. e.g.
def reverse_each_word_in_array(array):
    answer = []
    for element in array:
        answer.append(element[::-1])
    return answer

    # 6.given an array of student names, like ['Bob', 'Dave', 'Clive']
    # give every possible pairing - in this case:
    # [['Bob', 'Clive'], ['Bob', 'Dave'], ['Clive', 'Dave']]
    # make sure you don't have the same pairing twice,
def permutations(array):
    answer = [",".join(map(str, comb)) for comb in combinations(array, 2)]
    return answer

# 7. discard the first 3 elements of an array,
# e.g. [1, 2, 3, 4, 5, 6] becomes [4, 5, 6]
def discard_first_3_elements(array):
    del array[:3]
    return array

 # 8. add an element to the beginning of an array
def add_element_to_beginning_or_array(array, element):
    array.insert(0, element)
    return array

  # // 9. sort an array of words by their last letter, e.g.
  #
  # // ['sky', 'puma', 'maker'] becomes ['puma', 'maker', 'sky']
  #
  #
  #
  # // 10 - cut strings in half, and return the first half, e.g.
  #
  # // 'banana' becomes 'ban'. If the string is an odd number of letters
  #
  # // round up - so 'apple' becomes 'app'
