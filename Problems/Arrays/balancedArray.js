function balanceArray(arr) {
    let leftSum = 0;
    let rightSum = 0;
    let minValues = [];

    // calc left leftSum
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < i; j++) {
            leftSum += arr[j];
        }
    
        // calc rightSum
        for (let k = i + 1; k < arr.length; k++) {
            rightSum += arr[k];
        }

        // compares both values to see if left and right
        // sides are =. If so, index val is added into an
        // array where Math.min will calc its val
        if (leftSum === rightSum) {
            minValues.push(i);
        }
        leftSum = 0;
        rightSum = 0;
    }

    return Math.min(minValues);

}


function main() {
    let array = [3, 4, 4, 5, 2]; // expected answer: 3

    let balanced = balanceArray(array);

    console.log(balanced);
}

main()