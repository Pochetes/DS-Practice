// finds max sum of sub array of size k

function findMaxSumSubArray(arr, k) {
    let maxValue = arr[0];
    let currentRunningSum = 0;

    // iterate through array
    for (let i = 0; i < arr.length; i++) {
        // keep summing up index values until reach k - 1
        currentRunningSum += arr[i];

        if (i >= k - 1) {
            // find max values of sums
            maxValue = Math.max(maxValue, currentRunningSum);
            // to move in linear time, subract the value of
            // the first index in subarray, giving only
            // the sum of the last two numbers and increasing
            // sum until we get size sub array of k
            currentRunningSum -= arr[i - (k - 1)];
        }
    }
    return maxValue;
}

function main() {
    let array = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0];
    let k = 3;

    let ans = findMaxSumSubArray(array, k);
    console.log(ans);
}

main();