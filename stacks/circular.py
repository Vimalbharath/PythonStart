class FullQueueError(Exception):
    """Exception raised for errors in the Circular Queue when it's full."""
    pass

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        return self.front == -1
        
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            # Raise a custom exception instead of printing
            raise FullQueueError("Queue is full.")
        
        if self.is_empty():
            self.front = 0
            
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            # Raise a standard IndexError instead of printing
            raise IndexError("Queue is empty.")
        
        item = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return item
        
    def peek(self):
        if self.is_empty():
            # Raise a standard IndexError
            raise IndexError("Queue is empty.")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
            
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example Usage:
cq = CircularQueue(3)

try:
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.display()
    
    # This will raise an exception
    cq.enqueue(4)
except FullQueueError as e:
    print(f"\nCaught Exception: {e}")

try:
    print("\nDequeued:", cq.dequeue())
    print("Dequeued:", cq.dequeue())
    print("Dequeued:", cq.dequeue())
    
    # This will raise an exception
    cq.dequeue()
except IndexError as e:
    print(f"Caught Exception: {e}")