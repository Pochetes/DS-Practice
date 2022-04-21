# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.

inputs = [
    {
        "arr": [1,1,1,0,0,0,1,1,1,1,0],
        "k": 2,
        "output": 6
    },
    {
        "arr": [0,1,0,0,1,1,0,1,1,0,0,1,1],
        "k": 3,
        "output": 9
    },
]

def lengthOfLongestSubstr(arr, k):
    # expand window until there are no more 0s to replace (i.e k = 0)
    #   if end ptr is 0, decrease the number of 0s to replace
    # move start pointer when k < 0, meaning window shrinks to find bigger substring
    #   if start ptr is 1, just keep shrinking window
    #   if start ptr is 0, add increase the number of 0s to replace   
    # get the max length of substring

    windowStart = 0
    zerosToReplace = k
    longestSubstr = 0

    for windowEnd in range(len(arr)):
        if arr[windowEnd] == 0:
            zerosToReplace -= 1
        
        while zerosToReplace < 0:
            if arr[windowStart] == 0:
                zerosToReplace += 1
            windowStart += 1
    
        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
    return longestSubstr


        

for i in range(len(inputs)):
    print("input " + str(i + 1) + ": ", end="")

    if lengthOfLongestSubstr(inputs[i]["arr"], inputs[i]["k"]) == inputs[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")