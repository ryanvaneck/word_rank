"""
Finds the rank of word in a hypothetical sorted list of all permutations of its letters. 
Loops through letters of word and counts the number of permutations that would rank before the substring starting at the letter.
Best explained with this example, using the word 'question':
4 letters rank before 'q':
 'i', 7! permutations with 'i' at beginning, all of which would rank before 'question'
 'e', 7! permutations with 'e' at beginning, all of which would rank before 'question'
 's', 7! permutations with 's' at beginning, all of which would rank before 'question'
 't', 7! permutations with 't' at beginning, all of which would rank before 'question'

leaving 'q' at the beginning, there are 6 letters left that rank before the second letter, 'u'
 'e', 6! permutations with 'qe' at beginning
 's', 6! permutations with 'qs' at beginning
 't', 6! permutations with 'qt' at beginning
 'i', 6! permutations with 'qi' at beginning
 'o', 6! permutations with 'qo' at beginning
 'n', 6! permutations with 'qn' at beginning

leaving 'qu' at beginning, there are no letters left that rank before the 3rd letter, 'e'

leaving 'que' at beginning, there are 3 letters left that rank before the 4th letter, 's'
 i, 4! permutations with 'quei' at beginning
 o, 4! permutations with 'queo' at beginning
 n, 4! permutations with 'quen' at beginning

leaving 'ques' at beginning, there are 3 letters left that rank before the 5th letter, 't'
 i, 3! permutations with 'quesi' at beginning
 o, 3! permutations with 'queso' at beginning
 n, 3! permutations with 'quesn' at beginning

leaving 'quest' at the beginning, there are no letters left that ranks before the 6th letter, 'i'

leaving 'questi' at the beginning, there is one letter left that ranks before the 7th letter, 'o'
 n, 1 permutation with 'questin' at the beginning

4*7! + 6*6! + 3*4! + 3*3! + 1*1! + 1 = 24572

"""
import sys, math, time

def main(args):
    word = args[1]
    length = len(word)
    result = 0
    for i in range(length):
        count = countPreviousPermutations(word[i:])
        result += count
    print result + 1

"""
Counts number of permutations of a word that would be ranked before the word based on the first letter only. 
Loops through letters of the word looking for those that rank before the first letter, then counts all permutations of the remaining letters. 
Avoids double counting repeated letters by tracking letters in an array.
'math' -> 
1. 'a' at beginning -> perms of 'mth' -> 6
2. 'h' at beginning -> perms of 'mat' -> 6
returns 12

'athens' ->
returns 0 because no letter ranks before 'a'
"""
def countPreviousPermutations(word):
    length = len(word)
    result = 0
    counted = []
    for i in range(1, length):
        if word[i] < word[0] and word[i] not in counted:
            counted.append(word[i])
            first_index = 1 if i==0 else 0
            other_letters = word[first_index:i] + word[i+1:]
            count = countAllPermutations(other_letters)
            result += count
    return result

""" 
 Counts total number of possible permutations of letters in a word, excluding duplicates resulting from repeated characters.
 First takes factorial of word to get the number of permutations if all letters are unique, then counts repeated
 characters and divides the result by the factorial of each character total.
 aaab -> 4!/3! = 4 | abab -> 4!/2!/2! = 6
"""
def countAllPermutations(word):
    result = math.factorial(len(word))
    counts = countChars(word)
    for key in counts:
        count = counts[key]
        if count > 1:
            result = result / math.factorial(count)
    return result

"""
Builds and returns map of characters to number of occurences in word
"""
def countChars(word):
    length = len(word)
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

main(sys.argv)
