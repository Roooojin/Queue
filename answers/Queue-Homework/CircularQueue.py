class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if not self.is_full():
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.max_size
            self.count += 1
        else:
            raise Exception("Circular queue is full. Cannot enqueue item.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max_size
            self.count -= 1
            return item
        else:
            raise Exception("Circular queue is empty. Cannot dequeue item.")

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.max_size

    def size(self):
        return self.count


def josephus(n, k):
    # Create a circular queue with n participants
    queue = CircularQueue(n)

    # Add participants to the queue
    for i in range(1, n + 1):
        queue.enqueue(i)

    # Eliminate participants until only one remains
    while queue.size > 1:
        # Skip k-1 participants
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        # Eliminate the k-th participant
        queue.dequeue()

    # Return the position of the last remaining participant
    return queue.dequeue()