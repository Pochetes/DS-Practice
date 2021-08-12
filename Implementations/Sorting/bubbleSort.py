def main():
    Array = [12, 19, 11, 17, 12, 19, 14, 10, 10, 14]
    BubbleSort(Array)

def BubbleSort(arr):
    # Bubble sort will have two pointers. One starting at the beginning and one starting at
    # the length of arr - i. One full iteration will have sorted the first number all the way to the end
    # if curr index value is greater than its adjacent counterpart, swap them.

    if not arr: # if array is empty
        print("EMPTY")

    for i in range(1, len(arr)): 
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    print("BUBBLE SORTED ARRAY: ", arr)

main()
