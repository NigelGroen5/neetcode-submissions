class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # if both empty
        if len(self.left) == 0 and len(self.right) == 0:
            heapq.heappush(self.left, -num)
            return
        # if num <= top of left (max of small half)
        if num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
               
        
        # resize if uneven (>1)
        # if left size -right size > 1, pop top (max) and add to right 
        if len(self.left) - len(self.right) > 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) - len(self.left) > 1:
            val = -heapq.heappop(self.right)
            heapq.heappush(self.left, val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return ((-self.left[0] + self.right[0]) / 2)
        