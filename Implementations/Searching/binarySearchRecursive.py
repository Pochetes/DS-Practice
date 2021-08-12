def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50]
    low = 0
    high = len(arr) - 1
    searchNum = int(input("Search a number "))
    
    binarySearchRecursive(arr, low, high, searchNum)


def binarySearchRecursive(arr, l, h, key):
    if l <= h:
        mid = (l + h) // 2
        if key < arr[mid]:
            binarySearchRecursive(arr, l, mid - 1, key)
        elif key > arr[mid]:
            binarySearchRecursive(arr, mid + 1, h, key)
        elif key == arr[mid]:
            print(key, " WAS FOUND")
            return
    else: 
        print(key, " WAS NOT FOUND")
        return

main()