class MedianFinder:

    def __init__(self):
        self.left = [] #max of small half -maxheap so negate nums
        self.right = [] # min of large half

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 and len(self.right) == 0:
            heapq.heappush(self.left, -num)
            return
        
        if -self.left[0] >= num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if (len(self.left) - len(self.right)) >1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        elif (len(self.right) - len(self.left)) >1:
            val = -heapq.heappop(self.right)
            heapq.heappush(self.left, val)

    def findMedian(self) -> float:
        if len(self.left) < len(self.right):
            return self.right[0]
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return ((-self.left[0] + self.right[0]) / 2)
        
        