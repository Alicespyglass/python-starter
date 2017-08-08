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


# 3. remove instances of null (but NOT false) from an array

# 4. remove instances of nil AND false from an array

# 5. don't reverse the array, but reverse every word inside it. e.g.
# ['dog', 'monkey'] becomes ['god', 'yeknom']

# 6.given an array of student names, like ['Bob', 'Dave', 'Clive']
# give every possible pairing - in this case:
# [['Bob', 'Clive'], ['Bob', 'Dave'], ['Clive', 'Dave']]
# make sure you don't have the same pairing twice,
