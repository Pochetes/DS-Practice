# Given a string, find the length of the longest substring, which has all distinct characters.

inputs = [
    {
        "string": "aabccbb",
        "output": 3
    },
    {
        "string": "abbbb",
        "output": 2
    },
    {
        "string": "abccde",
        "output": 3
    },
]

def nonRepeatSubstring(string):
    # add end pointer char to hashmap with key - char and value - count
    # shrink sliding window while substring does not have distinct chars
    # for every substring that satisfies criteria, check for longest substring
    windowStart = 0
    longestSubstr = 0
    freq = {}
    
    for windowEnd in range(len(string)):
        if string[windowEnd] in freq:
            freq[string[windowEnd]] += 1
        else:
            freq[string[windowEnd]] = 1

        while freq[string[windowEnd]] > 1:
            freq[string[windowStart]] -= 1
            if freq[string[windowStart]] == 0:
                freq.pop(string[windowStart])
            windowStart += 1
        
        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
    
    return longestSubstr
    

for i in range(len(inputs)):
    print("input " + str(i + 1) + ": ", end="")

    if nonRepeatSubstring(inputs[i]["string"]) == inputs[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")