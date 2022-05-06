"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N! permutations (or anagrams) of a string having N characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""

input = [
    {
        "string": "ppqp",
        "pattern": "pq",
        "output": [1, 2]
    },
    {
        "string": "abbcabc",
        "pattern": "abc",
        "output": [2, 3, 4]
    },
]

def findStringAnagrams(string, pattern):
    # we need to find the starting ptr of the sliding windows that matches the pattern
    # fill in the frequencies of the chars the pattern string
    # for each char in string, check if the end ptr char is in the pattern
    #   if so, dec freq of that char by 1
    #       if the freq of that char is 0, we have exhausted all counts of that char in the pattern
    # after the sliding window satisfies len of pattern, begin checking start ptr char
    #   if the start ptr char is in the pattern
    #       if the freq of that char is 0, we are starting again so we remove the matches
    #       inc freq of that char by 1
    #   move the start ptr by 1
    
    windowStart, matched = 0, 0
    strAnagrams = []
    charFreq = {}

    for char in pattern:
        if char not in charFreq:
            charFreq[char] = 1
        else:
            charFreq[char] += 1
    
    for windowEnd in range(len(string)):
        endChar = string[windowEnd]
        if endChar in charFreq:
            charFreq[endChar] -= 1
            if charFreq[endChar] == 0:
                matched += 1
        
        if matched == len(charFreq):
            strAnagrams.append(windowStart)
        
        if windowEnd >= len(pattern) - 1:
            startChar = string[windowStart]
            if startChar in charFreq:
                if charFreq[startChar] == 0:
                    matched -= 1
                charFreq[startChar] += 1
            windowStart += 1
    return strAnagrams
            


for i in range(len(input)):
    print("Input " + str(i + 1) + ": ", end="")

    if findStringAnagrams(input[i]["string"], input[i]["pattern"]) == input[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")