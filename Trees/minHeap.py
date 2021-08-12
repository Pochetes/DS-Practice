# heap constructor
class Heap:
    def __init__(self):
        self.heap = []
  
# [4, 50, 7, 55, 58, 87, 33]
#  0  1   2  3   4   5   6

    # action functions
    def leftChild(self, index):
        return (2 * index) + 1

    def rightChild(self, index):
        return (2 * index) + 2

    def parentNode(self, index):
        return (index - 1) // 2

    def hasParentNode(self, index):
        return self.parentNode(index) >= 0

    def hasBothChildren(self, index):
        return self.leftChild(index) < len(self.heap) and self.rightChild(index) < len(self.heap)

    def swap(self, index, parentIndex):
        temp = self.heap[index]
        self.heap[index] = self.heap[parentIndex] 
        self.heap[parentIndex] = temp

    def insert(self, key):
        self.heap.append(key) # add to the end of the complete binary tree and heapify up
        self.heapifyUp(len(self.heap) - 1)

    def heapifyUp(self, index):
        # swaps with parent node if parent > currNode until min heap variant is satisfied
        while self.hasParentNode(index) and self.heap[self.parentNode(index)] > self.heap[index]:
            self.swap(index, self.parentNode(index))
            index = self.parentNode(index) # this continues the while loop onto the next comparison

    def printHeap(self):
        print(self.heap)

    def findMin(self):
        print(self.heap.pop(0))

# execution function
def main():
    minHeap = Heap()

    minHeap.insert(10)
    minHeap.insert(5) 
    minHeap.insert(55)
    minHeap.insert(1)
    minHeap.insert(99)
    minHeap.insert(24)

    minHeap.printHeap()
    minHeap.findMin()

if __name__ == "__main__":
    main()


