"""
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"

Example 3:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Example 4:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""

input = [
    {
        "string": "aabdec",
        "pattern": "abc",
        "output": "abdec"
    },
    {
        "string": "aabdec",
        "pattern": "abac",
        "output": "aabdec"
    },
    {
        "string": "abdbca",
        "pattern": "abc",
        "output": "bca"
    },
    {
        "string": "adcad",
        "pattern": "abc",
        "output": ""
    },
]


def findSubstring(string, pattern):
    # goal is to find the shortest substring that has ALL chars of pattern in it
    # fill up hashmap of pattern
    # traverse end ptr and for each char check if letter is in the char freq of pattern
    # if so, subtract the freq of that char and check if value is 0 to find a match
    # once pattern is found in substring (num of matches equal the len of hashmap)
    # check if substring is the shortest length, and replace answer with it
    # move start pointer until it condition is satisfied 
    # check if letter is in hashmap to add freq of it and possibly remove matches
    
    windowStart, matches = 0, 0
    minLength = float("inf")
    res = ""
    charFreq = {}

    if len(pattern) > len(string):
        return res

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
                matches += 1

        while matches >= len(charFreq):
            currWindowLength = windowEnd - windowStart + 1
            if currWindowLength <= minLength:
                res = string[windowStart: windowEnd + 1]

            startChar = string[windowStart]
            if startChar in charFreq:
                if charFreq[startChar] == 0:
                    matches -= 1
                charFreq[startChar] += 1
            windowStart += 1
    return res
                            



for i in range(len(input)):
    print("Input " + str(i + 1) + ": ", end="")

    if findSubstring(input[i]["string"], input[i]["pattern"]) == input[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")