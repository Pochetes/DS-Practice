class Heap:
    def __init__(self):
        self.heap = []

    def leftChild(self, index):
        return (index * 2) + 1
    
    def rightChild(self, index):
        return (index * 2) + 2
    
    def getSize(self):
        return len(self.heap)

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
        self.heap.append(key)
        self.heapifyUp(self.getSize() - 1)

    def heapifyUp(self, index):
        # swaps with parent node if parent > currNode until max heap variant is satisfied
        while self.hasParentNode(index) and self.heap[self.parentNode(index)] < self.heap[index]:
            self.swap(index, self.parentNode(index))
            index = self.parentNode(index) # this continues the while loop onto the next comparison

    def printHeap(self):
        print(self.heap)

    def findMax(self):
        print(self.heap[0])

    def delete(self):
        # swaps the root node with the last node
        # deletes connection of the last node (which was previously the root node to delete)
        # starts the "sink" process until max heap variant is satisfied
        if self.heap == 0:
            return -1
        lastIndex = len(self.heap) - 1
        self.swap(0, lastIndex)
        root = self.heap.pop()
        self.heapifyDown(0)
        return root
    
    def heapifyDown(self, index):
        while self.hasLeftChild(index):
            maxChild = self.getMaxChild(index)

            if maxChild == -1:
                break
            # after finding maxChild, compare with currNode to see if it should
            # be bubbled down the tree
            if self.heap[index] < self.heap[maxChild]:
                self.swap(index, maxChild)
                index = maxChild
            else:
                break
    
    def getMaxChild(self, index):
        # checks if left and right children exist
        if self.hasLeftChild(index):
            left_child = self.leftChild(index)
            if self.hasRightChild(index):
                right_child = self.rightChild(index)
                # compare to see which one is greater to compare with currNode
                if self.heap[left_child] > self.heap[right_child]:
                    return left_child
                else:
                    return right_child
        else:
            return -1

def main():
    maxHeap = Heap()

    maxHeap.insert(10)
    maxHeap.insert(5) 
    maxHeap.insert(55)
    maxHeap.insert(1)
    maxHeap.insert(99)
    maxHeap.insert(24)

    print("Before deleting")
    maxHeap.printHeap()
    maxHeap.findMax()

    maxHeap.delete()

    print("After deleting")
    maxHeap.printHeap()
    maxHeap.findMax()

if __name__ == "__main__":
    main()