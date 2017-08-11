from IPython import embed

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
