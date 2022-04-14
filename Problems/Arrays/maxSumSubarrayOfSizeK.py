inputs = [
    {
        "arr": [2, 1, 5, 1, 3, 2],
        "k": 3,
        "output": 9
    },
    {
        "arr": [2, 3, 4, 1, 5],
        "k": 2,
        "output": 7
    },
]

def maxSumSubarrayOfSizeK(arr, k):
    windowStart = 0
    windowEnd = 0
    currentSum = 0
    globalSum = 0

    for windowEnd in range(len(arr)):
        currentSum += arr[windowEnd]

        if (windowEnd + 1) - windowStart == k:
            if currentSum >= globalSum:
                globalSum = currentSum
            
            currentSum -= arr[windowStart]
            windowStart += 1
    return globalSum


for i in range(len(inputs)):
    print("input " + str(i + 1) + ": ", end="")

    if maxSumSubarrayOfSizeK(inputs[i]["arr"], inputs[i]["k"]) == inputs[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")