# Given a string and a pattern, find out if the string contains any permutation of the pattern.

input = [
    {
        "string": "oidbcaf",
        "pattern": "abc",
        "output": True,
    },
    {
        "string": "odicf",
        "pattern": "dc",
        "output": False,
    },
    {
        "string": "bcdxabcdy",
        "pattern": "bcdyabcdx",
        "output": True,
    },
    {
        "string": "aaacb",  # { 'a': 1, 'b': 1, 'c': 1}
        "pattern": "abc",
        "output": True,
    },
]

def findPermutation(string, pattern):
    # trying to match all characters of sliding window with pattern string
    # for every end ptr char, check if its in the pattern
    # if so, subtract 1 to frequency hashmap and check for match
    # return true if num of matches == length of frequency hashmap
    # move start pointer whenever size of sliding window is larger than pattern string length
    # check if startptr in pattern string
    # if so, add 1 to frequency hashmap and check for match

    windowStart, matched = 0, 0
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
            return True

        # starts moving pointer once it reaches the length of pattern
        if windowEnd >= len(pattern) - 1:
            startChar = string[windowStart]
            windowStart += 1
            if startChar in charFreq:
                if charFreq[startChar] == 0:
                    matched -= 1
                charFreq[startChar] += 1
    return False

for i in range(len(input)):
    print("input " + str(i + 1) + ": ", end="")

    if findPermutation(input[i]["string"], input[i]["pattern"]) == input[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")
