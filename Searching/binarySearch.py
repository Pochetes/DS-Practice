def main():
    Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    toFind = int(input("Enter a number: "))
    BinarySearch(Array, toFind)

def BinarySearch(arr, key):
    # this algorithm starts at the middle of the array, checks if key is greater, less, or equal to number at mid
    # if key > number at mid --> that means number is on the left side of mid
    # array will now check from low to mid - 1
    # if key < number at mid --> that means number is on the right side of mid
    # array will now check from mid + 1 to high
    # the algorithm divides the amount to iterate through by 2
    # time complexity at runtime is O(log n)

    low = 0
    high = len(arr) - 1

    if not arr:
        print("EMPTY")
        return

    while (low <= high):
        mid = (high + low) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            print(key, " WAS FOUND")
            return
    
    print(key, " WAS NOT FOUND")
    return

main()