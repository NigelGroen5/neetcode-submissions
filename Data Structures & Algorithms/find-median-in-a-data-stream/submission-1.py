class MedianFinder:

    def __init__(self):
        self.left = [] # max-heap of small half
        self.right = [] # min-heap of big half

    def addNum(self, num: int) -> None:
        if len(self.left) == 0  and len(self.right) == 0:
            heapq.heappush(self.left, -num)
            return
        
        # compare to left top. bigger -> right, smaller -> left
        if num >= -self.left[0]:
            heapq.heappush(self.right, num)
        else: 
            heapq.heappush(self.left, -num)
        
        # resize if needed
        if len(self.left) - len(self.right) > 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) - len(self.left) > 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        return 


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
        