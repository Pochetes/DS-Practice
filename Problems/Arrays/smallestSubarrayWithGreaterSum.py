inputs = [
    {
        "arr": [2, 1, 5, 2, 3, 2], # start = 3, end = 5, sum = 7, localLength = 3, minlength = 2
        "s": 7,
        "output": 2
    },
    {
        "arr": [2, 1, 5, 2, 8],
        "s": 7,
        "output": 1
    },
    {
        "arr": [3, 4, 1, 1, 6],
        "s": 8,
        "output": 3
    },
]

def smallestSubarrayWithGreaterSum(arr, s):
    # increase end pointer until sum >= s
    # decrease sum and move start pointer until sum < s
    # evaluate minLength while moving start pointer

    windowStart, windowEnd = 0, 0
    currSum = 0
    minLength = float("inf")

    while windowEnd < len(arr):
        currSum += arr[windowEnd]

        while currSum >= s:
            localLength = windowEnd - windowStart + 1
            minLength = min(minLength, localLength)

            currSum -= arr[windowStart]
            windowStart += 1

        windowEnd += 1

    return minLength
    
for i in range(len(inputs)):
    print("input " + str(i + 1) + ": ", end="")

    if smallestSubarrayWithGreaterSum(inputs[i]["arr"], inputs[i]["s"]) == inputs[i]["output"]:
        print("Correct! ✅ ")
    else:
        print("Not Quite! ❌ ")