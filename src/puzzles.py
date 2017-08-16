from IPython import embed
from itertools import combinations
from math import *
import string
import re
from datetime import datetime

# 1 - select elements starting with 'a'
def elements_starting_with_a(list):
    answer = []
    for element in list:
        if element[0] == 'a':
            answer.append(element)
    return answer

# 2 - keep only the elements that start with a vowel
def elements_starting_with_vowels(list):
    answer = []
    for element in list:
        if element[0] in 'aeiou':
            answer.append(element)
    return answer

# 3. remove instances of None (but NOT false) from an array
def remove_none_not_false(list):
    answer = []
    for element in list:
        if element != None:
            answer.append(element)
    return answer

# 4. remove instances of nil AND false from an array
def remove_none_and_false(list):
    answer = []
    for element in list:
        if element not in (None, False):
            answer.append(element)
    return answer

# 5. don't reverse the array, but reverse every word inside it. e.g.
def reverse_each_word_in_list(list):
    answer = []
    for element in list:
        answer.append(element[::-1])
    return answer

    # 6.given an array of student names, like ['Bob', 'Dave', 'Clive']
    # give every possible pairing - in this case:
    # [['Bob', 'Clive'], ['Bob', 'Dave'], ['Clive', 'Dave']]
    # make sure you don't have the same pairing twice,
def permutations(list):
    answer = [",".join(map(str, comb)) for comb in combinations(list, 2)]
    return answer

# 7. discard the first 3 elements of an array,
# e.g. [1, 2, 3, 4, 5, 6] becomes [4, 5, 6]
def discard_first_3_elements(list):
    del list[:3]
    return list

# 8. add an element to the beginning of an array
def add_element_to_beginning_or_list(list, element):
    list.insert(0, element)
    return list

# 9. sort an array of words by their last letter, e.g.
# ['sky', 'puma', 'maker'] becomes ['puma', 'maker', 'sky']
def sort_elements_by_last_letter(list):
    return sorted(list, key=lambda x: x[-1])

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
def split_list_by_odds_and_evens(list):
    even = []
    odd = []
    answer = [even,odd]
    for element in list:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    return answer

# 13 - count the numbers of elements in an element which are palindromes
# a palindrome is a word that's the same backwards as forward
# e.g. 'bob'. So in the array ['bob', 'radar', 'eat'], there
# are 2 palindromes (bob and radar), so the method should return 2
def count_palindromes(list):
    count = 0
    for element in list:
        reverse = element[::-1]
        if element == reverse:
            count += 1
    return count

# 14 - return the shortest word in an array
def return_shortest_word_in_list_A(list):
    shortest = list[0]
    for element in list:
        if len(element) < len(shortest):
            shortest = element
    return shortest

def return_shortest_word_in_list_B(list):
    return min(list, key=len)

# 15 - return the longest word in an array
def return_longest_word_in_list_A(list):
    longest = list[0]
    for element in list:
        if len(element) > len(longest):
            longest = element
    return longest

def return_longest_word_in_list_B(list):
    return max(list, key=len)

# 16 - add up all the numbers in an , so [1, 3, 5, 6]
# returns 15
def sum_numbers_in_list_A(list):
    total = 0
    for element in list:
        total += element
    return total

def sum_numbers_in_list_B(list):
    return sum(list)

# 17 - turn an array into itself repeated twice. So [1, 2, 3]
# becomes [1, 2, 3, 1, 2, 3]
def repeat_list(list):
    return list * 2

# 18 - convert a symbol into a string
#   let a = Symbol();
# expect(questions.symbolToString(a)).toEqual('Symbol()');

# NA - Python does not have symbols. In Python, any hashable object can be used a a
# dictionary (hash) key

# 19 - get the average from an array, rounded to the nearest integer
# so [10, 15, 25] should return 17
def list_integer_average(list):
    return ceil(sum(list) / len(list))

