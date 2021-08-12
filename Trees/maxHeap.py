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
        while self.hasParentNode(index) and self.heap[self.parentNode(index)] < self.heap[index]:
            self.swap(index, self.parentNode(index))
            index = self.parentNode(index)

    def printHeap(self):
        print(self.heap)

    def findMax(self):
        print(self.heap.pop(0))

def main():
    maxHeap = Heap()

    maxHeap.insert(10)
    maxHeap.insert(5) 
    maxHeap.insert(55)
    maxHeap.insert(1)
    maxHeap.insert(99)
    maxHeap.insert(24)

    maxHeap.printHeap()
    maxHeap.findMax()

if __name__ == "__main__":
    main()