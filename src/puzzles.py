from IPython import embed
from itertools import combinations
from math import ceil

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

# 9. sort an array of words by their last letter, e.g.
# ['sky', 'puma', 'maker'] becomes ['puma', 'maker', 'sky']
def sort_elements_by_last_letter(array):
    return sorted(array, key=lambda x: x[-1])

# 10 - cut strings in half, and return the first half, e.g.
# 'banana' becomes 'ban'. If the string is an odd number of letters
# round up - so 'apple' becomes 'app'
def cut_strings_in_half(string):
    half = ceil(len(string)/2)
    return string[:half]

# 11 - turn a positive integer into a negative integer. A negative integer
# stays negative
def turn_integers_negative(integer):
    if integer > 0:
        return -integer
    return integer

# 12 - turn an array of numbers into two arrays of numbers, one an array of
# even numbers, the other an array of odd numbers
# even numbers come first
# so [1, 2, 3, 4, 5, 6] becomes [[2, 4, 6], [1, 3, 5]]
def split_array_by_odds_and_evens(array):
    even = []
    odd = []
    answer = [even,odd]
    for element in array:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    return answer

# 13 - count the numbers of elements in an element which are palindromes
# a palindrome is a word that's the same backwards as forward
# e.g. 'bob'. So in the array ['bob', 'radar', 'eat'], there
# are 2 palindromes (bob and radar), so the method should return 2
def count_palindromes(array):
    count = 0
    for element in array:
        reverse = element[::-1]
        if element == reverse:
            count += 1
    return count

# 14 - return the shortest word in an array
def return_shortest_word_in_array_A(array):
    shortest = array[0]
    for element in array:
        if len(element) < len(shortest):
            shortest = element
    return shortest

def return_shortest_word_in_array_B(array):
    return min(array, key=len)

# 15 - return the longest word in an array
def return_longest_word_in_array_A(array):
    longest = array[0]
    for element in array:
        if len(element) > len(longest):
            longest = element
    return longest

def return_longest_word_in_array_B(array):
    return max(array, key=len)

# 16 - add up all the numbers in an array, so [1, 3, 5, 6]
# returns 15
def sum_numbers_in_array_A(array):
    total = 0
    for element in array:
        total += element
    return total

def sum_numbers_in_array_B(array):
    return sum(array)

  # 17 - turn an array into itself repeated twice. So [1, 2, 3]
  # becomes [1, 2, 3, 1, 2, 3]

  # 18 - convert a symbol into a string
    #   let a = Symbol();
    # expect(questions.symbolToString(a)).toEqual('Symbol()');


  # 19 - get the average from an array, rounded to the nearest integer
  # so [10, 15, 25] should return 17

  # 20 - get all the elements in an array, up until the first element
  # which is greater than five. e.g.
  # [1, 3, 5, 4, 1, 2, 6, 2, 1, 3, 7]
  # becomes [1, 3, 5, 4, 1, 2]
