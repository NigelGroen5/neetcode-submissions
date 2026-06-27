class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        l = 0
        for i in range(len(prices)):
            if prices[l] > prices[i]:
                l = i
            elif prices[l] < prices[i]:
                max_price = max(max_price, prices[i]- prices[l])
        return max_price
            

#right always goes up 1
# look at left and right, if left is lower move left to right
# if right is higher see if can update max

