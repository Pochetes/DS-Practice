def main():
    Array = [12, 19, 11, 17, 12, 19, 14, 10, 10, 14]
    SelectionSort(Array)

def SelectionSort(arr):
    # algorithm that sorts through subsections by finding the smallest value from
    # i + 1 to the rest of the array and swapping it with the value at index i
    # i would then move to the next index and repeat the process
    # time complexity would be O(N^2) worst case
    # [12, 19, 11, 17, 12, 19, 14, 10, 10, 14] --> i = 12, smallest = first 10
    # swap 12 and 10, move to 19 and iterate through 11 and forward
    # repeat process

    for i in range(len(arr) - 1):

        minIndex = i
        for j in range(i + 1, len(arr)):
            
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    
    print("SORTED ARRAY: ", arr)


main()
