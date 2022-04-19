# Given a string with lowercase letters only, 
# if you are allowed to replace no more than k letters with any letter, 
# find the length of the longest substring having the same letters after replacement.

from dataclasses import replace


inputs = [
    {
        "string": "aabccbb",
        "k": 2,
        "output": 5
    },
    {
        "string": "abbcb",
        "k": 1,
        "output": 4
    },
    {
        "string": "abccde", 
        "k": 1,
        "output": 3
    }
]

def lengthOfLongestSubstr(string, k):
    # add key - char and value - count in hashmap
    # move end pointer while a substring has chars to replace
    # once all k chars have been replaced, move start ptr until at most k chars need to be replaced
    # the length of the substring - repeating char gives how many chars need to be replaced
    
    windowStart = 0
    freq = {}
    longestSubstr = 0

    for windowEnd in range(len(string)):
        if string[windowEnd] in freq:
            freq[string[windowEnd]] += 1
        else:
            freq[string[windowEnd]] = 1

        while (windowEnd - windowStart + 1) - freq[string[windowStart]] > k:
            freq[string[windowStart]] -= 1
            windowStart += 1

        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
    return longestSubstr

for i in range(len(inputs)):
    print("input " + str(i + 1) + ": ", end="")

    if lengthOfLongestSubstr(inputs[i]["string"], inputs[i]["k"]) == inputs[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")