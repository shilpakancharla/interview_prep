import heapq

class MedianFinder:
    def __init__(self):
        self.count = 0
        self.min_heap = [] # Default heapq is smallest element as root
        self.max_heap = [] # Modify heapq in max heap by making numbers negative, whenever pushed or popped

    """
        Adds a number to the data structure.
    """
    def add_number(self, num):
        if self.count % 2 == 0:
            if len(self.min_heap) == 0:
                heapq.heappush(self.min_heap, num)
            else:
                if num <= -self.max_heap[0]:
                    heapq.heappush(self.max_heap, -num)
                    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                else:
                    heapq.heappush(self.min_heap, num)
        else:
            if num >= self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            else:
                heapq.heappush(self.max_heap, -num)

        self.count += 1

    """
        Returns the median of current data stream.
    """
    def find_median(self):
        if self.count % 2 == 0:
            return (float(self.min_heap[0]) + float(-self.max_heap[0])) / 2.0
        else:
            return float(self.min_heap[0])
