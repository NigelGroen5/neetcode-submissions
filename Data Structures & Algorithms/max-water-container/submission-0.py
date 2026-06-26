class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        while (l<r):
            width = r-l
            height = min(heights[l],heights[r])
            water = width * height
            max_water = max(max_water, water)
            if heights[l] < heights[r]:
                l+= 1
                continue
            else:
                r-= 1
                continue
        return max_water

# question: bars can't move, can only make one container. 
# max out water. width * height.
'''
width = distance between indices
height = smaller of bars
'''
