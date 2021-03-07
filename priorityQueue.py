import math

class Queue():
    """ My implementation of a Priority Queue using Heap"""
    """ When performing the operations, ensure the heap is more than 5 elements """
    def __init__(self):
        self.heap = []

    def getParent(self, index):
        return math.floor(index/2)

    def getLeft(self, index):
        return (2 * index) 

    def getRight(index):
        return (self, 2 * index) + 1

    def maxQ(self):
        return self.heap[0]

    def insert(self, x):
        self.heap.append(x)
        current = len(self.heap)
        correct = False
        while not correct:
            parent = self.getParent(current)
            if (self.heap[current - 1] > self.heap[parent - 1]):
                # swap current with parent
                temp = self.heap[parent - 1]
                self.heap[parent - 1] = self.heap[current - 1]
                self.heap[current - 1] = temp
                current = parent
            else:
                # done
                correct = True

    def extractMax(self):
        largest = self.maxQ()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        current = 1
        correct = False
        while not correct:
            left = self.getRight(current)
            right = self.getLeft(current)
            if (self.heap[current - 1] < self.heap[left -1 ] or self.heap[current - 1] < self.heap[right - 1]):
                # bubble down, swap with the largest child
                if self.heap[left - 1 ] > self.heap[right - 1]:
                    # swap parent with left
                    child = left
                else:
                    # swap parent with right
                    child = right
                temp = self.heap[child - 1]
                self.heap[child - 1] = self.heap[current - 1]
                self.heap[current - 1] = temp
                current = child
            else:
                # done
                correct = True