# 20 - get all the elements in an array, up until the first element
# which is greater than five. e.g.
# [1, 3, 5, 4, 1, 2, 6, 2, 1, 3, 7]
# becomes [1, 3, 5, 4, 1, 2]
def list_elements_less_than_five(list):
    answer = []
    for element in list:
        if element > 5:
          break
        answer.append(element)
    return answer

# 21 - turn an array (with an even number of elements) into a hash, by
# pairing up elements. e.g. ['a', 'b', 'c', 'd'] becomes
# {'a' => 'b', 'c' => 'd'}
def list_to_dictionary_pairs(list):
    answer = {list[i]: list[i+1] for i in range(0, len(list), 2)}
    return answer

# 22 - get all the letters used in an array of words and return
# it as a array of letters, in alphabetical order
# . e.g. the array ['cat', 'dog', 'fish'] becomes
# ['a', 'c', 'd', 'f', 'g', 'h', 'i', 'o', 's', 't']
def list_of_words_to_list_of_letters(list):
    answer = []
    for word in list:
        for letters in word:
            answer.append(letters)
    answer.sort()
    return answer

# 23 - swap the keys and values in a hash. e.g.
# {'a' => 'b', 'c' => 'd'} becomes
# {'b' => 'a', 'd' => 'c'}
def swap_dictionary_keys_and_values(dict):
    answer = { values:keys for keys, values in dict.items() }
    return answer

# 24 - in a hash where the keys and values are all numbers
# add all the keys and all the values together, e.g.
# {1 => 1, 2 => 2} becomes 6
def sum_dictionary_keys_and_values(dict):
    answer = sum(dict.keys()) + sum(dict.values())
    return answer

# 25 - take out all the capital letters from a string
# so 'Hello JohnDoe' becomes 'ello ohnoe'
def remove_capital_letters_from_string(str):
    answer = re.sub('[^a-z,\s]', '', str)
    return answer

# 26 - round up a float up and convert it to an Integer,
# so 3.214 becomes 4
def round_up_float_to_integer(float):
    return int(ceil(float))

# 27 - round down a float up and convert it to an Integer,
# so 9.52 becomes 9
def round_down_float_to_integer(float):
    return int(floor(float))

# 28 - take a date and format it like dd/mm/yyyy, so Halloween 2013
# becomes 31/10/2013
def format_date(date):
    datetime_object = datetime.strptime(date, '%d %b %Y')
    answer = datetime_object.strftime('%d/%m/%Y')
    return answer

# 29 - get the domain name *without* the .com part, from an email address
# so alex@makersacademy.com becomes makersacademy
def domain_ex_dotcom(email):
    domain = email.split('@')[1].split('.')[0]
    return domain

# 30 - capitalize the first letter in each word of a string,
# except 'a', 'and' and 'the'
# *unless* they come at the start of the start of the string, e.g.
# 'the lion the witch and the wardrobe' becomes
# 'The Lion the Witch and the Wardrobe'
def title_case_A(string):
    exception = ['a', 'and', 'the']
    sentence = string.split()
    for n, word in enumerate(sentence):
        if word not in exception:
            sentence[n] = sentence[n].capitalize()
    sentence[0] = sentence[0].capitalize()
    answer_string = " ".join(str(word) for word in sentence)
    return answer_string

def title_case_B(string):
    exception = ['a', 'and', 'the']
    word_list = re.split(' ', string)       # re.split behaves as expected
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word if word in exception else word.capitalize())
    return " ".join(final)

# 31 - return true if a string contains any special characters
# where 'special character' means anything apart from the letters
# a-z (uppercase and lower) or numbers
def true_if_special_characters(string):
    check = string.split()
    for word in check:
        if word.isalnum():
            pass
        else:
            return True
            break
    return False

# 32 - get the upper limit of a range. e.g. for the range 1..20, you
# should return 20
def upper_limit_of_range(range):
    return max(range) + 1

# 33 - should return true for a 3 dot range like 1...20, false for a
# normal 2 dot range
# NA for Python

# 34 - get the square root of a number
def number_root(number):
    return sqrt(number)

# 35 - count the number of words in a file
def count_words_in_file(file_path):
    num_words = 0
    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    return num_words
