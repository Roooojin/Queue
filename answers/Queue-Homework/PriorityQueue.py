
class PriorityQueue:
    def __init__(self , capacity):
        self.queue=[]
        self.capacity=capacity


    def size(self):
        return len(self.queue)


    def enQueue(self,item):
        if self.size()< self.capacity:
            self.queue.append(item)
        raise Exception("Queue is full.impossible to add a new element")

    def deQueue(self):
        if not self.is_empty():
            highest_priority = self.queue[0][1]
            highest_priority_index = 0

            for i in range(1, len(self.queue)):
                if self.queue[i][1] < highest_priority:
                    highest_priority = self.queue[i][1]
                    highest_priority_index = i

            return self.queue.pop(highest_priority_index)[0]
        else:
            raise IndexError("Cannot dequeue from an empty priority queue.")



    def isEmpty(self):
        if len(self.queue) ==0:
            return True
        return False