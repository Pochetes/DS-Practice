// finds smallest sized subarray given a targetSum

function findMinSubarray(arr, sum) {
    // initialized to js's highest number to compare min values
    let minWindowSize = Number.MAX_SAFE_INTEGER;
    let currentWindowSum = 0;
    let windowStart = 0;

    // windowEnd will mark the end of curr window of nums
    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        // sums nums in curr window until >= targetSum
        currentWindowSum += arr[windowEnd];

        while (currentWindowSum >= sum) {
            // once targetSum is reached, find min of curr
            // window size.
            minWindowSize = Math.min(minWindowSize, windowEnd - windowStart + 1);
            // guide to remove first value of sum in order to
            // move windows [4, 2, 2] --> [2, 2]
            currentWindowSum -= arr[windowStart];
            // moves starting window pointer to the start
            // of next window
            windowStart++;
        }
    }
    return minWindowSize;
}



function main() {
    let array = [4, 2, 2, 7, 8, 1, 2, 8, 10];
    let targetSum = 8;

    let ans = findMinSubarray(array, targetSum);
    console.log(ans);
}

main();