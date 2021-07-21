class Queue:
    def __init__(self):
        self.queue = []
    
    # adds items to queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # let go of earliest queue item
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # returns size of queue
    def size(self):
        return len(self.queue)

    # prints out items in the queue
    def print(self):
        for item in self.queue:
            print(item)

def main():
    songsList = Queue()

    songsList.enqueue("Deep End Freestyle")
    songsList.enqueue("PIN PIN")
    songsList.enqueue("Good for u")

    songsList.print()
    songsList.dequeue()
    print()
    songsList.print()

    songsList.dequeue()
    print()
    songsList.print()
    songsList.enqueue("Friends")
    print()
    songsList.print()
    


if __name__ == "__main__":
    main()