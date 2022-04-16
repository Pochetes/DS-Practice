# Given a string, find the length of the longest substring in it with no more than K distinct characters.
inputs = [
    {
        "string": "araaci",
        "k": 2,
        "output": 4,
    },
    {
        "string": "araaci",
        "k": 1,
        "output": 2,
    },
    {
        "string": "cbbebi",
        "k": 3,
        "output": 5,
    },
    {
        "string": "cbbebi",
        "k": 10,
        "output": 6
    },
]


def longestSubstringWithKDistinct(string, k):
    # add char - key, count - value in hashmap
    # if does not meet criteria, move start until it does
    # check for criteria and longest length substring
    windowStart = 0
    freq = {}
    longestLength = float("-inf")
    
    for windowEnd in range(len(string)):
        if string[windowEnd] in freq:
            freq[string[windowEnd]] += 1
        else:
            freq[string[windowEnd]] = 1

        while len(freq) > k:
            freq[string[windowStart]] -= 1
            if freq[string[windowStart]] == 0:
                freq.pop(string[windowStart])
            windowStart += 1
        
        if len(freq) <= k:
            localLength = windowEnd - windowStart + 1
            longestLength = max(longestLength, localLength)
        
    return longestLength




for i in range(len(inputs)):
    print("input " + str(i + 1) + ": ", end="")

    if longestSubstringWithKDistinct(inputs[i]["string"], inputs[i]["k"]) == inputs[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")