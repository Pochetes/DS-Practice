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

    def hasLeftChild(self, index):
        return self.leftChild(index) < len(self.heap)
        
    def hasRightChild(self, index):    
        return self.rightChild(index) < len(self.heap)

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
        print(self.heap[0])
    
    def delete(self):
        # swaps the root node with the last node
        # deletes connection of the last node (which was previously the root node to delete)
        # starts the "sink" process until max heap variant is satisfied
        if len(self.heap) == 0:
            return -1
        lastIndex = len(self.heap) - 1
        self.swap(0, lastIndex)
        root = self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyDown(self, index):
        while self.hasLeftChild(index):
            minChild = self.getMinChild(index)

            if minChild == -1:
                break
            # after finding minChild, compare with currNode to see if it should
            # be bubbled down the tree
            if self.heap[index] > self.heap[minChild]:
                self.swap(index, minChild)
                index = minChild
            else:
                break
    
    def getMinChild(self, index):
        # checks if left and right children exist
        if self.hasLeftChild(index):
            left_child = self.leftChild(index)
            if self.hasRightChild(index):
                right_child = self.rightChild(index)
                # compare to see which one is lesser to compare with currNode
                if self.heap[left_child] < self.heap[right_child]:
                    return left_child
                else:
                    return right_child
        else:
            return -1

# execution function
def main():
    minHeap = Heap()

    minHeap.insert(10)
    minHeap.insert(5) 
    minHeap.insert(55)
    minHeap.insert(1)
    minHeap.insert(99)
    minHeap.insert(24)

    print("Before deleting")
    minHeap.printHeap()
    minHeap.findMin()

    minHeap.delete()

    print("After deleting")
    minHeap.printHeap()
    minHeap.findMin()

if __name__ == "__main__":
    main()


